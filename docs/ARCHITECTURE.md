# Architecture Notes

This repo is organized by pipeline stage, not by task type, so each
team member can own a self-contained slice end-to-end:

- Person A -> Stage 1 (src/stage1/, notebooks/stage1_personA.ipynb)
- Person B -> Stage 1.5 (src/stage1_5/, notebooks/stage1_5_personB.ipynb)
- Person C -> Stage 2 + integration (src/stage2/, notebooks/stage2_personC.ipynb,
  notebooks/final_combined_report.ipynb)

## Where data lives
- data/raw/   -> gitignored, populated locally via data/download_*.py scripts
- data/processed/ -> small cleaned CSVs, safe to commit

## Where models live
- NOT in this repo. See models/README.md for Google Drive links.

## Google Drive folder structure (shared, Editor access for all 3)
Breast-Cancer-Project/
  raw_datasets/
    bcsc/
    cbis_ddsm/
      images/
      labels.csv
    wdbc/
  trained_models/
  figures_and_outputs/
  report_drafts/

## Git workflow
main
  stage1-personA
  stage1_5-personB
  stage2-personC
Each person works in their own branch, opens a Pull Request into
main once their piece works. Person C (integration lead) merges PRs
and checks everything matches CONTRACT.md before merging.
