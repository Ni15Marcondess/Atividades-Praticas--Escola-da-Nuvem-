# Exercicio 2: Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
# O programa deve exibir o nome, email e país do usuário gerado.

import requests

print("✨ Gerador de Perfil Aleatório ✨")

# Faz a requisição na API
response = requests.get("https://randomuser.me/api/")

if response.status_code == 200:
    dados = response.json()

    # Extrai as informações necessárias 
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    # Resultado
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")

else:
    print("Ops! Não consegui pegar os dados do usuário. Tente novamente.")
