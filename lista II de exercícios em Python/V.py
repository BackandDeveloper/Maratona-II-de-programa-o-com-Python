#Atividade V:
# Função para converter dias, horas e minutos em segundos
def converter_para_segundos(dias, horas, minutos):
    return dias * 24 * 3600 + horas * 3600 + minutos * 60

# Entrada de dados
D1 = int(input("Digite o dia de partida (D1): "))
H1 = int(input("Digite a hora de partida (H1): "))
M1 = int(input("Digite os minutos de partida (M1): "))
D2 = int(input("Digite o dia de chegada (D2): "))
H2 = int(input("Digite a hora de chegada (H2): "))
M2 = int(input("Digite os minutos de chegada (M2): "))

# Cálculo do tempo de partida e chegada em segundos
tempo_partida = converter_para_segundos(D1, H1, M1)
tempo_chegada = converter_para_segundos(D2, H2, M2)

# Cálculo do tempo total da viagem em segundos
tempo_viagem = tempo_chegada - tempo_partida

# Saída do resultado
print(f"{tempo_viagem} segundos")
