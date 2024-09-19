"""  2.9 """

""" (Valore intero di un carattere) In questo capitolo abbiamo imparato a usare le stringhe. Ogni carattere
che appare in una stringa ha una rappresentazione come numero intero. La collezione di caratteri usati su un
computer insieme alla sua rappresentazione tramite intero è chiamato set di caratteri di quel computer. Per
indicare il valore di un carattere in un programma basta racchiuderlo tra virgolette, come 'A'. Per vedere il
valore intero di un carattere, dovete usare la funzione integrata ord:
In [1]: ord('A')
Out[1]: 65
Visualizzate i valori interi equivalenti di B C D b c d 0 1 2 $ * + e del carattere spazio. """

lista = ['B', 'C', 'D', 'b', 'c', 'd', '0', '1', '2', '$', '*', '+', 'e', ' ']
for i in lista:
    print(f"ord('{i}') = {ord(i)}")