# Testo dell'esercizio
# Definire una classe Conto sottoclasse di Object
# Definire una classe ContoCorrente sottoclasse di Conto.
# Definire una classe GestoreContiCorrente sottoclasse di Object.
# Definire il costruttore di Conto che accetta
# in input 2 parametri: nome e conto. Gli attributi
# di istanza sono nome e conto.
# Definire il costruttore di ContoCorrente che accetta
# in input 3 parametri: nome, conto e importo. I parametri nome e conto
# devono essere passati alla superclasse mentre la
# variabile saldo deve essere un attributo dell'istanza
# ContoCorrente.
# Definire il saldo come attributo nascosto.
# Definire una property getter, di nome saldo, che ritorna
# il saldo.
# Definire una property setter, di nome saldo, che modifica
# l'attributo saldo.
# All'interno del metodo setter chiamare il metodo che sottrae
# il saldo portandolo a zero. Chiamare poi il metodo deposita
# che definisce il nuovo importo pari al saldo.
# Definire un metodo preleva che accetta in input un importo
# che preleverà dal saldo una certa somma ogni volta che verrà
# invocato.
# Definire un metodo deposita che accetta in unput un importo
# che aggiungerà una certa somma ogni volta che verrà
# invocato.
# Definire un metodo descrizione che stampa il nome del titolare,
# il numero del conto e il saldo.
# Definire un metodo statico bonifico in GestoreContiCorrenti
# che accetta in input 3 parametri: sorgente, destinazione,
# importo. Il metodo bonifico preleva del denaro 
# dal conto sorgente e lo accredita nel conto di
# destinazione.


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
