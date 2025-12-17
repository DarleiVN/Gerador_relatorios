<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="180" alt="Python Logo">
</p>

<h1 align="center" style="color:#ffffff;">Gerador de Relatórios de Vendas</h1>

<p align="center" style="color:#cccccc;">
  Automação completa de relatórios em PDF e Excel, gráficos profissionais e análise de vendas usando Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-2ecc71?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Relatórios-PDF%20%7C%20XLSX-f39c12?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Licença-MIT-9b59b6?style=for-the-badge" />
</p>

---

## 📌 Sobre o Projeto

Este projeto automatiza a geração de relatórios de vendas a partir de uma planilha Excel.  
Ele processa os dados, salva em um banco SQLite, calcula métricas, gera gráficos e exporta relatórios em **PDF** e **Excel (XLSX)**.

Ideal para análises rápidas, dashboards offline e automação de relatórios corporativos.

---

## 🚀 Funcionalidades

- 📥 Leitura automática da planilha `vendas.xlsx`
- 🧹 Limpeza e padronização dos dados
- 📊 Cálculo de métricas:
  - Faturamento total
  - Faturamento por mês
  - Faturamento por categoria
  - Faturamento por forma de pagamento
  - Faturamento por vendedor
- 📈 Geração de gráficos profissionais (PNG)
- 📄 Exportação de relatórios:
  - PDF
  - Excel (XLSX) com múltiplas abas
- 🗄 Banco de dados SQLite para persistência

---

## 🗂 Estrutura do Projeto
Gerador_relatorios/ │
 ├── data/ │   
 ├── vendas.xlsx │  
  └── database/ │    
     └── vendas.db │ 
 ├── output/ │   
 ├── charts/ │   
 ├── relatorio.pdf │  
  └── relatorio.xlsx │ 
 ├── src/ │  
 ├── main.py │   
 ├── excel_reader.py │   
 ├── db_loader.py │   
 ├── metrics.py │  
 ├── charts.py │  
 ├── pdf_generator.py │  
  └── xlsx_generator.py │ 
└── README.md


---

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Pandas
- Matplotlib
- SQLite3
- OpenPyXL
- ReportLab

---

```md
## 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com//gerador-relatorios.git
cd gerador-relatorios
▶ Como Executar
Na raiz do projeto:
python src/main.py

O programa irá:
- Ler a planilha data/vendas.xlsx
- Criar/atualizar o banco vendas.db
- Gerar gráficos em output/charts/
- Criar:
- output/relatorio.pdf
- output/relatorio.xlsx
```

Observações Importantes
- Se alterar a estrutura da planilha, apague o banco vendas.db para evitar inconsistências.
- A primeira linha da planilha deve conter os nomes das colunas.
- Linhas vazias são "é para ser" automaticamente removidas.
```
🤝 Contribuições
Contribuições são bem-vindas.
Sinta-se à vontade para abrir issues e enviar pull requests.(●'◡'●)
 
```