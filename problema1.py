# lista de dicionario dado
listDict = [
    {1 : 1, 2 : "oi", "nome" : "obrigado"},
    {"Bolo" : "Cenoura", "Camarão" : "Verde", "nome" : "Sagrado"},
    {1 : 10, "nome" : "oi", "caracol" : "obrigado"},
    {"nome":"obrigado"}
]

# a chave que será procurada
nome = "nome"

# inicializando a lista vazia 
lista = []

# verifico para cada nome se ele está ou não no dicionário
for dict1 in listDict:
    # se a chave nome estiver no dicionário
    # e o valor dela não tiver sido adicionado a lista, só adicionar na lista
    if nome in dict1 and dict1[nome] not in lista:
        lista.append(dict1[nome])

# printa a lista
print(lista)