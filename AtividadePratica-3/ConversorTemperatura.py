# Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.


# Função para a conversão
def converter_temperatura(valor, origem, destino):
    if origem == "C":
        if destino == "F":
            return (valor * 9/5) + 32
        elif destino == "K":
            return valor + 273.15
    elif origem == "F":
        if destino == "C":
            return (valor - 32) * 5/9
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif origem == "K":
        if destino == "C":
            return valor - 273.15
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32
    return valor  # Se for mesma unidade


# Entrada de dados
valor = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()


# Verifica se as unidades são válidas
unidades_validas = ["C", "F", "K"]


if origem in unidades_validas and destino in unidades_validas:
    resultado = converter_temperatura(valor, origem, destino)
    print(f"\n🌡️ {valor}°{origem} é igual a {resultado:.2f}°{destino}")
else:
    print("❌ Unidades inválidas! Use apenas C, F ou K.")
