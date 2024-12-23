# Questão II:
C = float(input("Digite o capital inicial (C): "))
i = float(input("Digite a taxa de juros mensal (i) em %: ")) / 100
t = int(input("Digite o número de meses (t): "))

# Cálculo do montante final
M = C * (1 + i)**t

# Saída do resultado
print(f"Montante final após {t} meses: R$ {M:.2f}")