from excel_reader import carregar_vendas
from db_loader import salvar_vendas_no_db
from metrics import (
    faturamento_total,
    faturamento_por_mes,
    faturamento_por_categoria,
    faturamento_por_pagamento,
    faturamento_por_vendedor
)
from charts import (
    grafico_faturamento_por_mes,
    grafico_faturamento_por_categoria,
    grafico_faturamento_por_pagamento,
    grafico_faturamento_por_vendedor    
)
from xlsx_generator import gerar_relatorio_xlsx
from pdf_generator import gerar_relatorio_pdf

def main():
    print("Carregando planilha...")
    df = carregar_vendas("data/input/vendas.xlsx")
    print("Primeiras linhas:")
    print(df.head())

    print("\nSalvando no banco de dados...")
    salvar_vendas_no_db(df, "data/database/vendas.db")

    caminho_db = "data/database/vendas.db"

    print("\nCalculando métricas...")

    total = faturamento_total(caminho_db)
    print(f"Faturamento total: R$ {total:.2f}")

    df_mes = faturamento_por_mes(caminho_db)
    df_cat = faturamento_por_categoria(caminho_db)
    df_pag = faturamento_por_pagamento(caminho_db)
    df_vend = faturamento_por_vendedor(caminho_db)

    print("\nGerando gráficos...")

    pasta_charts = "output"

    grafico_faturamento_por_mes(df_mes, pasta_charts)
    grafico_faturamento_por_categoria(df_cat, pasta_charts)
    grafico_faturamento_por_pagamento(df_pag, pasta_charts)
    grafico_faturamento_por_vendedor(df_vend, pasta_charts)

    print("\nGráficos gerados na pasta:", pasta_charts)
    print("\nProcesso concluído com sucesso!")

 # Escolher o tipo de relatório

    print("\nQual relatório deseja gerar?")
    print("1 - XLSX")
    print("2 - PDF")
    print("3 - Ambos")


    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        print("\nGerando relatório XLSX...")
        gerar_relatorio_xlsx(df_mes, df_cat, df_pag, df_vend, total)
        print("Relatório XLSX gerado em output/relatorio.xlsx")

    elif escolha == "2":
        print("\nGerando relatório PDF...")
        gerar_relatorio_pdf(df_mes, df_cat, df_pag, df_vend, total)
        print("Relatório PDF gerado em output/relatorio.pdf")

    elif escolha == "3":
        print("\nGerando relatório XLSX...")
        gerar_relatorio_xlsx(df_mes, df_cat, df_pag, df_vend, total)
        print("Relatório XLSX gerado.")

        print("\nGerando relatório PDF...")
        gerar_relatorio_pdf(df_mes, df_cat, df_pag, df_vend, total)
        print("Relatório PDF gerado.")

    else:
        print("Opção inválida. Nenhum relatório foi gerado.")

    print("\nProcesso concluído com sucesso!")




    pasta_charts = ""
if __name__ == "__main__":
    main()