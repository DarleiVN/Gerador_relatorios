import sqlite3
import pandas as pd

def criar_conexao(caminho_db: str) -> sqlite3.Connection:
    try:
        conexao = sqlite3.connect(caminho_db)
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def faturamento_total(caminho_db: str) -> float:
    conn = criar_conexao(caminho_db)
    query = """
        SELECT SUM(faturamento) AS faturamento
        FROM vendas
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df["faturamento"].iloc[0]


def faturamento_por_mes(caminho_db: str) -> pd.DataFrame:
    conn = criar_conexao(caminho_db)
    df = pd.read_sql_query("SELECT * FROM vendas", conn)
    conn.close()

    df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
    df = df.dropna(subset=["data_venda"])

    df["mes"] = df["data_venda"].dt.to_period("M").astype(str)

    df_mes = df.groupby("mes")["faturamento"].sum().reset_index()
    return df_mes


def faturamento_por_categoria(caminho_db: str) -> pd.DataFrame:
    conn = criar_conexao(caminho_db)
    query = """
        SELECT 
            categoria,
            SUM(faturamento) AS faturamento
        FROM vendas
        GROUP BY categoria
        ORDER BY faturamento DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def faturamento_por_pagamento(caminho_db: str) -> pd.DataFrame:
    conn = criar_conexao(caminho_db)
    query = """
        SELECT 
            forma_pagamento,
            SUM(faturamento) AS faturamento
        FROM vendas
        GROUP BY forma_pagamento
        ORDER BY faturamento DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def faturamento_por_vendedor(caminho_db: str) -> pd.DataFrame:
    conn = criar_conexao(caminho_db)
    query = """
        SELECT 
            vendedor,
            SUM(faturamento) AS faturamento
        FROM vendas
        GROUP BY vendedor
        ORDER BY faturamento DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df