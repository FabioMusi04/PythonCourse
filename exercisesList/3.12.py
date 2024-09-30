""" 3.12 """

"""  Un numero, una parola o una frase di testo che si legge allo stesso modo sia da sinistra a
destra che da destra a sinistra si chiama palindromo. Per esempio, i seguenti interi a cinque cifre sono palindromi: 12321, 55555, 45554 e 11611. Scrivete uno script che legga un intero di 5 cifre e determini se è palindromo.
[Suggerimento: Utilizzate gli operatori // e % per separare il numero in cifre]. """

import math as Math
while True:
    try:
        n = int(input("Inserisci un numero di 5 cifre: "))
        n_len = Math.floor(Math.log10(n)) + 1
        if n_len != 5:
            print("Devi inserire un numero di 5 cifre")
            continue
        for i in range(0, n_len):
            if i == (n_len - 1) - i:
                break
            s = n // 10**i % 10
            e = n // 10**(( n_len-1 ) -i) % 10
            if s != e:
                print("Il numero non è palindromo")
                break
            else:
                print("Il numero è palindromo")
                break
    except ValueError:
        print("Devi inserire un numero")