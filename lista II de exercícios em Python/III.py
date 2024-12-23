# Questão III:
total_alunos = int(input("Digite o número total de alunos: "))
alunos_por_equipe = int(input("Digite o número de alunos por equipe: "))

# Cálculo do número de equipes formadas e alunos sem equipe
numero_equipes = total_alunos // alunos_por_equipe
alunos_sem_equipe = total_alunos % alunos_por_equipe

# Saída dos resultados
print(f"Número de equipes formadas: {numero_equipes}")
print(f"Alunos sem equipe: {alunos_sem_equipe}")
