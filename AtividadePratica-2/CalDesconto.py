# Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

# Informações do produto
nome_do_produto = "Camiseta"
preco = 50.00
porcentagem_desconto = 20 

# Cálculo do valor do desconto 
valor_desconto = (porcentagem_desconto / 100) * preco

#Cálculo do preço final 
preco_final = preco - valor_desconto

# Resultado 
print("Detalhes da Promoção!!!💰")
print(f"Produto: {nome_do_produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com o desconto: R$ {preco_final:.2f}")