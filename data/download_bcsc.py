"""
data/download_bcsc.py
Run this once to download the BCSC risk-factor dataset into
data/raw/stage1_bcsc/. Running this script (instead of manually
downloading) guarantees every team member ends up with the same
folder structure and file names.

NOTE: BCSC requires free registration at bcsc-research.org before
you can download. Fill in your access credentials/download URL
below once you have them.
"""
import os

RAW_DIR = "data/raw/stage1_bcsc"

def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    print(f"Place BCSC files in: {RAW_DIR}")
    print("Register for access at: https://www.bcsc-research.org/")
    # TODO: add actual download logic once access is granted
    # e.g. using requests.get() with your registered download URL

if __name__ == "__main__":
    main()
