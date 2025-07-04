# 3 - Crie um programa que verifique se uma senha é forte. 
# Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.
# O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

def verificar_senha():
    print("✨ Verificador de senha forte ✨")
    print("A senha deve ter pelo menos 8 caracteres e conter pelo menos um número! ")
    print("Digite 'sair' se quiser encerrar. \n")

    while True:
        senha = input ("Digite sua senha: ")

        if senha.lower() == 'sair':
            print("Você escolheu sair. Até logo!")
            break

        if len(senha) < 8: 
            print("❌ A sua senha deve ter pelo menos 8 caracteres!")
            continue

        if not any(char.isdigit() for char in senha):
            print("❌ A senha precisa ter pelo menos um número!")
            continue

        print("✅✨ Senha forte! Arrasou!🔒")
        break

# executa a função 
verificar_senha()