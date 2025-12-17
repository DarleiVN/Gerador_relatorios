from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import Table, TableStyle
import os


# Descrições automáticas


def descricao_faturamento_mes(df):
    maior = df.loc[df["faturamento"].idxmax()]
    menor = df.loc[df["faturamento"].idxmin()]
    return (
        f"O mês com maior faturamento foi {maior['mes']} "
        f"com R$ {maior['faturamento']:.2f}. "
        f"O menor faturamento ocorreu em {menor['mes']}."
    )

def descricao_categoria(df):
    top = df.loc[df["faturamento"].idxmax()]
    return f"A categoria líder em faturamento foi {top['categoria']} com R$ {top['faturamento']:.2f}."

def descricao_pagamento(df):
    top = df.loc[df["faturamento"].idxmax()]
    return f"A forma de pagamento mais utilizada foi {top['forma_pagamento']} com R$ {top['faturamento']:.2f}."

def descricao_vendedor(df):
    top = df.loc[df["faturamento"].idxmax()]
    return f"O vendedor com maior faturamento foi {top['vendedor']} com R$ {top['faturamento']:.2f}."


# Função auxiliar para tabelas


def desenhar_tabela(pdf, df, x, y, largura=500):
    dados = [list(df.columns)] + df.values.tolist()

    tabela = Table(dados, colWidths=[largura / len(df.columns)] * len(df.columns))
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E88E5")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
    ]))

    tabela.wrapOn(pdf, x, y)
    tabela.drawOn(pdf, x, y)


# Função principal para gerar o PDF


def gerar_relatorio_pdf(
    df_mes,
    df_cat,
    df_pag,
    df_vend,
    faturamento_total,
    pasta_saida="output"
):

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    caminho_pdf = os.path.join(pasta_saida, "relatorio.pdf")
    pdf = canvas.Canvas(caminho_pdf, pagesize=A4)

    largura, altura = A4

    
    # CAPA
    

    pdf.setFillColor(colors.HexColor("#1E88E5"))
    pdf.rect(0, altura - 80, largura, 80, fill=1)

    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(2 * cm, altura - 50, "Relatório de Vendas")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(2 * cm, altura - 70, "Gerado automaticamente pelo sistema")

    pdf.showPage()

    # PÁGINA 1 — Faturamento Geral
   

    pdf.setFont("Helvetica-Bold", 18)
    pdf.setFillColor(colors.HexColor("#1E88E5"))
    pdf.drawString(2 * cm, altura - 50, "Faturamento Geral")

    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(colors.black)
    pdf.drawString(2 * cm, altura - 80, f"Faturamento Total: R$ {faturamento_total:.2f}")

    # Gráfico
    pdf.drawImage("output/faturamento_por_mes.png", 2 * cm, altura - 350, width=400, height=200)

    # Descrição para o gráfico
    pdf.setFont("Helvetica", 10)
    pdf.drawString(2 * cm, altura - 370, descricao_faturamento_mes(df_mes))

    pdf.showPage()

   
    # PÁGINA 2 — Categorias
    

    pdf.setFont("Helvetica-Bold", 18)
    pdf.setFillColor(colors.HexColor("#1E88E5"))
    pdf.drawString(2 * cm, altura - 50, "Faturamento por Categoria")

    desenhar_tabela(pdf, df_cat, 2 * cm, altura - 300)

    pdf.drawImage("output/faturamento_por_categoria.png", 2 * cm, altura - 520, width=400, height=200)

    pdf.setFont("Helvetica", 10)
    pdf.drawString(2 * cm, altura - 540, descricao_categoria(df_cat))

    pdf.showPage()

    # PÁGINA 3 — Formas de Pagamento
   
    pdf.setFont("Helvetica-Bold", 18)
    pdf.setFillColor(colors.HexColor("#1E88E5"))
    pdf.drawString(2 * cm, altura - 50, "Faturamento por Forma de Pagamento")

    desenhar_tabela(pdf, df_pag, 2 * cm, altura - 300)

    pdf.drawImage("output/faturamento_por_pagamento.png", 2 * cm, altura - 520, width=400, height=200)

    pdf.setFont("Helvetica", 10)
    pdf.drawString(2 * cm, altura - 540, descricao_pagamento(df_pag))

    pdf.showPage()

    
    # PÁGINA 4 — Vendedores
   

    pdf.setFont("Helvetica-Bold", 18)
    pdf.setFillColor(colors.HexColor("#1E88E5"))
    pdf.drawString(2 * cm, altura - 50, "Faturamento por Vendedor")

    desenhar_tabela(pdf, df_vend, 2 * cm, altura - 300)

    pdf.drawImage("output/faturamento_por_vendedor.png", 2 * cm, altura - 520, width=400, height=200)

    pdf.setFont("Helvetica", 10)
    pdf.drawString(2 * cm, altura - 540, descricao_vendedor(df_vend))

    pdf.showPage()

   
    # FINALIZAÇÃO
    # ---------------------------------------------------------

    pdf.save()
    return caminho_pdf