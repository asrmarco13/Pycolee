class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
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


conto_corrente1 = ContoCorrente('Marco Orfei', '000123456', 1000)
conto_corrente2 = ContoCorrente('Pietro Ciaco', '100123456', 500)

conto_corrente1.descrizione()
conto_corrente2.descrizione()

print('Definite le property invoco' +
      'il setter saldo e stampo i nuovi conti corrente')
conto_corrente1.saldo = 5000
conto_corrente2.saldo = 3000

conto_corrente1.descrizione()
conto_corrente2.descrizione()
