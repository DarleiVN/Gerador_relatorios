import pandas as pd
import xlsxwriter
import os


# Funções auxiliares para gerar descrições automáticas


def descricao_faturamento_mes(df):
    maior_mes = df.loc[df["faturamento"].idxmax()]
    menor_mes = df.loc[df["faturamento"].idxmin()]
    return (
        f"O mês de maior faturamento foi {maior_mes['mes']} "
        f"com R$ {maior_mes['faturamento']:.2f}. "
        f"O menor faturamento ocorreu em {menor_mes['mes']}."
    )

def descricao_categoria(df):
    top = df.loc[df["faturamento"].idxmax()]
    return (
        f"A categoria com maior faturamento foi {top['categoria']} "
        f"com R$ {top['faturamento']:.2f}."
    )

def descricao_pagamento(df):
    top = df.loc[df["faturamento"].idxmax()]
    return (
        f"A forma de pagamento mais utilizada foi {top['forma_pagamento']} "
        f"com R$ {top['faturamento']:.2f}."
    )

def descricao_vendedor(df):
    top = df.loc[df["faturamento"].idxmax()]
    return (
        f"O vendedor com maior faturamento foi {top['vendedor']} "
        f"com R$ {top['faturamento']:.2f}."
    )


# Função principal para gerar o relatório XLSX


def gerar_relatorio_xlsx(
    df_mes,
    df_cat,
    df_pag,
    df_vend,
    faturamento_total,
    pasta_saida="output"
):

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    caminho_arquivo = os.path.join(pasta_saida, "relatorio.xlsx")

    workbook = xlsxwriter.Workbook(caminho_arquivo)
    ws = workbook.add_worksheet("Gráficos")

    # Formatos
    titulo = workbook.add_format({"bold": True, "font_size": 14})
    subtitulo = workbook.add_format({"bold": True, "font_size": 12})
    normal = workbook.add_format({"font_size": 10})
    dinheiro = workbook.add_format({"num_format": "R$ #,##0.00"})

    linha = 0

    
    # Seção 1 — Faturamento Geral
    
    ws.write(linha, 0, "Faturamento Total", titulo)
    linha += 2
    ws.write(linha, 0, faturamento_total, dinheiro)
    linha += 2

    ws.write(linha, 0, "Faturamento por Mês", subtitulo)
    linha += 1

    # Inserir gráfico
    ws.insert_image(linha, 0, "output/faturamento_por_mes.png", {"x_scale": 0.7, "y_scale": 0.7})
    linha += 20

    # Descrição automática
    ws.write(linha, 0, descricao_faturamento_mes(df_mes), normal)
    linha += 3

   
    # Seção 2 — Categorias
   
    ws.write(linha, 0, "Faturamento por Categoria", subtitulo)
    linha += 2

    # Tabela
    ws.write_row(linha, 0, ["Categoria", "Faturamento"], titulo)
    linha += 1
    for _, row in df_cat.iterrows():
        ws.write(linha, 0, row["categoria"], normal)
        ws.write(linha, 1, row["faturamento"], dinheiro)
        linha += 1

    linha += 1
    ws.insert_image(linha, 0, "output/faturamento_por_categoria.png", {"x_scale": 0.7, "y_scale": 0.7})
    linha += 20

    ws.write(linha, 0, descricao_categoria(df_cat), normal)
    linha += 3

    
    # Seção 3 — Formas de Pagamento
    
    ws.write(linha, 0, "Faturamento por Forma de Pagamento", subtitulo)
    linha += 2

    ws.write_row(linha, 0, ["Forma de Pagamento", "Faturamento"], titulo)
    linha += 1
    for _, row in df_pag.iterrows():
        ws.write(linha, 0, row["forma_pagamento"], normal)
        ws.write(linha, 1, row["faturamento"], dinheiro)
        linha += 1

    linha += 1
    ws.insert_image(linha, 0, "output/faturamento_por_pagamento.png", {"x_scale": 0.7, "y_scale": 0.7})
    linha += 20

    ws.write(linha, 0, descricao_pagamento(df_pag), normal)
    linha += 3

   
    # Seção 4 — Vendedores
    
    ws.write(linha, 0, "Faturamento por Vendedor", subtitulo)
    linha += 2

    ws.write_row(linha, 0, ["Vendedor", "Faturamento"], titulo)
    linha += 1
    for _, row in df_vend.iterrows():
        ws.write(linha, 0, row["vendedor"], normal)
        ws.write(linha, 1, row["faturamento"], dinheiro)
        linha += 1

    linha += 1
    ws.insert_image(linha, 0, "output/faturamento_por_vendedor.png", {"x_scale": 0.7, "y_scale": 0.7})
    linha += 20

    ws.write(linha, 0, descricao_vendedor(df_vend), normal)

    workbook.close()

    return caminho_arquivo