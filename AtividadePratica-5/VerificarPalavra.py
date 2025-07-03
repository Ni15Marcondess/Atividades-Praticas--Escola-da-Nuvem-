# Exercicio 3: Crie uma função que verifique se uma palavra ou frase é um palindromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação).
# Se o resultado é True, responda "Sim", se o resultado for False, responda "Não".

import unicodedata
import string

def eh_palindromo(texto):
    # Remove  acentos
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')

    # Remove espaços, pontuações e coloca tudo em minúsculas
    texto_limpo = ''.join(
        char.lower() for char in texto if char.isalnum()
    )

    # Verifica se é igual ao reverso 
    if texto_limpo == texto_limpo[::-1]:
        print("Sim 😀 é um palíndromo!")
    else:
        print("Não 😥 não é um palíndromo.")

# exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
eh_palindromo(frase)