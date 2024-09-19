""" 2,12  """

""" (Rendimento del 7% sull’investimento) Alcuni consulenti finanziari sostengono che sia ragionevole
aspettarsi un rendimento del 7% sugli investimenti azionari a lungo termine. Assumendo di aver investito
$1.000, calcolate e visualizzate quanti soldi avrete dopo 10, 20 e 30 anni. Usate la seguente formula per calcolare queste cifre:
a=p(1 + r) n
dove
p è la cifra iniziale investita ($1.000);
r è il tasso di rendimento annuale (7%);
n è il numero di anni (10, 20 o 30);
a è il denaro posseduto alla fine dell’n-esimo anno. """

initial_investment = 1000
annual_rate = 0.07

for years in [10, 20, 30]:
    amount = initial_investment * (1 + annual_rate) ** years
    print(f'After {years} years, you will have ${amount:.2f}')