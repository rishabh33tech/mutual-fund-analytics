import pandas as pd
import os

RAW_FOLDER = "data/raw"

print("=" * 70)
print("DATA INGESTION STARTED")
print("=" * 70)

for file in os.listdir(RAW_FOLDER):

    if file.endswith(".csv"):

        filepath = os.path.join(RAW_FOLDER, file)

        print("\n" + "=" * 70)
        print(f"FILE: {file}")
        print("=" * 70)

        try:

            df = pd.read_csv(filepath)

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

        except Exception as e:
            print(f"Error reading {file}")
            print(e)

print("\nData ingestion completed.")