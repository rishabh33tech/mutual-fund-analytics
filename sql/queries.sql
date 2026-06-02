-- Total NAV records
SELECT COUNT(*) FROM fact_nav;

-- Total schemes
SELECT COUNT(*) FROM dim_fund;

-- Total transactions
SELECT COUNT(*) FROM fact_transactions;

-- Top 10 funds by AUM
SELECT fund_house,
       MAX(aum_crore)
FROM fact_aum
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC;

-- Average NAV by fund
SELECT amfi_code,
       AVG(nav)
FROM fact_nav
GROUP BY amfi_code;