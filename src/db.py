from sqlalchemy import create_engine
import pandas as pd

def load_to_sql (df:pd.DataFrame) :

    engine = create_engine('postgresql://postgres@localhost:5432/stock_db')
    
    df = df.reset_index()
    df.columns = df.columns.str.lower()
    df.to_sql(name="stock",if_exists='replace', index= False, con= engine)
    print("✅ Connected to PostgreSQL and data saved")

