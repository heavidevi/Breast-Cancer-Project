"""
data/download_cbis_ddsm.py
Run this once to download CBIS-DDSM into data/raw/stage1_5_cbis_ddsm/.
CBIS-DDSM is hosted on The Cancer Imaging Archive (TCIA) and requires
the NBIA Data Retriever tool or TCIA's API.

NOTE: this dataset is large (several GB). Consider downloading once
to the shared Google Drive folder, then having each team member pull
from there instead of all three hitting TCIA separately.
"""
import os

RAW_DIR = "data/raw/stage1_5_cbis_ddsm"

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    print(f"Place CBIS-DDSM files in: {RAW_DIR}")
    print("Register for access at: https://www.cancerimagingarchive.net/")
    # TODO: add NBIA Data Retriever or TCIA API download logic

if __name__ == "__main__":
    main()
