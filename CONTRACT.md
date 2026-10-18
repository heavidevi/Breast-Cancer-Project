# Shared Team Contract

Agree on everything below BEFORE any data collection or modeling starts.
This file is the single source of truth for naming/format conventions —
update it (via Pull Request) if the team agrees to change something, so
it never goes stale.

## Naming conventions
- Target column: always named `target` (0 = no cancer / benign, 1 = cancer / malignant)
- Patient identifier column: always named `patient_id`
- No other naming variants (no `Target`, `label`, `diagnosis_flag`, etc.) in processed data

## File structure
- Every cleaned dataset lands at: `data/processed/<stage>_cleaned.csv`
- Raw data is NEVER committed to Git — lives in `data/raw/` (gitignored) and
  in the shared Google Drive `raw_datasets/` folder

## Preprocessing conventions
- Scaler: `RobustScaler` (sklearn) unless a specific reason is documented otherwise
- Imputation: median for numeric columns, mode for categorical columns
- Train/test split: 80/20, stratified, `random_state=42` everywhere
- Class imbalance handling: class_weight="balanced" or SMOTE (document which, per stage)

## Metric reporting format
Every stage reports, in this exact order, as a table:
| Metric | Value |
|---|---|
| Recall (Sensitivity) | |
| Precision | |
| F1 | |
| PR-AUC | |
| ROC-AUC | |

## Notebook section order (every notebook follows this)
1. Load
2. Clean
3. EDA
4. Feature Engineering
5. Model Training
6. Evaluation

## Model versioning
- Every saved model file includes a version suffix: `stageX_modelname_v1.pkl`
- Never overwrite a previous version in Google Drive — add a new version number
- Log who trained it, when, and headline recall/precision in `models/README.md`
