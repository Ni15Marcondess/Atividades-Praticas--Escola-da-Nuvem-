# Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias: 

# Criança (0-12 anos), 
# Adolescente (13-17 anos), 
# Adulto (18-59 anos) ou 
# Idoso (60 anos ou mais).

#Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

#Classificação por faixa etária
if idade >= 0 and idade <= 12:
    classificacao = "Muito fofo, uma Criança!"
elif idade >= 13 and idade <= 17:
    classificacao = "Vixe, tá na parte chata, Adolescente!"
elif idade >= 18 and idade <= 59:
    classificacao = "Agora a vida é sobre contas pra pagar, Adulto!"
elif idade >= 60:
    classificacao = "Onde se tem tempo, dinheiro, mas a dor nas costas não deixa fazer o mesmo de antes, Idoso!"
else:
    classificacao = "Insira uma idade válida!"

#Exibe o resultado 
print(f"Você é classificado como: {classificacao}")