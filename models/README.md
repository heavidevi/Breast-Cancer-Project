# Trained Model Artifacts

Model weight files are NOT stored in this Git repo (too large, and
binary files don't version well in Git). They live in the shared
Google Drive folder: `Breast-Cancer-Project/trained_models/`

Update this table every time a new model version is trained:

## Stage 1 — Risk-Factor Model
| File | Trained by | Date | Recall | Precision | Drive Link |
|---|---|---|---|---|---|
| stage1_xgboost_v1.pkl | Person A | YYYY-MM-DD | | | [link] |
| stage1_scaler_v1.pkl | Person A | YYYY-MM-DD | - | - | [link] |

## Stage 1.5 — Imaging CNN
| File | Trained by | Date | Recall | Precision | Drive Link |
|---|---|---|---|---|---|
| stage1_5_cnn_resnet18_v1.pt | Person B | YYYY-MM-DD | | | [link] |

## Stage 2 — Diagnostic Model
| File | Trained by | Date | Recall | Precision | Drive Link |
|---|---|---|---|---|---|
| stage2_xgboost_v1.pkl | Person C | YYYY-MM-DD | | | [link] |
| stage2_scaler_v1.pkl | Person C | YYYY-MM-DD | - | - | [link] |

**Rule:** never overwrite a previous version — add a new version number
and keep the old one in Drive, in case a new training run performs worse.
