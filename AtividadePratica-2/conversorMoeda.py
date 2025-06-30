#Conversor de Moeda
#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.20
# Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

#Valor em reais 
valor_reais = 100.00

#Taxas de conversão
taxa_dolar = 5.20
taxa_euro = 6.15

#Conversão
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

#Exibindo os resultados
print("💰 Conversor de Moedas 🌎")
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Em Dólares: US$ {valor_dolar:.2f}")
print(f"Em Euros: € {valor_euro:.2f}")