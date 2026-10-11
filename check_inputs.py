"""Quick input availability check; does not execute the analysis."""
from pathlib import Path
from lung_mirna_utils import COHORTS, TCGA_FILE, find_data_dir
import pandas as pd

base = Path(find_data_dir())
files = [v["file"] for v in COHORTS.values()] + [TCGA_FILE]
errors = []
for filename in files:
    path = base / filename
    if not path.is_file():
        errors.append(f"MISSING: {path}")
        continue
    cols = set(pd.read_csv(path, nrows=0).columns)
    required = {"class_type"} if filename == TCGA_FILE else {"sample_id", "class_type"}
    missing = required - cols
    if missing:
        errors.append(f"MISSING COLUMNS {sorted(missing)}: {path}")
    else:
        print(f"OK: {filename}")
alias = Path(__file__).with_name("mirbase_hsa_alias_all_versions.csv")
if not alias.is_file():
    errors.append(f"MISSING: {alias}")
else:
    cols = set(pd.read_csv(alias, nrows=0).columns)
    if not {"acc", "sym"} <= cols:
        errors.append(f"ALIAS MISSING COLUMNS: {alias}")
if errors:
    raise SystemExit("\n".join(errors))
print("Input filenames and required headers verified. Full analysis not tested.")
