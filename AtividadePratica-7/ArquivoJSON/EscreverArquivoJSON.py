#4 -  Crie um script em Python que leia e escreva dados em um arquivo JSON.
#  O arquivo JSON deve conter informações de uma pessoa, com campos:
# - Nome, Idade e Cidade.

import json

# Dicionário com os dados da pessoa
pessoa = {
    "Nome": "Fernanda",
    "Idade": 25,
    "Cidade": "São Paulo"
}

# Nome do arquivo JSON  
arquivo_json = "pessoa.json"

# Escrevendo os dados no arquivo JSON  
with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
    print("✅ Dados salvos com sucesso em JSON!")

# Lendo os dados do arquivo JSON
with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    dados_lidos = json.load(arquivo)
    print("\n Dados lidos do arquivo JSON:")
    print(f"Nome: {dados_lidos['Nome']}")
    print(f"Idade: {dados_lidos['Idade']}")
    print(f"Cidade: {dados_lidos['Cidade']}")
