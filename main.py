import sqlite3

con = sqlite3.connect('bancodedados.db')
cursor = con.cursor()

print('='*100)
print()
print('{:^100}'.format('BANCO NEXXEES\n'))
print('='*100)
print()

nome= input('Digite o nome do titular: \n')
print()
conta =float(input(f"Digite os números da sua conta, {nome}: \n"))
print()
saldo = float(input(f"Digite o seu saldo atual: \n"))
print()

cursor.execute(f"INSERT INTO conta VALUES('{nome}', '{conta}', '{saldo}')")
con.commit()

while True:

    print("Qual das operações você deseja utilzar? Escolha uma das duas abaixo:\n 1 - Deposito    \n 2 - Retirada  \n 3-  Informações da conta.  \n 4-  Extrato \n 5 - Sair " )
    print('______________________________________')
    operacao = int(input())

    if operacao==1:
    
        deposito = float(input("Quanto deseja depositar? "))

        saldo+=deposito

        print(f"Seu saldo atual é de: R${saldo:.2f}\n")

    elif operacao==2:

        retirada = float(input("Quanto deseja sacar? "))  

        saldo-=retirada

        if saldo >=0:

            print(f"Seu saldo atual é de: R$ {saldo:.2f}\n")

        else:

            print("Não há saldo suficiente!")

            print(f"Seu saldo atual seria de: R$ {saldo:.2f}\n")

    elif operacao==3:

        print(f"Sua conta é a: {conta}")

        print(f"Seu saldo atual é de: R$ {saldo:.2f}\n")
        
    elif operacao==4:
        print(f"Seu extrato é de: \n Saldo: R${saldo} \n Depósito: R${deposito} \n Saque: R${retirada}")    
        print()

    elif operacao==5:

        break

    else:

        print("Digite uma operação válida\n")
        
