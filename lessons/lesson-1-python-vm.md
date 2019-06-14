# Python Virtual Machine (CPython)

Senza entrare troppo nel dettaglio, i linguaggi di programmazione si dividono, a grandi linee, in 2 tipologie:
* [compilato](https://en.wikipedia.org/wiki/Compiler)
* [interpretato](https://en.wikipedia.org/wiki/Interpreter_(computing))

Python è considerato dai meno esperti un linguaggio interpretato. Sebbene possa sembrarlo, questo in realtà non è propriamente vero. Python è una sorta di linguaggio ibrido dove l'interprete compila il codice sorgente in un set di istruzioni definito **"bytecode"**, cioè istruzioni di più basso livello che non sono più quelle del codice sorgente scritte con la sintassi di Python ma che comunque restano ancora indipendenti dalla piattaforma fisica sottostante. Una volta compilato il bytecode la CPython prende in gestione il tutto, lo traduce per la piattaforma specifica e lo esegue. Cosa comporta questo? Di certo una maggiore velocità rispetto al linguaggio interpretato, minore però a quelle di un linguaggio compilato.

![CPython](https://i.imgur.com/PJME67T.png)
