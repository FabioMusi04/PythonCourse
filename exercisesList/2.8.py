""" 2.8 """

""" (Tabella dei quadrati e dei cubi) Scrivete uno script che calcoli i quadrati e i cubi dei numeri da 0 a 5.
Visualizzate i risultati in una tabella come quella mostrata qui sotto. Usate la sequenza di escape \t (tabulazione) per allineare l’output in tre colonne. """

number = [ 0, 1, 2, 3, 4, 5 ]
numberLength = len("number")
squareLength = len("square")
cubeLength = len("cube")

print("number\t square\t cube")
for i in number:
    print(f"{i}\t {i**2}\t {i**3}")
    

print("number\t square\t cube")
for i in number:
    print(f"{i:>{numberLength}}\t {i**2:>{squareLength}}\t {i**3:>{cubeLength}}")