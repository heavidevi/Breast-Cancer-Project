# Breast-Cancer-Project — Shared Google Drive Folder

This is the shared data/model/output storage for the project, linked
from the GitHub repo's `models/README.md` and `data/download_*.py`
scripts. Share this folder with "Editor" access to all 3 team members.

## Folder guide
- raw_datasets/   -> downloaded source data (BCSC, CBIS-DDSM, WDBC)
- trained_models/ -> versioned model files (.pkl, .pt) -- never overwrite, add new versions
- figures_and_outputs/ -> exported SHAP plots, Grad-CAM images, EDA charts (used directly in the report)
- report_drafts/  -> the actual Word/PowerPoint files for real-time collaborative editing

## How to set this up in real Google Drive
Google Drive does NOT auto-extract zip files on upload. To recreate
this structure in Drive:
1. Unzip this file on your computer
2. Open Google Drive in your browser
3. Drag the whole unzipped "Breast-Cancer-Project" folder into Drive
   (this preserves the full folder structure automatically)
4. Right-click the folder -> Share -> add your teammates as Editors
5. Get the folder's shareable link and paste it into the GitHub repo's
   models/README.md and docs/ARCHITECTURE.md

Alternative: use Google Drive Desktop (syncs a local folder to Drive
automatically) or `rclone` if you prefer a command-line upload.
