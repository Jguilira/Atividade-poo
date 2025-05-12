class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def exibir_info(self):
        print(f"Aluno: {self.nome} | Nota: {self.nota}")

lista_alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    nota = float(input(f"Digite a nota de {nome}: "))
    
    aluno = Aluno(nome, nota)
    lista_alunos.append(aluno)

print("\nLista de Alunos Cadastrados:")
for aluno in lista_alunos:
    aluno.exibir_info()