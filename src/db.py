from sqlalchemy import create_engine
import pandas as pd
from fetch import fetch_from_yahoo

def load_to_sql (df:pd.DataFrame) :

    engine = create_engine("postgresql://postgres@localhost:5432/stock_db")

    with engine.connect() as conn:

        df.to_sql(name="stock",if_exists='replace', index= False, con= engine)
        print("✅ Connected to PostgreSQL and data saved")

stock = fetch_from_yahoo()

load_to_sql(stock)
