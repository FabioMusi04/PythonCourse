""" 3.28 """

"""  Calcolate la media, la mediana e la moda
dei valori 9, 11, 22, 34, 17, 22, 34, 22 e 40. Supponete che nei valori ci sia un altro 34. Che problema potrebbe
verificarsi? """

def media(array):
    return sum(array) / len(array)
def mediana(array):
    array.sort()
    n = len(array)
    if n % 2 == 0:
        return (array[n//2] + array[n//2 - 1]) / 2
    else:
        return array[n//2]
def moda(array):
    d = {}
    for i in array:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    m = 0
    for i in d:
        if d[i] > m:
            m = d[i]
    return [i for i in d if d[i] == m]

print(media([9, 11, 22, 34, 17, 22, 34, 22, 40]))
print(mediana([9, 11, 22, 34, 17, 22, 34, 22, 40]))
print(moda([9, 11, 22, 34, 17, 22, 34, 22, 40]))

# Il problema che potrebbe verificarsi è che la moda non è unica, cioè ci sono più valori che si ripetono con la stessa frequenza