from dataclasses import dataclass, field


@dataclass(frozen=True)
class AvaliacaoDisciplina:
    """
    O @dataclass cria automaticamente o __init__ e outras funções úteis.
    O parâmetro frozen=True torna o objeto inteiro IMUTÁVEL após ser criado.
    """
    aluno: str
    disciplina: str
    notas: tuple[float, ...]

    @property
    def media(self) -> float:
        return sum(self.notas) / len(self.notas)

    @property
    def status(self) -> str:
        if self.media >= 7:
            return "aprovado"
        if self.media >= 5:
            return "reposição"
        return "reprovado"

    @property
    def classificacao(self) -> str:
        if self.media >= 9:
            return "muito boa"
        if self.media >= 7:
            return "boa"
        if self.media >= 5:
            return "regular"
        return "insuficiente"

    def __str__(self) -> str:
        """Define como o objeto será exibido quando usarmos print(avaliacao)."""
        return (
            f"aluno: {self.aluno}\n"
            f"disciplina: {self.disciplina}\n"
            f"media: {self.media:.2f}\n"
            f"classificacao: {self.classificacao}\n"
            f"situacao: {self.status}"
        )


class SistemaAcademico:
    def __init__(self):
        self.__historico: list[AvaliacaoDisciplina] = []

    def _ler_notas(self, quantidade: int) -> tuple[float, ...]:
        # List comprehension + conversão direta para tupla imutável
        return tuple(
            float(input(f"digite a nota {i + 1}: "))
            for i in range(quantidade)
        )

    def _ler_quantidade_notas(self) -> int:
        while True:
            quantidade = int(input("digite a quantidade de notas (2 a 10): "))
            if 2 <= quantidade <= 10:
                return quantidade
            print("valor inválido! digite entre 2 e 10.")

    def cadastrar_disciplina(self):
        aluno = input("digite o nome do aluno: ").strip()
        disciplina = input("digite o nome da disciplina: ").strip()
        quantidade = self._ler_quantidade_notas()
        notas = self._ler_notas(quantidade)

        avaliacao = AvaliacaoDisciplina(aluno, disciplina, notas)
        self.__historico.append(avaliacao)

        print("\n- resultado -")
        print(avaliacao)  # Chama o __str__ automaticamente!

    def consultar_historico(self):
        if not self.__historico:
            print("\nainda nao existem disciplinas cadastradas.")
            return

        print("\n- historico -")
        for avaliacao in self.__historico:
            print(f"\n{avaliacao}")

    def executar(self):
        opcoes = {
            "1": self.cadastrar_disciplina,
            "2": self.consultar_historico,
        }

        while True:
            print("\n- sistema academico -")
            print("1. cadastrar disciplina")
            print("2. consultar historico")
            print("3. sair")

            opcao = input("escolha uma opcao: ").strip()

            if opcao == "3":
                print("\nfim")
                break

            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                print("\ninvalido")


if __name__ == "__main__":
    SistemaAcademico().executar()
