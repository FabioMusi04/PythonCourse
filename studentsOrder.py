""" studenti = [
    {
        "nome": "Mario",
        "cognome": "Rossi",
        "età": 20,
        "classe": "A",
    },
    {
        "nome": "Luca",
        "cognome": "Verdi",
        "età": 22,
        "classe": "B",
    },
    {
        "nome": "Giulia",
        "cognome": "Bianchi",
        "età": 21,
        "classe": "A",
    }
]
ottenere questi ordinamenti (lambda):
- per cognome e a parità di cognome per nome crescente
- per nome e a parità di nome per cognome decrescente
- usare faker per generare i dati """

import faker as fk
fake = fk.Faker()

studenti = [
    {
        "nome": fake.first_name(),
        "cognome": fake.last_name(),
        "età": fake.random_int(18, 30),
        "classe": fake.random_letter(),
    }
    for _ in range(10)
]

print(studenti)

def ordina_cognome_nome(studente):
    for s in studente:
        studente.sort(key=lambda x: (x["cognome"], x["nome"]))
        
        def sort_by_cognome_nome(x):
            return x["cognome"], x["nome"]
        studente.sort(key=sort_by_cognome_nome)
    return studente
def ordina_nome_cognome(studente):
    for s in studente:
        studente.sort(key=lambda x: (x["nome"], x["cognome"]), reverse=True)
        
        def sort_by_nome_cognome(x):
            return x["nome"], x["cognome"]
        studente.sort(key=sort_by_nome_cognome, reverse=True)
    return studente
print(ordina_cognome_nome(studenti))
print(ordina_nome_cognome(studenti))