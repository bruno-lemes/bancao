#pylint: disable=missing-module-docstring
from tkinter.tix import Tree
from nucleo_sistema.conta import ContaBanco


print(50 * '=')
TITULO = 'BANCÃO DO BRUNÃO'
print(f'{TITULO:^50}')
print(50 * '=', '\n')

nome = input('Nome do titular: ').title().strip()

while True:
    tipo_da_conta = input('Tipo da conta\n1: Corrente (Bônus de saldo inicial: R$50)\n2:\
 Poupança (Bônus de saldo inicial: R$150)\nOpção: ').strip()
    match tipo_da_conta:
        case '1':
            TIPO_DA_CONTA = 'cc'
            break
        case '2':
            TIPO_DA_CONTA = 'cp'
            break
        case _:
            print(50*'-')
            print('\033[31mInforme um tipo válido de conta\033[m')
            print(50*'-')

conta = ContaBanco()

conta.abrir_conta(nome, TIPO_DA_CONTA)

print('\033[32mConta aberta com sucesso!\033[m')

while True:
    print(50 * '=')
    print('Escolha uma opção\n')
    print(' 1: Sacar \n 2: Depositar \n 3: Encerrar conta \n ')
    opcao = input('Opção: ').strip()
    match opcao:
        case '1':
            while True:
                try:
                    saque = float(input('Valor do saque: '))
                except ValueError:
                    print('Informe um valor válido')
                else:
                    if conta.saldo_da_conta >= saque > 0:
                        conta.sacar(saque)
                        print('Saque realizado com sucesso.')
                        break
                    print('Informe um valor válido')
        case '2':
            break
        case '3':
            break
        case _:
            print('\033[31m Informe uma opção válida \033[m')
