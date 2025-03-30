import requests
from bs4 import BeautifulSoup
import datetime as dt
import re
import pandas as pd

anos = ['{:02d}'.format(a) for a in range(6, 23)]
meses = ['{:02d}'.format(m) for m in range(1, 13)]

# Lista para armazenar os registros
dados_mare = []

regex_mare = re.compile(r'(\d{2}:\d{2})\s*(-?\d+\.\d)')

for ano in anos:
    for mes in meses:
        url = f'http://ondas.cptec.inpe.br/~rondas/mares/index.php?cod=40252&mes={mes}&ano={ano}'
        print(f"Acessando {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Erro ao acessar {url}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            tabua = soup.find("div", {"class": "tabua"})
            dados = tabua.find_all('li', {"class": "dados"})
        except Exception:
            continue

        for item in dados:
            texto = item.get_text(strip=True).replace(u'\xa0', '')
            if texto:
                dia = texto[0:2]
                try:
                    data = dt.datetime.strptime(dia + mes + ano, '%d%m%y').date()
                except:
                    continue

                matches = regex_mare.findall(texto)
                # Cria dicionário com até 4 pares hora-altura
                registro = {'Data': data}
                for i in range(4):
                    if i < len(matches):
                        hora, altura = matches[i]
                        registro[f'Hora_{i+1}'] = hora
                        registro[f'Altura_{i+1}'] = altura
                    else:
                        registro[f'Hora_{i+1}'] = ""
                        registro[f'Altura_{i+1}'] = ""
                dados_mare.append(registro)

# Criar DataFrame
df_final = pd.DataFrame(dados_mare)

# Salvar Excel
df_final.to_excel("tabela_mares_completa_limpinha.xlsx", index=False)
print("Arquivo salvo com sucesso: tabela_mares_completa_limpinha.xlsx")
