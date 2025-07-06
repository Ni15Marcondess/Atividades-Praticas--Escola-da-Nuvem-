# 2 - Crie um script em Python que escreva dados em um arquivo CSV.
#  O arquivo CSV deve conter informações de pessoas, com colunas:
# - Nome, Idade e Cidade.

import csv 

# Nome do arquivo Csv que será criado
nome_arquivo = 'pessoas.csv'

# Dados que queremos salvar
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Ana', 25, 'São Paulo'],
    ['Bruno', 30, 'Rio de Janeiro'],
    ['Carla', 22, 'Belo Horizonte'],
    ['Diego', 28, 'Porto Alegre']
]

# Escrevendo no arquivo CSV 
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(dados)

print(f"Arquivo '{nome_arquivo}' criado com sucesso! ✨")