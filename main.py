#pylint: disable=missing-module-docstring

from nucleo_sistema.conta import ContaBanco

#Controla o ativamento ou desligamento do sistema
ENCERRAR_SISTEMA = False

# Estrutura do cabeçalho
print(50 * '=')
TITULO = 'BANCÃO DO BRUNÃO'
print(f'{TITULO:^50}')
print(50 * '=')

# Nome da pessoa a ser cadastrada
nome = input('\nNome do titular: ').title().strip()

# Validação do tipo de conta
while True:
    tipo_da_conta = input('\nTipo da conta:\n\n1: Corrente Bônus de saldo inicial:\
 R$50)\n2: Poupança (Bônus de saldo inicial: R$150)\n\nOpção: ').strip()
    match tipo_da_conta:
        case '1':
            TIPO_DA_CONTA = 'cc'
            break
        case '2':
            TIPO_DA_CONTA = 'cp'
            break
        case _:
            print('\n \033[31mInforme um tipo válido de conta \033[m')

# Criação da conta
conta = ContaBanco()

# Ativamento da conta
conta.abrir_conta(nome, TIPO_DA_CONTA)
print('\n \033[32m Conta aberta com sucesso! \033[m \n')

# Estrutura principal do sistema
while not ENCERRAR_SISTEMA:
    # Menu de opções da conta
    print(50 * '=')
    print('\nEscolha uma opção:\n')
    print(' 1: Sacar \n 2: Depositar \n 3: Pagar taxa de manutenção \n 4: Encerrar conta \n ')
    escolha = input('Opção: ').strip()

    # Estrutura principal do menu de opções
    match escolha:
        # Estrutura da opção "Sacar"
        case '1':
            # Validação do saque
            while True:
                # Pergunta o valor a ser sacado
                try:
                    print(f'\nSaldo disponível: R${conta.saldo_da_conta}')
                    saque = float(input('Valor do saque: '))
                # Caso as condições para o saque não sejam atendidas
                except ValueError:
                    print('\n \033[31m Informe um valor válido \033[m')
                else:
                    # Caso as condições para o saque sejam atendidas
                    if conta.saldo_da_conta >= saque > 0:
                        conta.sacar(saque)
                        print('\n \033[32m Saque realizado com sucesso. \033[m \n')
                        break
                    # Caso as condições para o saque não sejam atendidas
                    print('\n \033[31m Informe um valor válido \033[m')

        # Estrutura da opção "Depositar"
        case '2':
            # Validação do depósito
            while True:
                # Pergunta o valor a ser depositado
                try:
                    print(f'\nSaldo disponível: R${conta.saldo_da_conta}')
                    deposito = float(input('Valor do depósito: '))
                # Caso as condições para o depósito não sejam atendidas
                except ValueError:
                    print('\n \033[31m Informe um valor válido \033[m')
                else:
                    # Caso as condições para o depósito sejam atendidas
                    if deposito > 0:
                        conta.depositar(deposito)
                        print('\n \033[32m Depósito realizado com sucesso. \033[m \n')
                        break
                    # Caso as condições para o depósito não sejam atendidas
                    print('\n \033[31m Informe um valor válido \033[m')

        # Estrutura da opção "Pagar taxa de manutenção"
        case '3':
            # Validação do pagamento da taxa
            while True:
                # Pergunta se quer realizar o pagamento da taxa
                pagamento = input(f'\nGostaria de pagar a taxa de manutenção da conta\
 agora (de R${conta.divida_da_conta})? [S/N]: ').strip().upper()
                if pagamento in 'S':
                    # Caso as condições para o pagamento sejam atendidas
                    if conta.saldo_da_conta >= conta.divida_da_conta > 0:
                        conta.pagar_mensal()
                        print('\n \033[32m Taxa paga com sucesso. \033[m \n')
                        break
                    # Caso tenha dívida quitada
                    if conta.divida_da_conta == 0:
                        print('\n \033[31m A taxa já foi paga. \033[m \n')
                        break
                    # Caso tenha saldo insuficiente
                    if conta.saldo_da_conta < conta.divida_da_conta:
                        print('\n \033[31m Saldo insuficiente. \033[m \n')
                        break
                elif pagamento in 'N':
                    break
                else:
                    # Caso o usuário escolha uma opção inválida no menu
                    print('\n \033[31m Informe uma opção válida \033[m')

        # Estrutura da opção "Encerrar conta"
        case '4':
            # Validação do encerramento da conta
            while True:
                # Pergunta se quer encerrar a conta
                print(f'\nPara encerrar a conta, retire todo o saldo restante (de: R$\
 {conta.saldo_da_conta}) e quite a dívida pedente (de: R${conta.divida_da_conta})')
                fechamento = input('Tem certeza que quer encerrar a conta? [S/N]: ').strip().upper()
                if fechamento in 'S':
                    # Caso tenha saldo restante
                    if conta.saldo_da_conta > 0:
                        print('\n \033[31m Retire o saldo restante. \033[m \n')
                        break
                    # Caso tenha dívida pedente
                    if conta.divida_da_conta > 0:
                        print('\n \033[31m Quite a dívida restante. \033[m \n')
                        break
                    # Caso as condições para encerrar a conta sejam atendidas
                    conta.fechar_conta()
                    ENCERRAR_SISTEMA = True
                    del conta
                    break
                # Caso o usuário escolha uma opção inválida no menu
                print('\n \033[31m Informe uma opção válida \033[m')

        # Caso o usuário escolha uma opção inválida no menu
        case _:
            print('\n \033[31m Informe uma opção válida \033[m \n')

# Mensagem de encerramento
print(50 * '=')
print('\n \033[32m Obrigado por usar o Bancão, volte sempre! \033[m \n')
