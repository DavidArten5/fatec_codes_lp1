senha_usuario = ("x")
senha_coreta = "123mudar"
while senha_coreta != senha_usuario :
 senha_usuario = input("coloque sua senha: ") 
 if senha_coreta == senha_usuario :
    print("acesso permitido")    
 else:
    print("acesso negado")    