# src/data_downloader.py

import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_amazon_reviews_kaggle(dataset_name="mehmetisik/amazon-review", local_path="data/raw"):
    """
    Downloads the specified Kaggle dataset to local_path and unzips it.
    """
    # Authenticate with Kaggle
    api = KaggleApi()
    api.authenticate()

    # Ensure the directory exists
    os.makedirs(local_path, exist_ok=True)
    print(f"Downloading dataset: {dataset_name} ...")
    api.dataset_download_files(dataset_name, path=local_path, unzip=True)
    print("Download complete. Files are in:", local_path)
