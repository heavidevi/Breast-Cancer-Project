# Trained Model Files

Store versioned model artifacts here. NEVER overwrite a previous
version -- add a new version number instead, so you can roll back
if a new training run performs worse.

Expected files (filled in as each stage is trained):
- stage1_xgboost_v1.pkl
- stage1_scaler_v1.pkl
- stage1_5_cnn_resnet18_v1.pt
- stage2_xgboost_v1.pkl
- stage2_scaler_v1.pkl

After uploading a new file here, add its shareable link to the
GitHub repo's models/README.md table (trainer, date, recall, link).
