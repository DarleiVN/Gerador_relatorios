from excel_reader import carregar_vendas

df = carregar_vendas("data/vendas.xlsx")

print("Primeiras linhas:")
print(df.head())
print("\nColunas:")
print(df.columns)
print("\nTotal de linhas:", len(df))