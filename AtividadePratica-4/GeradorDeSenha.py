# Exercicio 1: Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. ​

import random
import string

print("🔒 Gerador de Senha Aleatória 🔒")


#entrada
tamanho = int(input("Quantos caracteres você quer na sua senha?"))

#grupos equilibrados de caracteres
letras = string.ascii_letters # A-Z + a-z
numeros = string.digits   # 0-9
especiais = "!@#$%¨&*?"  # Mais bonitos e usuais

# Garante que: 50% seja letras, 30% seja números, 20% seja caracteres especiais 
qtd_letras = int(tamanho * 0.5)
qtd_numeros = int(tamanho * 0.3)
qtd_especiais = tamanho - qtd_letras - qtd_numeros

senha_lista = (
    random.choices(letras, k=qtd_letras) +
    random.choices(numeros, k=qtd_numeros) +
    random.choices(especiais, k=qtd_especiais)
)

random.shuffle(senha_lista)  # Vai misturar tudo forma aleatória

senha = ''.join(senha_lista)

#Exibe a senha gerada
print(f"Sua senha aleatória é: {senha}")
