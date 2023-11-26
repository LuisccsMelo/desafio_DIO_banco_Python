menu = '''
    [d] Depósitar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => '''

saldo = 0
extrato = ""
numero_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print('Digite o valor a ser depositado: ')
        valor = int(input('=> '))
        if valor <= 0:
            print('Operação não realizada, valor não é válido.')
        elif valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor:.2f}\n'
            print(f'Deposito de R$ {valor:.2f} realizado com sucesso')

    elif opcao == "s":
        print('Digite o valor que você quer sacar')
        valor = int(input('=> '))
        if valor <= 0:
            print('Operação não realizada, valor não é válido.')
        elif valor > 500:
            print('Operação não realizada. O valor de saque não pode ser maior que R$ 500,00')
        elif valor > 0 and valor < 500:
            if numero_saques == 0:
                print('Operação não realizada. Você já realizou 3 saques hoje.')
            elif saldo < valor:
                print('Operação não realizada. O valor de saldo não é suficiente.')
            else:
                saldo -= valor
                extrato += f'Saque de R$ {valor}\n'
                numero_saques -= 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso')

    elif opcao == "e":
        print('=' * 40)
        print('EXTRATO DA CONTA\n')
        print('Não houveram movimentações nesta conta' if not extrato else extrato)        
        print('  ')
        if numero_saques > 0:
            print(f'Ainda lhe resta {numero_saques} saques disponíveis')
        elif numero_saques == 1:
            print('Você só tem mais um saque disponível')
        else:
            print('Você não possui mais saques disponíveis')
        print(f'Saldo: R$ {saldo:.2f}')
        print('=' * 40)


    elif opcao == "q":
        break

    else:
        print('Opção inválida. Por favor escolha uma opção válida!')

