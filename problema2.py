import csv

# função para ordenar a lista da forma desejada
def nome(lista):
    return lista[1]

# le o CSV
arquivo = open("arquivo.txt")

# separa em ;
ler = csv.reader(arquivo, delimiter=';')

# inicializa a lista vazia
lista = []
# usado para pular a primeira linha
conta = 0

# nesse loop transformamos o csv em uma lista
for l in ler:
    if conta > 0:
        lista.append(l)
        lista[-1][1] = lista[-1][1].lower()
    else:
        conta += 1
    
# aqui ordenamos o csv da forma desejada
lista.sort(key=nome)

# printa a lista
print(lista)