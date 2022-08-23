from criar_conta import ContaBanco


print(50 * '=')
titulo = 'BANCÃO DO BRUNÃO'
print(f'{titulo:^50}')
print(50 * '=', '\n')

nome = input('Nome do titular: ').title().strip()

while True:
    tipo_de_conta = input('Tipo da conta\n1: Corrente (Bônus de saldo inicial: R$50)\n2: Poupança (Bônus de saldo inicial: R$150)\nOpção: ').strip()
    
    match tipo_de_conta:
        case '1':
            tipo_de_conta = 'cc'
            break
        case '2':
            tipo_de_conta = 'cp'
            break
        case _:
            print(50*'-')
            print('\033[31mInforme um tipo válido de conta\033[m')
            print(50*'-')

conta = ContaBanco()

conta.abrir_conta(nome, tipo_de_conta)
print('\033[32mConta aberta com sucesso!\033[m')

while True:
    print(50 * '=')
    print('Escolha uma opção\n')
    print(' 1: Sacar \n 2: Depositar \n 3: Encerrar conta \n ')
    
    opcao = input('Opção: ').strip()

    match opcao:
        case '1':
            print(50 * '-')

            while True:
                saque = input('Quantidade do saque: ')

                if(saque.isnumeric):
                    saque = float(saque)
                    
                else:
                    print('\033[33mSaque mínimo de R$1\033[m')

                    
        case '2':
            pass

        case '3':
            pass

        case _:
            print(50 * '-')
            print('\033[31mEscolha uma válida\033[m')
            print(50 * '-')
