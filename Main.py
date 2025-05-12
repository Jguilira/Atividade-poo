from Aluno import Aluno

lista_alunos = []
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    nota = float(input(f"Digite a nota de {nome}: "))
    aluno = Aluno(nome, nota)
    lista_alunos.append(aluno)


print("\n--- Lista de Alunos Cadastrados ---")
for aluno in lista_alunos:
    aluno.exibir_informacoes()