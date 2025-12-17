import sqlite3
import pandas as pd

def criar_conexao(caminho_db: str):
    conn = sqlite3.connect(caminho_db)
    return conn

def salvar_vendas_no_db(df: pd.DataFrame, caminho_db: str):
    # cria a coluna faturamento
    df["faturamento"] = df["quantidade"] * df["preco_unitario"]

    conn = criar_conexao(caminho_db)
    df.to_sql("vendas", conn, if_exists="replace", index=False)
    conn.close()