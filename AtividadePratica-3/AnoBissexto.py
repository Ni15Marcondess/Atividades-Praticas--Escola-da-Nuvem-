#Verificador de Ano Bissexto

#Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

#solicita o ano ao ussário
ano = int(input("Digite um ano: "))



#Verifica se é ano bissexto
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 ==0):
    print(f"✅ O ano {ano} é bissexto!")
else:
    print(f"❌ O ano {ano} não é bissexto!")


    #Explicando:
# Para ser um ano é bissexto precisa seguir essas regrinhas:
# 👉 1. Ele precisa ser divisível por 4
# 👉 2. Mas não pode ser divisível por 100 (a não ser que...)
# 👉 3. Ele seja também divisível por 400 

# Ou seja:
# - Se o ano for múltiplo de 4 E NÃO for múltiplo de 100 → é bissexto!
# - Mas, se o ano for múltiplo de 400 → também é bissexto, mesmo sendo múltiplo de 100

# Exemplos:
# 2024 → múltiplo de 4, não de 100 → ✅ bissexto
# 1900 → múltiplo de 4 e de 100, mas não de 400 → ❌ não bissexto
# 2000 → múltiplo de 4, de 100 e de 400 → ✅ bissexto