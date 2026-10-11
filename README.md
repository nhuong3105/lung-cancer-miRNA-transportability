# Lung cancer circulating miRNA signature transportability

Reproducibility code for the study:

> **Single-cohort ANOVA signatures of circulating microRNAs for lung cancer transport poorly across specimen–platform families: a one-versus-rest analysis of seven public blood cohorts with a cross-series overlap audit**

**Running title:** Transportability of circulating miRNA lung-cancer signatures

## Contents

- `PaperLu1_analysis.ipynb`: main analysis notebook (the provided executed notebook; outputs may be present).
- `lung_mirna_utils.py`: cohort loaders, miRBase harmonization, ANOVA, modeling, and overlap-audit utilities.
- `mirbase_hsa_alias_all_versions.csv`: miRNA name mapping table used by the code.
- `requirements.txt`: required Python packages (compatible ranges; original exact versions not supplied).
- `check_inputs.py`: verify data filenames and expected columns before execution.

## Data availability and layout

**The large preprocessed data matrices are NOT included in this code repository.** Obtain `Lung_miRNA_Preprocessed_Datasets.zip` from the authors or an approved public archival location **[ADD PERMANENT DATA URL / DOI BEFORE RELEASE]**, subject to original dataset reuse terms. The repository alone is not sufficient to reproduce the analysis until data access is provided.

Unzip the data archive into the repository root so that the layout is:

```text
lung-cancer-miRNA-transportability/
  PaperLu1_analysis.ipynb
  lung_mirna_utils.py
  mirbase_hsa_alias_all_versions.csv
  Lung_miRNA_Preprocessed_Datasets/
    E_MTAB_8026_STRICT_lung_vs_healthy_preprocessed.csv
    GSE137140_STRICT_lung_vs_healthy_preprocessed.csv
    GSE106817_STRICT_lung_vs_healthy_preprocessed.csv
    GSE112264_STRICT_lung_vs_healthy_preprocessed.csv
    GSE113486_STRICT_lung_vs_healthy_preprocessed.csv
    GSE31568_STRICT_lung_vs_healthy_preprocessed.csv
    GSE61741_STRICT_lung_vs_healthy_preprocessed.csv
    TCGA_Lung_miRNA_preprocessed_with_labels.csv
```

The TCGA tissue dataset is used in a later analysis step. Input matrices are preprocessed; reproducing the *original preprocessing from raw GEO/ArrayExpress data* requires separate preprocessing scripts not included here.

## Run the analysis

Use Python 3.11 or a compatible version. From the repository directory:

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python check_inputs.py
jupyter notebook PaperLu1_analysis.ipynb
```

In Jupyter, choose **Kernel → Restart Kernel and Run All Cells**. The notebook writes results to `figures/`, `tables/`, and `results_summary.json` in the current working directory. Start Jupyter from the repository root to keep paths consistent.

**Important:** This release is prepared from the supplied source files. Full end-to-end execution and matching all manuscript tables/figures have **not yet been verified** in a clean environment. The original exact package versions and data preprocessing provenance should be recorded before publication. Check cross-series overlap decisions and any feature-selection / validation leakage claims against the manuscript.

## Citation

Citation details / DOI: **[ADD AFTER PUBLICATION]**.

## License

**No license granted yet.** Select a license after checking authorship and rights for code and the miRBase-derived reference table. Dataset licenses may differ.

## Contact

GitHub: https://github.com/nhuong3105
