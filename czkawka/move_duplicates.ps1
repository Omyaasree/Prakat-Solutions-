# Path to your Czkawka output
$dupes = Get-Content "duplicates.txt"

# Folder to move ALL duplicate group files to
$inspect = "C:\Users\Public\Pictures\omyaa\Trash"

# Make sure Inspect folder exists
if (-not (Test-Path $inspect)) {
    New-Item -ItemType Directory -Path $inspect | Out-Null
}

# Variables
$group = @()

foreach ($line in $dupes) {
    if ($line -match '^----') {
        # New group found
        if ($group.Count -gt 0) {
            # Move ALL files in this group
            $group | ForEach-Object {
                $path = $_ -replace '"', ''
                if (Test-Path $path) {
                    $filename = Split-Path $path -Leaf
                    $dest = Join-Path $inspect $filename
                    Move-Item -Path $path -Destination $dest -Force
                    Write-Output "Moved: $path -> $dest"
                } else {
                    Write-Output "WARNING: $path not found, skipping"
                }
            }
        }
        # Reset group
        $group = @()
    }
    elseif ($line -match '^"') {
        $group += $line
    }
}

# Process last group if needed
if ($group.Count -gt 0) {
    $group | ForEach-Object {
        $path = $_ -replace '"', ''
        if (Test-Path $path) {
            $filename = Split-Path $path -Leaf
            $dest = Join-Path $inspect $filename
            Move-Item -Path $path -Destination $dest -Force
            Write-Output "Moved: $path -> $dest"
        } else {
            Write-Output "WARNING: $path not found, skipping"
        }
    }
}

Write-Output "✅ Done! All group files moved to: $inspect"
