from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT name FROM sqlite_master WHERE type='table';")
    )

    print("\nTABLES IN DATABASE:\n")

    for row in result:
        print(row[0])