import os
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd

# === CONFIG ===
FHIR_DIR = r"C:\Users\ojasb\OneDrive\Desktop\Prakat\HealthgGov\synthea\output\fhir"
OUTPUT_XLSX = "synthea_output.xlsx" # NO CSV SO THAT I CAN OPEN IN EXCEL

# === CSV columns ===
FIELDNAMES = [
    "PatientID", "FirstName", "LastName", "Gender", "BirthDate", "MaritalStatus", "Ethnicity",
    "BirthSex", "BirthPlace_City", "Address_Line", "Address_City", "Address_PostalCode",
    "Phone", "SSN", "DriverLicenseNumber", "PassportNumber",
    "DisabilityAdjustedLifeYears", "QualityAdjustedLifeYears",
    "ConditionCount", "Conditions", "MedicationCount", "Medications",
    "ObservationCount", "Observations",
    "ClaimCount", "TotalClaimedAmount", "InsuranceProvider"
]

def process_file(filepath):
    with open(filepath, "r", encoding='utf-8') as f:
        data = json.load(f)

    patient_resource = None
    for entry in data.get("entry", []):
        res = entry["resource"]
        if res.get("resourceType") == "Patient":
            patient_resource = res
            break

    if not patient_resource:
        return None

    row = {field: "" for field in FIELDNAMES}
    row["PatientID"] = patient_resource.get("id", "")
    name = patient_resource.get("name", [{}])[0]
    row["FirstName"] = name.get("given", [""])[0] if name.get("given") else ""
    row["LastName"] = name.get("family", "")
    row["Gender"] = patient_resource.get("gender", "")
    row["BirthDate"] = patient_resource.get("birthDate", "")
    row["MaritalStatus"] = patient_resource.get("maritalStatus", {}).get("text", "")
    row["Address_Line"] = patient_resource.get("address", [{}])[0].get("line", [""])[0] if patient_resource.get("address") else ""
    row["Address_City"] = patient_resource.get("address", [{}])[0].get("city", "")
    row["Address_PostalCode"] = patient_resource.get("address", [{}])[0].get("postalCode", "")
    row["Phone"] = patient_resource.get("telecom", [{}])[0].get("value", "")

    for ident in patient_resource.get("identifier", []):
        sys = ident.get("system", "")
        if "us-ssn" in sys:
            row["SSN"] = ident.get("value", "")
        elif "4.3.25" in sys:
            row["DriverLicenseNumber"] = ident.get("value", "")
        elif "passport" in sys:
            row["PassportNumber"] = ident.get("value", "")

    for ext in patient_resource.get("extension", []):
        url = ext["url"]
        if "ethnicity" in url:
            row["Ethnicity"] = ext["extension"][1]["valueString"]
        elif "birthsex" in url:
            row["BirthSex"] = ext["valueCode"]
        elif "birthPlace" in url:
            row["BirthPlace_City"] = ext["valueAddress"]["city"]
        elif "disability-adjusted-life-years" in url:
            row["DisabilityAdjustedLifeYears"] = ext["valueDecimal"]
        elif "quality-adjusted-life-years" in url:
            row["QualityAdjustedLifeYears"] = ext["valueDecimal"]

    conditions = []
    medications = []
    observations = []
    total_claimed_amount = 0.0
    insurance_providers = set()
    claim_count = 0

    for entry in data.get("entry", []):
        res = entry["resource"]
        rtype = res.get("resourceType")

        if rtype == "Condition":
            code = res.get("code", {}).get("text") or \
                   res.get("code", {}).get("coding", [{}])[0].get("display", "")
            if code:
                conditions.append(code)

        elif rtype == "MedicationRequest":
            med = res.get("medicationCodeableConcept", {}).get("text") or \
                  res.get("medicationCodeableConcept", {}).get("coding", [{}])[0].get("display", "")
            if med:
                medications.append(med)

        elif rtype == "Observation":
            obs = res.get("code", {}).get("text") or \
                  res.get("code", {}).get("coding", [{}])[0].get("display", "")
            if obs:
                observations.append(obs)

        elif rtype == "Claim":
            claim_count += 1
            amt = res.get("total", {}).get("value", 0.0)
            total_claimed_amount += amt
            for ins in res.get("insurance", []):
                insurance_providers.add(ins.get("coverage", {}).get("display", ""))

    row["ConditionCount"] = len(conditions)
    row["Conditions"] = "; ".join(conditions)
    row["MedicationCount"] = len(medications)
    row["Medications"] = "; ".join(medications)
    row["ObservationCount"] = len(observations)
    row["Observations"] = "; ".join(observations)
    row["ClaimCount"] = claim_count
    row["TotalClaimedAmount"] = round(total_claimed_amount, 2)
    row["InsuranceProvider"] = "; ".join(list(insurance_providers))

    return row

def main():
    start_time = time.time()
    all_files = [os.path.join(FHIR_DIR, f) for f in os.listdir(FHIR_DIR) if f.endswith(".json")]
    files = all_files[:115000]  # Limit to first 100

    rows = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_file, file) for file in files]

        for i, future in enumerate(as_completed(futures), 1):
            row = future.result()
            if row:
                rows.append(row)
            print(f"✅ Processed files: {i}")

    # Save to Excel using pandas
    df = pd.DataFrame(rows, columns=FIELDNAMES)
    df.to_excel(OUTPUT_XLSX, index=False)

    elapsed = time.time() - start_time
    print(f"\n✅ Excel generated: {OUTPUT_XLSX}")
    print(f"⏱️ Time elapsed: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()
