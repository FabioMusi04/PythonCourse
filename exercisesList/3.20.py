""" 3.20 """


""" (Conversione da binario a decimale) Prendete in ingresso un numero composto solo di cifre 0 e 1
(un numero binario) e visualizzate il numero decimale equivalente. [Suggerimento: Utilizzate gli operatori di
modulo e divisione per selezionare le cifre binarie una alla volta da destra verso sinistra. Come nel sistema numerico decimale, dove la cifra più a destra ha valore posizionale uguale a 1 e la cifra alla sua sinistra ha valore
posizionale uguale a 10, poi 100, poi 1000 ecc., nel sistema numerico binario la cifra più a destra ha valore
posizionale uguale a 1 e la cifra alla sua sinistra ha valore posizionale uguale a 2, poi 4, poi 8 ecc. Quindi, il
valore decimale 234 può essere interpretato come 2 * 100 + 3 * 10 + 4 * 1. Il valore decimale equivalente al
numero binario 1101 è 1 * 8 + 1 * 4 + 0 * 2 + 1 *1.] """

import math

def isBinary(n):
    n_len = math.floor(math.log10(n)) + 1
    for i in range(0, n_len):
        v = n // 10**i % 10
        if v != 0 and v != 1:
            return False
    return True
        

while True:
    try:
        binary = int(input("Inserisci un numero binario: "))
        if not isBinary(int(binary)):
            print("Devi inserire un numero binario")
            continue
        decimal = 0
        n_len = math.floor(math.log10(binary)) + 1
        for i in range(0, n_len):
            v = int(binary) // 10**i % 10
            decimal += v * 2**i
        print(decimal)
        
        decimal_len = math.floor(math.log10(decimal)) + 1

        for i in range(decimal_len - 1, -1, -1): 
            cifra = decimal // 10**(i) % 10
            if i > 0:
                print(f"{cifra} * {10**i} + ", end="")
            else:
                print(f"{cifra} * {10**i}", end="")

        print("\n")

    
    except ValueError:
        print("Devi inserire un numero binario")