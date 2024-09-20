""" 3.21 """

""" (Calcolo del resto usando il minor numero possibile di monete) Scrivete uno script che prenda in ingresso il prezzo di un oggetto che vale un euro o meno. Assumete che l’acquirente paghi con una moneta da
1 euro. Determinate la quantità di resto che il cassiere deve restituire al cliente. Visualizzate il resto usando il
minor numero possibile di monete da 1, 2, 5, 10, 20 e 50 centesimi. Per esempio, se al cliente va dato un resto
di 74 centesimi, lo script visualizzerà:
Il tuo resto è:
monete da 50 centesimi: 1
monete da 20 centesimi: 1
monete da 2 centesimi: 2 """

while True:
    try:
        price = int(input("Inserisci il prezzo dell'oggetto in centesimi: "))
        if price > 100 or price < 0:
            print("Devi inserire un prezzo inferiore a 1 euro")
            continue
        change = 100 - price
        coins = [50, 20, 10, 5, 2, 1]
        for coin in coins:
            if change >= coin:
                print(f"monete da {coin} centesimi: {change // coin}")
                change = change % coin
    except ValueError:
        print("Devi inserire un numero")