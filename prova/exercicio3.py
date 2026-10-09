# Seu código aqui
produtos = []

while True:
    nome = input("nome do produto ou digite sair para prosseguir: ")
    if nome.lower() == 'sair':
        break
    quantidade = int(input(nome + " ha essa quantidade em estoque: "))
    preço = float(input(nome + " custa: "))

    item = {
        'nome': nome, 
        "quantidade": quantidade,
        "preço": preço
    }
    produtos.append(item)

pesquisa = input("\nqual o item para pesquisar: ")

def inventario(produtos, pesquisa):
    for item in produtos:
        if item['nome'].lower() == pesquisa.lower():
            qtd = item["quantidade"]
            preco = item["preço"]
            total = qtd * preco 
            print(f"produto: {item['nome']} | qtd: {qtd} | preço unitario: R${preco:.2f} | valor total: R${total:.2f}")
            if qtd > 10 :
             print("estoque normal")
            else:
                print("estoque baixo")
            return 
        
    print("produto n encontrado")

itens_em_baixa= 0

for item in produtos:
    if item["quantidade"] < 10:
        itens_em_baixa= itens_em_baixa + 1
    else:
        itens_em_baixa = itens_em_baixa + 0
itens_em_baixa2 = str(itens_em_baixa)
inventario(produtos, pesquisa)
print("ha " + itens_em_baixa2 + " em com estoque baixo" )