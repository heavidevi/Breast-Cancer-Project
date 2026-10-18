# Two-Tier Breast Cancer Risk Stratification Project

## Team
- Person A — Stage 1 (Risk-Factor Screening Model) — [Name, ID]
- Person B — Stage 1.5 (Imaging CNN Model) — [Name, ID]
- Person C — Stage 2 (Diagnostic Model) + Integration Lead — [Name, ID]

## What this project does
A three-stage, cost-gated breast cancer triage pipeline:
1. **Stage 1** — low-cost risk-factor screening (BCSC dataset) -> flags who needs imaging
2. **Stage 1.5** — mammogram imaging classifier (CBIS-DDSM dataset) -> flags who needs biopsy
3. **Stage 2** — FNA cytology diagnostic support (Wisconsin WDBC dataset) -> supports pathologist diagnosis

See `CONTRACT.md` for the shared conventions every team member follows.

## How to run this project

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the relevant download script in `data/` for the dataset you need
   (e.g. `python data/download_bcsc.py`)
4. Open the relevant notebook in `notebooks/`
5. Trained model files are NOT stored in this repo — see `models/README.md`
   for Google Drive download links

## Folder structure

See `docs/ARCHITECTURE.md` for the full explanation of this repo's layout
and how it links to the shared Google Drive folder.
