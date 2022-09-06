"""Contém a interface para a funcionalidade de sacar.

Class:
    ISaca.
"""

from abc import ABC, abstractmethod


class ISaca(ABC):
    """Interface para a funcionalidade de sacar.

    Methods:
        sacar()
    """

    @abstractmethod
    def sacar(self) -> float:
        """Realiza saques.

        Return:
            Saldo restante.
        """

        raise NotImplementedError
