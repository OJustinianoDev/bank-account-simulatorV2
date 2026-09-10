from contabancaria import Conta
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=int(os.getenv("DB_PORT"))
)

cursor = conexao.cursor()
cursor.execute("USE simuladorv2;")

contas = {}

def menu():
    print("\n--- Simulador de Conta Bancaria V2 ---")
    print("[ 1 ]  Criar conta")
    print("[ 2 ]  Depositar")
    print("[ 3 ]  Sacar")
    print("[ 4 ]  Ver saldo")
    print("[ 5 ]  Ver extrato")
    print("[ 6 ]  Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do completo titular: ")
        conta = Conta(cursor, conexao, nome, 0)
        conta.criar_no_banco()
        contas[conta.id] = conta
        print(f"Conta criada com sucesso! ID: {conta.id}")

    elif opcao == "2":
        id_conta = int(input("ID da conta: "))
        valor = float(input("Valor do depósito: "))
        if id_conta in contas:
            contas[id_conta].depositar(valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "3":
        id_conta = int(input("ID da conta: "))
        valor = float(input("Valor do saque: "))
        if id_conta in contas:
            contas[id_conta].sacar(valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        id_conta = int(input("ID da conta: "))
        if id_conta in contas:
            print("Saldo:", contas[id_conta].consultar_saldo_banco())
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        id_conta = int(input("ID da conta: "))
        if id_conta in contas:
            for transacao in contas[id_conta].extrato():
                print(transacao)
        else:
            print("Conta não encontrada.")

    elif opcao == "6":
        print("Encerrando...")
        cursor.close()
        conexao.close()
        break

    else:
        print("Opção inválida.")