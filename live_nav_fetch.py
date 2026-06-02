import requests
import pandas as pd
import os

os.makedirs("data/raw/live_nav", exist_ok=True)

funds = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            meta = data.get("meta", {})

            df = pd.DataFrame([meta])

            filename = f"data/raw/live_nav/{fund_name}.csv"

            df.to_csv(filename, index=False)

            print(f"Saved {filename}")

        else:
            print(f"Failed for {fund_name}")

    except Exception as e:
        print(f"Error fetching {fund_name}")
        print(e)