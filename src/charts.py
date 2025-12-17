import matplotlib.pyplot as plt
import pandas as pd
import os

# ---------------------------------------------------------
# Configuração global de estilo
# ---------------------------------------------------------

plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["axes.edgecolor"] = "#B0BEC5"
plt.rcParams["axes.labelcolor"] = "#263238"
plt.rcParams["xtick.color"] = "#455A64"
plt.rcParams["ytick.color"] = "#455A64"
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 11
plt.rcParams["xtick.labelsize"] = 9
plt.rcParams["ytick.labelsize"] = 9


def garantir_pasta_saida(pasta: str):
    if not os.path.exists(pasta):
        os.makedirs(pasta)


def _add_bar_labels(ax):
    """Adiciona rótulos de valor no topo das barras."""
    for p in ax.patches:
        height = p.get_height()
        if pd.isna(height):
            continue
        ax.annotate(
            f"{height:,.0f}",
            (p.get_x() + p.get_width() / 2, height),
            ha="center",
            va="bottom",
            fontsize=8,
            color="#37474F",
            xytext=(0, 2),
            textcoords="offset points",
        )


# GRÁFICO: Faturamento por mês (linha)

def grafico_faturamento_por_mes(df_mes: pd.DataFrame, pasta_saida: str):
    garantir_pasta_saida(pasta_saida)

   
    df_mes = df_mes.dropna(subset=["mes", "faturamento"])

    fig, ax = plt.subplots(figsize=(9, 4))

    ax.plot(
        df_mes["mes"],
        df_mes["faturamento"],
        marker="o",
        color="#1E88E5",
        linewidth=2,
    )
    ax.set_title("Faturamento por Mês")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Faturamento (R$)")
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    plt.xticks(rotation=30)

    plt.tight_layout()
    caminho = os.path.join(pasta_saida, "faturamento_por_mes.png")
    plt.savefig(caminho, dpi=120)
    plt.close(fig)
    return caminho



# Função genérica para gráficos de barra


def _grafico_barra(df, coluna_x, coluna_y, titulo, rotulo_x, nome_arquivo, pasta_saida):
    garantir_pasta_saida(pasta_saida)

  
    df = df.dropna(subset=[coluna_x, coluna_y])

    fig, ax = plt.subplots(figsize=(9, 4))

    ax.bar(df[coluna_x], df[coluna_y], color="#42A5F5")
    ax.set_title(titulo)
    ax.set_xlabel(rotulo_x)
    ax.set_ylabel("Faturamento (R$)")
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    plt.xticks(rotation=30)

    _add_bar_labels(ax)

    plt.tight_layout()
    caminho = os.path.join(pasta_saida, nome_arquivo)
    plt.savefig(caminho, dpi=120)
    plt.close(fig)
    return caminho



# Gráficos específicos


def grafico_faturamento_por_categoria(df: pd.DataFrame, pasta_saida: str):
    return _grafico_barra(
        df,
        coluna_x="categoria",
        coluna_y="faturamento",
        titulo="Faturamento por Categoria",
        rotulo_x="Categoria",
        nome_arquivo="faturamento_por_categoria.png",
        pasta_saida=pasta_saida,
    )


def grafico_faturamento_por_pagamento(df: pd.DataFrame, pasta_saida: str):
    return _grafico_barra(
        df,
        coluna_x="forma_pagamento",
        coluna_y="faturamento",
        titulo="Faturamento por Forma de Pagamento",
        rotulo_x="Forma de Pagamento",
        nome_arquivo="faturamento_por_pagamento.png",
        pasta_saida=pasta_saida,
    )


def grafico_faturamento_por_vendedor(df: pd.DataFrame, pasta_saida: str):
    return _grafico_barra(
        df,
        coluna_x="vendedor",
        coluna_y="faturamento",
        titulo="Faturamento por Vendedor",
        rotulo_x="Vendedor",
        nome_arquivo="faturamento_por_vendedor.png",
        pasta_saida=pasta_saida,
    )