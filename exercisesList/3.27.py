""" 3.27 """

""" (Crescita della popolazione mondiale) Negli ultimi secoli la popolazione mondiale è cresciuta in maniera considerevole. La crescita continua potrebbe mettere alla prova i limiti di aria respirabile, acqua potabile,
terra arabile e altre risorse limitate. Ci sono prove che mostrano come la crescita stia recentemente rallentando
e che la popolazione mondiale possa raggiungere il picco in questo secolo, per poi iniziare a calare.
Per questo esercizio dovete cercare i problemi relativi alla crescita della popolazione. Essendo un tema controverso, dovete essere sicuri di trovare punti di vista diversi. Trovate delle stime sulla popolazione mondiale
attuale e sul suo tasso di crescita. Scrivete uno script che calcoli la crescita della popolazione mondiale per ogni
anno per i prossimi 100 anni. Assumete che il tasso di crescita resti costante. Visualizzate i dati in una tabella.
Nella prima colonna devono apparire gli anni, da 1 a 100. Nella seconda colonna visualizzate la popolazione
stimata per la fine di quell’anno. Nella terza colonna mostrate l’incremento numerico occorso nella popolazione per la fine di quell’anno. Usando questi risultati, determinate gli anni in cui la popolazione dovrebbe
raddoppiare ed eventualmente quadruplicare rispetto a oggi.
 """
 
 
population = 7.9e9
growth_rate = 0.01
years = 200
population_growth = population

print("Year\tPopulation\tGrowth")
doubled = False
quadrupled = False

for i in range(years):
    population_growth += population_growth * growth_rate
    print(f"{i + 1}\t{population_growth:.2f}\t{(population_growth - population):.2f}")
    
    if not doubled and population_growth >= 2 * population:
        print(f"Population will double in {i + 1} years")
        doubled = True
        
    if not quadrupled and population_growth >= 4 * population:
        print(f"Population will quadruple in {i + 1} years")
        quadrupled = True
        
    if doubled and quadrupled:
        break