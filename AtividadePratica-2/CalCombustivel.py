# Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# Distância percorrida: 300 km
# Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

#dados da viagem
distancia = 300 # em km
combustivel = 25 # em litros 

#cálculo do consumo 
consumo = distancia / combustivel

#Resultados 
print("🚗 Relatório de Consumo de Combustível 🚗")
print(f"Distância percorrida: {distancia} Km")
print(f"Combustível gasto: {combustivel} Litros")
print(f"Consumo: {consumo:.2f} Km/l")