# Exercicio 2: Crie uma função que calcule a idade de uma pessoa em dias, baseado no ano de nascimento.

from datetime import datetime, date 

def idade_em_dias_completa(ano, mes, dia):
    data_nascimento = date(ano, mes, dia)
    hoje = date.today()
    diferenca = hoje - data_nascimento
    dias = diferenca.days

    print(f"📆 Data de nasciemnto: {data_nascimento.strftime('%d/%m/%Y')}")
    print(f"📍 Data atual: {hoje.strftime('%d/%m/%Y')}")
    print(f"🎉 Você tem {dias} dias de vida! ✨")

# exemplo de uso 
print("👶 Digite sua data de nascimento:")
ano = int(input("Ano: "))
mes = int(input("Mês (1-12): "))
dia = int(input("Dia (1-31): "))

idade_em_dias_completa(ano, mes, dia)