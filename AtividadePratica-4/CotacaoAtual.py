# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização.
# Utilize a API da AwesomeAPI para obter os dados de cotação.​

import requests

#Solicita a moeda desejada 
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

#Monta a URL da API
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    dados =  resposta.json()

    #Verifica se a resposta tem moeda 
    chave = f"{moeda}BRL"
    if chave in dados: 
        cotacao = dados[chave]

        print(f"\n 📊 Cotação atual de {moeda} para BRL: ")
        print(f" 💰 Valor atual: R$ {float(cotacao['bid']):.2f}")
        print(f"📈 Valor máximo do dia: R$ {float(cotacao['high']):.2f}")
        print(f"📉 Valor mínimo do dia: R$ {float(cotacao['low']):.2f}")
        print(f"📆 Data da última atualização: {cotacao['create_date']}")
    else:
        print("❌ Moeda não encontrada! Verifique o código e tente novamente.")

except Exception as e:
    print("⚠ Ocorreu um erro ao buscar a cotação:", e)