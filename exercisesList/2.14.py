""" 2.14 """

""" (Calcolo del battito cardiaco) Mentre si fa esercizio fisico, si può usare un cardiofrequenzimetro per
controllare che la propria frequenza cardiaca sia compresa in un intervallo di sicurezza suggerito da dottori o
allenatori. Secondo la American Heart Association (AHA, http://bit.ly/AHATargetHeart-Rates), la
formula per calcolare la propria frequenza cardiaca massima, in battiti per minuto, è 220 meno la propria età
in anni. Durante lo sforzo fisico la frequenza cardiaca dovrebbe essere tra 50% e 85% della frequenza cardiaca
massima. Scrivete uno script che chieda l’età dell’utente e poi calcoli e visualizzi la frequenza cardiaca massima dell’utente e l’intervallo della frequenza cardiaca sotto sforzo. [Queste formule sono stime fornite dalla
AHA; la frequenza cardiaca massima e sotto sforzo possono variare in base allo stato di salute, alla corporatura e al genere di un individuo. Prima di iniziare o modificare una serie di esercizi, è sempre bene
consultare un medico o un professionista.] """


while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError
        max_heart_rate = 220 - age
        min_heart_rate = max_heart_rate * 0.5
        max_heart_rate = max_heart_rate * 0.85
        print(f"Your maximum heart rate is {max_heart_rate} bpm")
        print(f"Your target heart rate range is between {min_heart_rate} and {max_heart_rate} bpm")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")