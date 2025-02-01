# src/data_loader.py

import os
import pandas as pd

def load_amazon_reviews(csv_filename, nrows=None):
    """
    Loads the Amazon reviews CSV into a Pandas DataFrame.
    :param csv_filename: Full path to the CSV file.
    :param nrows: If not None, only load a subset of rows for quicker analysis.
    """
    if not os.path.exists(csv_filename):
        raise FileNotFoundError(f"CSV file not found: {csv_filename}")

    print(f"Loading data from {csv_filename} ...")
    df = pd.read_csv(csv_filename, nrows=nrows)
    print(f"Data loaded successfully with {len(df)} rows.")
    return df
