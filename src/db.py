from sqlalchemy import create_engine
import pandas as pd
import os

def load_to_sql (df:pd.DataFrame) :

    database_url = os.getenv("DATABASE_URL", 
                             "postgresql://postgres@localhost:5432/stock_db")

    engine = create_engine(database_url)
    
    df = df.reset_index()
    df.columns = df.columns.str.lower()
    df.to_sql(name="stock",if_exists='replace', index= False, con= engine)
    print("✅ Connected to PostgreSQL and data saved")

