import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

dashboard_df = fund_master.merge(
    performance,
    on="amfi_code"
)

dashboard_df.to_csv(
    "data/processed/fund_dashboard.csv",
    index=False
)

print("Dashboard file created successfully!")