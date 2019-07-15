class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.saldo = importo

    def preleva(self, importo):
        self.saldo -= importo

    def deposita(self, importo):
        self.saldo += importo

    def descrizione(self):
        print('Nome titolare: ' +
              self.nome +
              ', conto corrente: ' +
              self.conto +
              ', saldo: ' +
              str(self.saldo))


conto_corrente1 = ContoCorrente('Marco Orfei', '000123456', 1000.00)
conto_corrente2 = ContoCorrente('Pietro Ciaco', '100123456', 500.50)

conto_corrente1.descrizione()
conto_corrente2.descrizione()

conto_corrente1.preleva(100)
conto_corrente2.preleva(50)

conto_corrente1.descrizione()
conto_corrente2.descrizione()

conto_corrente1.deposita(500)
conto_corrente2.deposita(1000)

conto_corrente1.descrizione()
conto_corrente2.descrizione()
