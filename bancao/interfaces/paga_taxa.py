"""Contém a interface para a funcionalidade de pagar a taxa de manutenção.

Class:
    IPagaTaxa.
"""

from abc import ABC, abstractmethod


class IPagaTaxa(ABC):
    """Interface para a funcionalidade de pagar a taxa.

    Methods:
        pagar_taxa()
    """

    @abstractmethod
    def pagar_taxa(self) -> tuple[float, int]:
        """Realiza pagamento da taxa de manutenção.

        Return:
            Saldo restante.
            Nova dívida.
        """

        raise NotImplementedError
