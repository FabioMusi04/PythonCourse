""" 4.12 """
""" (Simulazione: la lepre e la tartaruga) In questo esercizio creerete la classica gara tra la lepre e la tartaruga. Utilizzeremo la generazione casuale dei numeri per sviluppare una simulazione di questo evento memorabile.
I nostri concorrenti iniziano la gara al primo quadrato di 70. Ogni quadrato rappresenta una posizione
nel percorso della gara. La linea di arrivo è al quadrato 70. Il primo concorrente che raggiunge o sorpassa il
quadrato 70 vincerà un cesto di carote e lattuga. Dato che la corsa si svolge in montagna, a volte i concorrenti
scivoleranno perdendo così terreno.
Un orologio scandisce i secondi. A ogni secondo dell’orologio, la vostra applicazione deve correggere la
posizione degli animali seguendo le regole della tabella qui sotto. Fate uso di variabili per tener traccia delle
posizioni degli animali (numeri da 1 a 70). Ogni animale inizia la gara alla posizione 1. Se uno degli animali
scivola all’indietro oltre la posizione 1, rimettetelo in posizione 1.

Create due funzioni per ottenere le percentuali nella tabella, una per la tartaruga e una per la lepre, generando
un numero intero casuale i nell’intervallo 1 ≤ i ≤ 10. Nella funzione per la tartaruga, essa effettuerà un “passo
veloce” quando 1 ≤ i ≤ 5, una “scivolata” quando 6 ≤ i ≤ 7 e un “passo lento” quando 8 ≤ i ≤ 10. Usate uno
schema simile per la lepre.
Iniziate la gara visualizzando:
BANG !!!!!
PARTITI !!!!!
Dopodiché, a ogni secondo che passa (ossia, a ogni iterazione di un ciclo) visualizzate una riga di 70 posizioni,
mostrando la lettera "T" nella posizione della tartaruga e la lettera "L" nella posizione della lepre. Se i concorrenti finiscono nello stesso quadrato, la tartaruga morde la lepre e il programma deve visualizzare "OUCH!!!"
in quella posizione. Tutte le posizioni al di fuori della "T", della "L" o di "OUCH!!!" devono rimanere vuote.
Ogni volta che visualizzate una riga, controllate se uno degli animali ha raggiunto od oltrepassato il quadrato 70. In questo caso, visualizzate il vincitore e terminate la simulazione. Se vince la tartaruga mostrate
"TARTARUGA VINCE!!! YAY!!!", se vince la lepre mostrate "Lepre vince. Yuch". Se entrambi gli
animali vincono nello stesso momento, potete favorire la tartaruga (quella svantaggiata), o potete visualizzare
"Pareggio". Quando siete pronti a eseguire la vostra applicazione, radunate un gruppo di amici per vedere la
gara. Rimarrete sorpresi dal coinvolgimento degli spettatori!
 """

import random

def tartaruga():
    i = random.randint(1, 10)
    if i <= 5:
        return 3
    elif i <= 7:
        return -6
    else:
        return 1
    
def lepre():
    i = random.randint(1, 10)
    if i <= 2:
        return 0
    elif i <= 4:
        return 9
    elif i <= 5:
        return -12
    elif i <= 8:
        return 1
    else:
        return -2

def main():
    tartaruga_pos = 1
    lepre_pos = 1
    print("BANG !!!!!")
    print("PARTITI !!!!!")
    while True:
        t = tartaruga()
        l = lepre()
        tartaruga_pos += t
        lepre_pos += l
        if tartaruga_pos < 1:
            tartaruga_pos = 1
        if lepre_pos < 1:
            lepre_pos = 1
        for i in range(1, 71):
            if i == tartaruga_pos and i == lepre_pos:
                print("OUCH!!!", end="")
            elif i == tartaruga_pos:
                print("T", end="")
            elif i == lepre_pos:
                print("L", end="")
            else:
                print(" ", end="")
        print()
        if tartaruga_pos >= 70 and lepre_pos >= 70:
            print("Pareggio")
            break
        elif tartaruga_pos >= 70:
            print("TARTARUGA VINCE!!! YAY!!!")
            break
        elif lepre_pos >= 70:
            print("Lepre vince. Yuch")
            break

main()