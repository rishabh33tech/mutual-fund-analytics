-- Fund Dimension
CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

-- NAV Facts
CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

-- AUM Facts
CREATE TABLE fact_aum (
    date DATE,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL
);

-- SIP Facts
CREATE TABLE fact_sip (
    month TEXT,
    sip_inflow_crore REAL
);

-- Transactions
CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    amount_inr REAL
);