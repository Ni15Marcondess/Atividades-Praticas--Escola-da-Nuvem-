# Exercicio 3:
# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
# O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

import requests

# Solicita o CEP ao usuário
cep = input("Digite o seu CEP por favor, (somente números): ")

# Remove espaços e valida tamanho 
cep = cep.strip()

if len(cep) != 8 or not cep.isdigit():
    print("❌ CEP inválido! Certifique-se de digitar 8 números.")
else:
    # monta a url da api
    url = f"https://viacep.com.br/ws/{cep}/json/"

    #faz a requisição 
    resposta = requests.get(url)

    #Converte a resposta para JSON
    dados = resposta.json()

    #Verifica se o CEP foi encontrado 
    if "erro" in dados:
        print("❌ CEP não encontrado!")
    else: 
        # Exibe as informações do endereço 
        print("\nEndereço encontrado: ")
        print(f"📍 Logradouro: {dados['logradouro']}")
        print(f"🏡 Bairro: {dados['bairro']}")
        print(f"🗽 Cidade: {dados['localidade']}")
        print(f"🌟 Estado: {dados['uf']}")