""" 3.13 """

""" Nel calcolo delle probabilità spesso si deve calcolare il fattoriale. Il fattoriale di un numero
intero positivo n si scrive n! (n fattoriale) ed è definito così:
n!= n · (n – 1) · (n – 2) · … · 1
per tutti i valori di n maggiori o uguali a 1; per definizione, 0! è uguale a 1. Quindi,
5!= 5· 4· 3· 2· 1
che fa 120. La dimensione dei fattoriali aumenta molto rapidamente. Scrivete uno script che riceva in ingresso
un intero positivo poi ne calcoli il fattoriale e infine lo visualizzi. Provate il vostro script sugli interi 10, 20, 30
e anche su valori più grandi. Avete trovato un intero di cui Python non riesce a produrre il fattoriale? """

while True:
    try:
        n = int(input("Inserisci un numero intero positivo: "))
        if n < 0:
            print("Devi inserire un numero positivo")
            continue
        f = 1
        for i in range(1, n+1):
            f *= i
        print(f)
    except ValueError:
        print("Devi inserire un numero")