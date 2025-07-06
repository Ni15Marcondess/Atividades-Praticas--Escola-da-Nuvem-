# 3 - Crie um script em Python que leia um arquivo CSV e exiba os dados na tela.
#  O arquivo CSV deve conter informações de pessoas, com colunas:
# - Nome, Idade e Cidade.

import csv

# Nome do arquivo csv que será lido
nome_arquivo = 'pessoas.csv'

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)

        print("📜 Lista de Pessoas:")
        for i, linha in enumerate(leitor):
            if i == 0:
                print(f"\n{linha[0]:<15} {linha[1]:<10} {linha[2]:<15}")
                print("-" * 40)
            else:
                print(f"{linha[0]:<15} {linha[1]:<10} {linha[2]:<15}")

except FileNotFoundError:
    print(f"❌ Arquivo '{nome_arquivo}' não encontrado, Certifique-se de que ele esteja na mesma pasta do script.")