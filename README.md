# 🌊 Coletor de Tábua de Marés - CPTEC/INPE

Este projeto realiza o web scraping das tábuas de maré do site do CPTEC/INPE, coletando os dados de **hora** e **altura da maré** para cada dia entre os anos de **2006 a 2022**, organizando as informações em um arquivo Excel limpo e pronto para análise.

## 📌 Funcionalidades

- 🔄 Coleta automática de dados mês a mês de 2006 a 2022.
- ⏰ Captura os horários e alturas de até 4 marés por dia.
- 🧹 Dados organizados em colunas: `Data`, `Hora_1`, `Altura_1`, ..., `Hora_4`, `Altura_4`.
- 📁 Gera arquivo Excel `.xlsx` com os dados prontos para uso.

## 🔧 Requisitos

Antes de rodar, instale os pacotes necessários com: `pip install pandas requests beautifulsoup4 openpyxl`

## ▶️ Como usar

Primeiro, clone este repositório executando:  

`git clone https://github.com/seu-usuario/coletor-mares.git`

Entre na pasta do projeto:  

`cd coletor-mares`

Em seguida, execute o script principal com:  

`python coletor_mares.py`

Após a execução, o arquivo `tabela_mares_completa_limpinha.xlsx` será gerado automaticamente na mesma pasta do script.

## 🗂 Estrutura do Excel

O Excel gerado terá as seguintes colunas:

| Data       | Hora_1 | Altura_1 | Hora_2 | Altura_2 | Hora_3 | Altura_3 | Hora_4 | Altura_4 |
|------------|--------|----------|--------|----------|--------|----------|--------|----------|
| 2018-03-10 | 03:51  | 0.7      | 09:38  | 1.0      | 16:23  | 0.6      | 23:13  | 1.0      |
| 2018-03-11 | 05:30  | 0.7      | 11:09  | 1.0      | 17:43  | 0.5      |        |          |

## 🌐 Fonte dos Dados

Os dados são obtidos diretamente do portal oficial de marés do [CPTEC/INPE](http://ondas.cptec.inpe.br/~rondas/mares/).


## Licença 

The [MIT License]() (MIT)

Copyright :copyright: - 2025
