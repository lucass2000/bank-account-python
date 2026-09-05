from src.account import Account


def read_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Digite um valor numérico maior que zero.")


def main():
    checking = Account("Conta Corrente", 1000)
    savings = Account("Conta Poupança", 500)

    while True:
        print("\n=== Sistema de Contas Bancárias ===")
        print(f"1 - Ver saldos")
        print("2 - Depositar na conta corrente")
        print("3 - Sacar da conta corrente")
        print("4 - Transferir da corrente para a poupança")
        print("0 - Sair")

        option = input("Escolha uma opção: ").strip()

        try:
            if option == "1":
                print(f"Corrente: R$ {checking.balance:.2f}")
                print(f"Poupança: R$ {savings.balance:.2f}")

            elif option == "2":
                checking.deposit(read_positive_float("Valor do depósito: R$ "))

            elif option == "3":
                checking.withdraw(read_positive_float("Valor do saque: R$ "))

            elif option == "4":
                checking.transfer(
                    savings,
                    read_positive_float("Valor da transferência: R$ "),
                )

            elif option == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")

        except (ValueError, TypeError) as error:
            print(f"Erro: {error}")


if __name__ == "__main__":
    main()
