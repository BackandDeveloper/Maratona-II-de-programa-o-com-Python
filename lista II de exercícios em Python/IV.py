#Atividade IV:
# Função para calcular a quantidade de grãos de trigo
def calcular_graos(posicao):
    return posicao**3

# Entrada de dados
posicao = int(input("Digite a posição do quadrado: "))

# Cálculo da quantidade de grãos de trigo
graos = calcular_graos(posicao)

# Cálculo da quantidade de kg de trigo (1 kg = 12.000 grãos)
kg_trigo = graos / 12000

# Saída do resultado
print(f"A quantidade de kg de trigo é: {int(kg_trigo)}")
