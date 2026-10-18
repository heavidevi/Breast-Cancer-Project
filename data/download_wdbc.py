"""
data/download_wdbc.py
Run this once to download the Wisconsin Diagnostic Breast Cancer
(WDBC) dataset into data/raw/stage2_wdbc/. This one is small and
has no access restrictions — safe to automate fully.
"""
import os
import urllib.request

RAW_DIR = "data/raw/stage2_wdbc"
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    dest = os.path.join(RAW_DIR, "wdbc.data")
    print(f"Downloading WDBC to {dest} ...")
    urllib.request.urlretrieve(URL, dest)
    print("Done.")

if __name__ == "__main__":
    main()
