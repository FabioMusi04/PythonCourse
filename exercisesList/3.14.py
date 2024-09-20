""" 3.14 """

""" (Sfida: approssimare la costante matematica π) Scrivete uno script che calcoli il valore di π usando la
seguente serie infinita. Visualizzate una tabella che mostri il valore di π approssimato da un termine di questa
serie, da due termini, da tre termini e così via. Quanti termini della serie dovete usare per ottenere 3.14? E
3.141? E 3.1415? E 3.14159? 
π = 1 + 1/!1 + 1/!2 + 1/!3 ...
"""
target_values = [3.14, 3.141, 3.1415, 3.14159]
approximations = {}
pi_approx = 0
i = 0
sign = 1

for target in target_values:
    pi_approx = 0
    i = 0
    while True:
        # Leibniz formula for Pi: alternating series
        pi_approx += sign * (4 / (2 * i + 1))
        sign *= -1  # Alternate the sign
        print(f"Approximation with {i + 1} terms: {pi_approx}")
        
        if round(pi_approx, len(str(target)) - 2) == target:
            print(f"Target {target} reached with {i + 1} terms")
            approximations[target] = i + 1
            break
        i += 1

print(approximations)

