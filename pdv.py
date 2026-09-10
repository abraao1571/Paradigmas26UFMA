opcao = ["1 - saldo", "2 - deposito", "3 - sacar", "4 - encerrar"]

while True:
    print("Escolha uma opção:")
    for item in opcao:
        print(item)
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        print("Saldo atual: R$ 1000,00")
    elif escolha == "2":
        valor = float(input("Digite o valor do depósito: R$ "))
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    elif escolha == "3":
        valor = float(input("Digite o valor do saque: R$ "))
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    elif escolha == "4":
        print("Encerrando o programa. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")