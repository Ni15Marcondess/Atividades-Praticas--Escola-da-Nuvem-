# Exercicio 1: Crie uma  função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcula o valor da gorjeta baseada no total a conta e na porcentagem desejada.

def calcular_gorjeta(valor_conta, porcentagem):
    gorjeta = valor_conta * (porcentagem / 100)
    total = valor_conta + gorjeta

    print(f" Valor da conta: R$ {valor_conta:.2f}")
    print(f" Porcentagem da gorjeta: {porcentagem}%")
    print(f" Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f" Total a pagar: R$ {total:.2f}")

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
calcular_gorjeta(valor, porcentagem)