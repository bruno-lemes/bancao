"""Contém a interface para a funcionalidade de ativar a conta.

Class:
    IAtivaConta.
"""

from abc import ABC, abstractmethod


class IAtivaConta(ABC):
    """Interface para a funcionalidade de ativar a conta.

    Methods:
        ativar_conta()
    """

    @abstractmethod
    def ativar_conta(self) -> bool:
        """Ativa conta.

        Return:
            Status da conta.
        """

        raise NotImplementedError
