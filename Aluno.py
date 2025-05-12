class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def exibir_info(self):
        print(f"Aluno: {self.nome} | Nota: {self.nota}")