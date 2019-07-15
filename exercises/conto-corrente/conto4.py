class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto


class ContoCorrente(Conto):
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print('Nome titolare: ' +
              self.nome +
              ', conto corrente: ' +
              self.conto +
              ', saldo: ' +
              str(self.__saldo))


class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)


conto_corrente1 = ContoCorrente('Marco Orfei', '000123456', 1000)
conto_corrente2 = ContoCorrente('Pietro Ciaco', '100123456', 500)

conto_corrente1.descrizione()
conto_corrente2.descrizione()

print('Eseguo bonifico dal conto 1 al conto 2 di 100 euro')
GestoreContiCorrenti.bonifico(conto_corrente1, conto_corrente2, 100)
print('Bonifico eseguito')

conto_corrente1.descrizione()
conto_corrente2.descrizione()
