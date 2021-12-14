import re
import requests

site = input('Digite o site: ')

requisicao = requests.get(site)

padrao = re.findall(r'[\w\.-]+@[\w-]+[\w\.-]+', requisicao.text)

if padrao:
    print(padrao)
else:
    print('E-mail não encontrado')


