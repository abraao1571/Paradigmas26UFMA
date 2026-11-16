class AvaliacaoDisciplina:
    "Representa o desempenho de um aluno em uma disciplina específica."

    def __init__(self, aluno: str, disciplina: str, notas: list[float]):
        self.aluno = aluno
        self.disciplina = disciplina
        # Encapsulamento: armazena as notas como tupla privada para manter a imutabilidade
        self.__notas = tuple(notas)

    @property
    def notas(self) -> tuple[float, ...]:
        return self.__notas

    def calcular_media(self) -> float:
        return sum(self.__notas) / len(self.__notas)

    def verificar_status(self) -> str:
        media = self.calcular_media()
        if media >= 7:
            return "aprovado"
        elif media >= 5:
            return "reposição"
        return "reprovado"

    def gerar_classificacao(self) -> str:
        media = self.calcular_media()
        if media >= 9:
            return "muito boa"
        elif media >= 7:
            return "boa"
        elif media >= 5:
            return "regular"
        return "insuficiente"

    def exibir_resumo(self):
        "Método responsável por formatar e exibir os dados do próprio objeto."
        print(f"aluno: {self.aluno}")
        print(f"disciplina: {self.disciplina}")
        print(f"media: {round(self.calcular_media(), 2)}")
        print(f"classificacao: {self.gerar_classificacao()}")
        print(f"situacao: {self.verificar_status()}")


class SistemaAcademico:
    "Gerencia o histórico de avaliações e o fluxo do menu."

    def __init__(self):
        # Encapsulamento: o histórico pertence ao sistema, não fica solto no escopo global
        self.__historico: list[AvaliacaoDisciplina] = []

    def _ler_notas(self, quantidade: int) -> list[float]:
        notas = []
        for i in range(quantidade):
            nota = float(input(f"digite a nota {i + 1}: "))
            notas.append(nota)
        return notas

    def cadastrar_disciplina(self):
        aluno = input("digite o nome do aluno: ")
        disciplina = input("digite o nome da disciplina: ")
        quantidade = int(input("digite a quantidade de notas: "))

        while quantidade < 2 or quantidade > 10:
            print("digite entre 2 a 10")
            quantidade = int(input("digite novamente: "))

        notas = self._ler_notas(quantidade)
        
        # Criação do objeto (Instanciação)
        avaliacao = AvaliacaoDisciplina(aluno, disciplina, notas)
        self.__historico.append(avaliacao)

        print("\n- resultado -")
        avaliacao.exibir_resumo()

    def consultar_historico(self):
        if not self.__historico:
            print("\nainda nao existem disciplinas cadastradas.")
            return

        print("\n- historico -")
        for avaliacao in self.__historico:
            print()
            avaliacao.exibir_resumo()

    def executar(self):
        opcao = 0
        while opcao != 3:
            print("\n- sistema academico -")
            print("1. cadastrar disciplina")
            print("2. consultar historico")
            print("3. sair")

            opcao = int(input("escolha uma opcao: "))

            if opcao == 1:
                self.cadastrar_disciplina()
            elif opcao == 2:
                self.consultar_historico()
            elif opcao == 3:
                print("\nfim")
            else:
                print("\ninvalido")


if __name__ == "__main__":
    sistema = SistemaAcademico()
    sistema.executar()