nota1 = [0,0,0,0,0,0]
nota2 = [0,0,0,0,0,0]
for nota in range(len(nota1)) :
    nota1[nota] = float(input("digite a nota1 do aluno :"))
   
for nota in range(len(nota2)):
    nota2[nota] = float(input("digite a nota2 do aluno :"))
    
print(nota1)
print(nota2)

for item in range(len(nota1)):
    media= nota1[item] + nota2[item]
    media= media / 2 

if media <= 3.0:
    print("reprovao")
elif  media <= 7.0 :
    print("exame")
else:
    print("aprovado")         