# Prakat-Solutions
Internship 2025

# 🏥 HealthGov Synthetic Health Data Generator & Analysis

> **By Omyaasree Balaji**
> Internship Project — *Transforming open-ended health data exploration into a reproducible, scalable, real-world pipeline.*

---

## 🚀 **Overview**

During my internship, I tackled a challenging open-ended problem:

> *“How can we generate, process, and analyze large-scale, realistic health data without violating patient privacy — and deliver meaningful insights for public health policy and predictive modeling?”*

Many organizations struggle with limited or restricted access to granular patient-level data due to privacy laws. To solve this, I built a **fully automated, end-to-end pipeline** that:

* 💡 **Generates** realistic synthetic health records at scale.
* ⚡ **Cleans & standardizes** the data for analysis.
* 📊 **Visualizes** trends to inform real-world health insights.

---

## 🔑 **Key Highlights**

✅ **Synthetic data at scale** — Used [Synthea](https://github.com/synthetichealth/synthea) to generate up to 100,000 realistic patient records with demographics, conditions, DALYs/QALYs, claims, and more.

✅ **Cross-tool data engineering** — Wrote robust **Python scripts** to extract, transform, and flatten complex nested FHIR JSON data into clean CSV/XLSX files.

✅ **Parallel processing** — Leveraged Python’s `ThreadPoolExecutor` to process large file sets efficiently.

✅ **Flexible data design** — Experimented with manual generation, hashmaps, name-gender prediction APIs, and fallback logic before optimizing with Synthea.

✅ **Clean analytical pipeline in R** — Standardized messy fields, calculated age groups, and grouped DALYs/QALYs for better population health insight.

✅ **Reproducible visual reporting** — Used `RMarkdown` and `ggplot2` for bar charts, pie charts, scatter plots, and trend lines to validate generated data against ideal health benchmarks.

✅ **Practical real-world impact** — Provides a reusable framework for organizations that need realistic test data for policy simulations, dashboards, or machine learning experiments — without privacy risks.

---

## 📊 **Core Outputs**

* **Raw synthetic patient dataset** — includes:

  * PatientID, full demographics, conditions, medications, observations, claims.
  * Disability-Adjusted Life Years (DALYs) & Quality-Adjusted Life Years (QALYs).

* **Reusable extractor** — customizable Python scripts to parse FHIR bundles to CSV/XLSX.

* **Cleaned analysis-ready Excel files** — easy for teams to inspect or hand off.

* **Graphs & RMarkdown report** — gender splits, marital status, ethnic subgroups, condition vs DALY relationships, and ideal trend overlays.

---

## ⚙️ **Tech Stack**

* **Synthea**: Synthetic health record generator (Java 17).
* **Python**: Data extraction, parsing, and concurrency.
* **R**: Data cleaning, analysis, visualization, and reporting.
* **Git**: Version control and reproducibility.
* **Excel/XLSX**: Final deliverables for non-technical stakeholders.

---

## 🧠 **What I Learned**

* Navigating real-world limitations when official data is restricted.
* Automating pipelines to handle **large JSON datasets** reliably.
* Combining open-source tools creatively to solve practical health data gaps.
* Communicating complex data processes clearly through reproducible notebooks and visuals.
* Balancing manual data inspection with automated cleaning to ensure realistic results.

---

## 📌 **Project Structure**

```
├── Data.java             # Early name-gen/hashmap experiments
├── DataGen.py            # Manual data generation logic
├── ExtractInfo.py        # Main JSON-to-CSV/XLSX extractor
├── synthea_output.xlsx   # Final cleaned patient dataset
├── HealthGov.Rmd         # RMarkdown analysis and plots
├── Graphs/               # Saved plots and visuals
├── HealthGov.docx        # Report/deliverable draft
├── README.md             # Project documentation
```

---

## 💼 **Why This Matters**

This project shows that I can:

* Take an ambiguous, open-ended problem and build a structured, practical solution.
* Engineer scalable, privacy-safe health datasets to simulate real-world scenarios.
* Communicate findings clearly through well-documented code, clean deliverables, and meaningful visuals.
