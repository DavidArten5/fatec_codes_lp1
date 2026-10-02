conjunto= set()
conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
print(conjunto)

5 in conjunto 

conjunto2 = set(range(10,15))
conjunto3 = set (range(5,20))
novo_conjunto = conjunto2 | conjunto3 
print(novo_conjunto)

interceçao= conjunto2.intersection(conjunto3)
print(interceçao)
diferença= conjunto2.diference(conjunto3)
print(diferença)