# Crie um programa que permita a um professor registrar as notas de uma turma.
# O programa deve continuar solicitando notas até que o professor digite 'fim'.
# Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando.
# No final, deve exibir a média da turma.



def registrar_notas():
    print("🎓 Registro de Notas da Turma 🎓")
    print("Digite as notas dos alunos (de 0 a 10).")
    print("Digite 'fim' para encerrar e calcular a média. \n")

    notas = []

    while True:
        entrada = input("Digite a nota do aluno: ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"✅ Nota {nota} registrada co sucesso!")
            else:
                print("⚠ Digite uma nota válida de um valor entre 0 e 10!")
        except ValueError:
            print("❌ Entrada inválida! Digite uma nota ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\n 📊 A média da turma é: {media:.2f}")
    else: 
        print("\nNenhuma nota válida foi registrada.")

# executa o programa 
registrar_notas()