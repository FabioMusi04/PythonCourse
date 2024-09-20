""" 3.15 """

""" (Sfida: approssimare la costante matematica e) Scrivete uno script che stimi il valore della costante
matematica e utilizzando la formula qui sotto. Lo script può fermarsi dopo aver sommato 10 termini. 
e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! + 1/6! + 1/7! + 1/8! + 1/9! + 1/10! ... """

e = 0
f = 1

for i in range(0, 10):
    e += 1/f
    f *= (i + 1)
    print(f"Approximation with {i + 1} terms: {e}")
    
print(f"Approximation with 10 terms: {e}")