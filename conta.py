#pylint: disable=missing-module-docstring
from random import randint


class ContaBanco():
    """Cria conta no bancão."""

    def __init__(self):
        """Cria conta no bancão.

        Attributes:
            id_da_conta (int): Número de identificação da conta (default randint(1, 10)).
            tipo_da_conta (str): Tipo de conta (default '').
            titular_da_conta (str): Nome do titular (default '').
            saldo_da_conta (float): Saldo disponível na conta (default 0).
            status_da_conta (bool): Status da conta (default False).
            divida_da_conta (int): Dívida pedente (default 0).
        """
        self.id_da_conta = randint(1, 10)
        self.tipo_da_conta = ''
        self.titular_da_conta = ''
        self.saldo_da_conta = 0
        self.status_da_conta = False
        self.divida_da_conta = 0

    @property
    def id_da_conta(self):
        """ID da conta."""
        return self._id_da_conta

    @id_da_conta.setter
    def id_da_conta(self, novo_id : int):
        self._id_da_conta = novo_id

    @property
    def tipo_da_conta(self):
        """Tipo da conta."""
        return self._tipo_da_conta

    @tipo_da_conta.setter
    def tipo_da_conta(self, novo_tipo : str):
        self._tipo_da_conta = novo_tipo

    @property
    def titular_da_conta(self):
        """Titular da conta."""
        return self._titular_da_conta

    @titular_da_conta.setter
    def titular_da_conta(self, novo_titular : str):
        self._titular_da_conta = novo_titular

    @property
    def saldo_da_conta(self):
        """Saldo da conta."""
        return self._saldo_da_conta

    @saldo_da_conta.setter
    def saldo_da_conta(self, novo_saldo : float):
        self._saldo_da_conta = novo_saldo

    @property
    def status_da_conta(self):
        """Status da conta."""
        return self._status_da_conta

    @status_da_conta.setter
    def status_da_conta(self, novo_status : bool):
        self._status_da_conta = novo_status

    @property
    def divida_da_conta(self):
        """Dívida pedente."""
        return self._divida_da_conta

    @divida_da_conta.setter
    def divida_da_conta(self, nova_divida : int):
        self._divida_da_conta = nova_divida

    def abrir_conta(self, titular_da_conta : str, tipo_da_conta : str):
        """Ativa uma conta criada.

        Arguments:
            titular_da_conta: Nome do titular da conta.
            tipo_da_conta: Tipo da conta (corrente ou poupança).

        Conditions:
            Usar os valores 'cc' para conta corrente e 'cp' para conta poupança.

        Notes:
            Conta corrente: R$50 de saldo e R$12 de dívida inicial.
            Conta poupança: R$150 de saldo e R$20 de dívida inicial.
        """
        if not self._status_da_conta:
            self._status_da_conta = True
            self._titular_da_conta = titular_da_conta
            self._tipo_da_conta = tipo_da_conta
            match tipo_da_conta:
                case 'cc':
                    self._saldo_da_conta = 50
                    self._divida_da_conta = 12
                case 'cp':
                    self._saldo_da_conta = 150
                    self._divida_da_conta = 20
        else:
            print('\033[31m Não foi possível abrir a conta. \033[m')

    def fechar_conta(self):
        """Desativa conta ativa.

        Conditions:
            A conta deve estar aberta.\n
            O saldo e a dívida devem estar zerados.
        """
        if not (self._status_da_conta and self._divida_da_conta == 0 and self._saldo_da_conta == 0):
            print('\033[31m Não foi possível desativar a conta. \033[m')

    def depositar(self, deposito : float):
        """Realiza depósitos na conta.

        Arguments:
            deposito: Valor do depósito.

        Conditions:
            O valor do depósito deve ser positivo.
        """
        if deposito > 0:
            self._saldo_da_conta += deposito
        else:
            print('\033[31m Não foi possível realizar o depósito. \033[m')

    def sacar(self, saque : float):
        """Realiza saques na conta.

        Arguments:
            saque: Valor do saque.

        Conditions:
            O valor do saque deve ser positivo.\n
            O valor do saque não deve ser maior que o saldo na conta.
        """
        if self._saldo_da_conta >= saque > 0:
            self._saldo_da_conta -= saque
        else:
            print('\033[31m Não foi possível realizar o saque. \033[m')

    def pagar_mensal(self):
        """Realiza o pagamento da dívida.

        Notes:
            Conta corrente paga R$12.\n
            Conta poupança paga R$20.
        """
        if self._tipo_da_conta == 'cc':
            self._saldo_da_conta -= 12
            self._divida_da_conta = 0
        elif self._tipo_da_conta == 'cp':
            self._saldo_da_conta -= 20
            self._divida_da_conta = 0

    def info(self):
        """Mostra todas as informações da conta."""
        print(f'Titular da conta: {self.titular_da_conta}')
        print(f'Tipo da conta: {self.titular_da_conta}')
        print(f'ID da conta: {self.id_da_conta}')
        print(f'Saldo disponível: {self.saldo_da_conta}')
        print(f'Status da conta: {self.status_da_conta}')
        print(f'Dívida pedente: {self.divida_da_conta}')
