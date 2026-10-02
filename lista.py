jabocreia = [3,4,7,2,7,3,8]
jaburanga = [7,9,0,2,9,7,3]

lista= []
for numero in jabocreia:
    lista.append(numero) 

for numero in jaburanga:
    lista.append(numero)
    
print(lista)
lista_no = list(set(jabocreia + jaburanga))