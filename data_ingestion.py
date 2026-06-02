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




print("\n" + "="*70)
print("AMFI CODE VALIDATION")
print("="*70)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print(f"Fund Master Codes: {len(master_codes)}")
print(f"NAV History Codes: {len(nav_codes)}")

if len(missing_codes) == 0:
    print("SUCCESS: All AMFI codes exist in NAV history")
else:
    print("Missing Codes:")
    print(missing_codes)