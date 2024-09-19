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
def ordina_cognome_nome(studenti):
    return sorted(studenti, key=lambda x: (x["cognome"], x["nome"]))

def ordina_nome_cognome(studenti):
    return sorted(studenti, key=lambda x: (x["nome"], x["cognome"]), reverse=True)

def ordina_cognome_nome_without_lambda(studenti):
    def key(x):
        return x["cognome"], x["nome"]
    return sorted(studenti, key=key, reverse=True)

def ordina_nome_cognome_without_lambda(studenti):
    def key(x):
        return x["nome"], x["cognome"]
    return sorted(studenti, key=key, reverse=True)

print(ordina_cognome_nome(studenti))
print("-" * 50)
print(ordina_nome_cognome(studenti))
print("-" * 50)
print(ordina_cognome_nome_without_lambda(studenti))
print("-" * 50)
print(ordina_nome_cognome_without_lambda(studenti))
print("-" * 50)