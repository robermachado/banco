# -*- coding: utf-8 -*-

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Saldo insuficiente.')

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.saldo}')


def main():
    print("Bem-vindo ao sistema bancário!")

    nome_titular = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome_titular)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
        elif opcao == '2':
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_saque)
        elif opcao == '3':
            conta.exibir_saldo()
        elif opcao == '4':
            print("Obrigado por utilizar o sistema bancário!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
