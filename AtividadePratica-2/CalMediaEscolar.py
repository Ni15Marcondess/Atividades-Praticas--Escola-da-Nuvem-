# Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# Nota 1: 7.5
# Nota 2: 8.0
# Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.


#Notas dos alunos
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

#Cálculo da média
media = (nota1 + nota2 + nota3) /3

#Resultados 
print("📕 Boletim Escolar 📕")
print(f"Primeira nota: {nota1:.2F}")
print(f"Segunda nota: {nota2:.2f}")
print(f"Terceira nota: {nota3:.2f}")
print(f"Média Final: {media:.2f}")