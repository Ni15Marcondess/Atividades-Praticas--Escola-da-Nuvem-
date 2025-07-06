# 1 - Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. 
# Calcule a média e o desvio padrão do tempo de execução constantes.

# O código vai ler cada linha do txt, e procurar por números que tenham o final com "s"
# ele vai guardar todos esses tempos e calcular a média e o desvio padrão desses tempos 

import re 
import os
from statistics import mean, stdev

# Caminho para o arquivo na mesma pasta do script
caminho = os.path.join(os.path.dirname(__file__), 'logTreinamento.txt')

# Abre o arquivo de log
with open(caminho, 'r') as arquivo:
    linhas = arquivo.readlines()

tempos = []

# Extrai os tempos de execução 
for linha in linhas:
    resultado = re.search(r'(\d+\.?\d*)s', linha)
    if resultado:
        tempo = float(resultado.group(1))
        tempos.append(tempo)


# Calcula média e desvio padrão 
if tempos: 
    media = mean(tempos)
    desvio = stdev(tempos)
    print(f"Média dos tempos: {media:.2f}s")
    print(f"Desvio padrão: {desvio:.2f}s")
else:
    print("Nenhum tempo de execução encontrado.")