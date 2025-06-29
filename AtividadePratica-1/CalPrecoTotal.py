#Calculadora de Preço Total
# Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

#Informações
nome_produto = "Cadeira Infantil"
preco = 12.40
quantidade = 3

#Cálculo
preco_total = preco * quantidade

#Resultado
print("🛒 Detalhes da sua compra: ")
print("Produto: ", nome_produto)
print("Preço unitário: R$", preco)
print("Quantidade: ", quantidade)
print("Preço total: R$", round(preco_total,2))