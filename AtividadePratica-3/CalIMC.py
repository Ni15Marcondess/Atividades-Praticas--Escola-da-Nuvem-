# Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

#Solicita os dados do usuário
peso = float(input("Digite seu peso em Kg, por favor: "))
altura = float(input("Digite sua aultura, por favor: "))

#calcula o IMC
imc = peso / (altura * altura)

#Resultados 
if imc < 18.5:
    classificacao = "Tá podendo comer mais, abaixo do peso normal"
elif imc < 25:
    classificacao = "Parabéns! Seu peso está certinho, peso ideal!"
elif imc < 30: 
    classificacao = "Vamos dando uma segurada e prestando atenção na saúde, sobrepeso"
else:
    classificacao = "Procure uma atividade física urgente!!! Obeso"

#resultado
print(f"\n 📈 Seu IMC é: {imc:.2f}")
print(f"Calssificação: {classificacao}")