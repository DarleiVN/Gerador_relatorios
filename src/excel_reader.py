import pandas as pd

def carregar_vendas(caminho_excel: str) -> pd.DataFrame:
    df = pd.read_excel(caminho_excel)

    # remove linhas totalmente vazias
    df = df.dropna(how="all")

    #  É para converter data
    df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")

    
    df = df.dropna(subset=["data_venda"])

    return df