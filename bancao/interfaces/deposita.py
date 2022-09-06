"""Contém a interface para a funcionalidade de depositar.

Class:
    IDeposita.
"""

from abc import ABC, abstractmethod


class IDeposita(ABC):
    """Interface para a funcionalidade de depósito.

    Methods:
        depositar()
    """

    @abstractmethod
    def depositar(self) -> float:
        """Realiza depósitos.

        Return:
            Novo saldo.
        """

        raise NotImplementedError
