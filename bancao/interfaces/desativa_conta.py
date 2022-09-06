"""Contém a interface para a funcionalidade de desativar a conta.

Class:
    IDesativaConta.
"""

from abc import ABC, abstractmethod


class IDesativaConta(ABC):
    """Interface para a funcionalidade de desativar a conta.

    Methods:
        desativar_conta()
    """

    @abstractmethod
    def desativar_conta(self) -> bool:
        """Desativa conta.

        Return:
            Status da conta.
        """

        raise NotImplementedError
