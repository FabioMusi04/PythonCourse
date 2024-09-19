""" 2.11 """

"""
(Separare le cifre di un intero) Scrivete uno script che riceva in input dall’utente un intero di 5 cifre.
Separate questo numero nelle sue cifre. Visualizzate ogni cifra separandola dalla successiva con tre spazi. Per
esempio, se l’utente digita 42339, lo script visualizzerà:
4 2 3 3 9
Assumete pure che l’utente inserisca sempre 5 cifre. Usate gli operatori di modulo e di parte intera di una divisione per “estrarre” ogni cifra. """

while True:
    try:
        number = int(input("Enter a 5-digit number: "))
        if number < 10000 or number > 99999:
            raise ValueError
        for i in range(4, -1, -1):
            print(number // 10**i % 10, end="   ")
        print("\n")
    except ValueError:
        print("Invalid input. Please enter a 5-digit number.")