import sqlite3
import pandas as pd

conn = sqlite3.connect("data/database/vendas.db")
df = pd.read_sql_query("SELECT * FROM vendas", conn)
print(df.head())
print(df.columns)
conn.close()
