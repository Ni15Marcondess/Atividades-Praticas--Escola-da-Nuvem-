# 2 - Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. 
# Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar. 
# No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.

def verificar_par_ou_impar():
    pares = 0
    impares = 0

    print("Digite núemros inteiros e eu direi se são pares ou ímpares! ✨")
    print("Digite 'fim' quando quiser encerrar\n")

    while True: 
        entrada = input("Digite um número (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é um número **par**! 💙")
                pares += 1
            else:
                print(f"{numero} é um número **ímpar**! ❤")
                impares += 1
        except ValueError:
            print("Erro: Por favor, digite apenas um núemros inteiros ou 'fim'! ")

    
    print("\n ✨ Resultado final ✨")
    print(f"Núemros pares digitando: {pares}")
    print(f"Números ímpares digitados: {impares}")
    print("Obrigada por brincar com os números comigo! ❤")

# Executa a função
verificar_par_ou_impar()