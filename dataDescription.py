"""
implementare descrizione dataset statistici

dato un dizionario di studenti 

"""


def somma(array):
    s = 0
    for i in array:
        s += i
    return s
def media(array):
    return sum(array) / len(array)
def massimo(array):
    m = array[0]
    for i in array:
        if i > m:
            m = i
    return m
def minimo(array):
    m = array[0]
    for i in array:
        if i < m:
            m = i
    return m
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

p = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
print(somma(p))
print(media(p))
print(massimo(p))
print(minimo(p))
print(mediana(p))
print(moda(p))