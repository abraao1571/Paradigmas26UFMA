def media(qntd, notas):
    soma = 0
    for i in range(qntd):
        soma += notas[i]
    media = soma / qntd
    return media


def classificacao(media):
    if media >= 9.5:
        return "A"
    elif media >= 8 and media < 9.5:
        return "B"
    elif media >= 7 and media < 8:
        return "C"
    elif media >= 6 and media < 7:
        return "D"
    else:
        return "E"


def aproveitamento(classificacao):
    if classificacao in ("A", "B", "C"):
        print("Aproveitamento: Aprovado")
    else:
        print("Aproveitamento: Reprovado")


def main():
    qntd = int(input("Digite a quantidade de notas: "))
    notas = []
    for i in range(qntd):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

    media_final = media(qntd, notas)
    print(f"Média: {media_final:.2f}")

    classificacao_final = classificacao(media_final)
    print(f"Classificação: {classificacao_final}")
    aproveitamento(classificacao_final)


if __name__ == "__main__":
    main()

