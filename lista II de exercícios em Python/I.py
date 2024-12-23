# Questão I:
produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Cálculo do valor total
valor_total = produto1 + produto2 + produto3

# Cálculo do valor do desconto
desconto = (percentual_desconto / 100) * valor_total

# Cálculo do valor com desconto
valor_com_desconto = valor_total - desconto

# Saída dos resultados
print(f"Valor total: R$ {valor_total:.2f}")
print(f"Desconto de {percentual_desconto}%: R$ {desconto:.2f}")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")