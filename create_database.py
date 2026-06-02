import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

BASE_DIR = Path(__file__).parent

DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

print("Loading CSV files...")

fund_master = pd.read_csv(BASE_DIR / "data" / "raw" / "01_fund_master.csv")
nav_history = pd.read_csv(BASE_DIR / "data" / "raw" / "02_nav_history.csv")
aum = pd.read_csv(BASE_DIR / "data" / "raw" / "03_aum_by_fund_house.csv")
sip = pd.read_csv(BASE_DIR / "data" / "raw" / "04_monthly_sip_inflows.csv")
transactions = pd.read_csv(BASE_DIR / "data" / "raw" / "08_investor_transactions.csv")
holdings = pd.read_csv(BASE_DIR / "data" / "raw" / "09_portfolio_holdings.csv")
benchmark = pd.read_csv(BASE_DIR / "data" / "raw" / "10_benchmark_indices.csv")

print("Writing tables to SQLite...")

fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_history.to_sql("fact_nav", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
sip.to_sql("fact_sip", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
holdings.to_sql("fact_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("fact_benchmark", engine, if_exists="replace", index=False)

print("Database created successfully!")
print(DB_PATH)