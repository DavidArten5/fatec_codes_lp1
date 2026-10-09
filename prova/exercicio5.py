# Seu código aqui
# Definindo as informações de cada cargo da tabela nas listas
# Estrutura: [Código, Nome do Cargo, Salário Base, Benefícios, Percentual do Imposto]
lista1 = [1, "Auxiliar Administrativo", 2200.00, 350.00, 0.075]
lista2 = [2, "Técnico de TI", 3520.00, 450.00, 0.09]
lista3 = [3, "Analista", 4400.00, 500.00, 0.11]
lista4 = [4, "Coordenador", 6600.00, 800.00, 0.14]
lista5 = [5, "Gerente", 8800.00, 1200.00, 0.18]

# Agrupando no quadro de funcionários (sua matriz/tabela)
quadro_de_funcionarios = [lista1, lista2, lista3, lista4, lista5]

# Variáveis acumuladoras para o relatório final
funcionarios_processados = 0
total_folha_pagamento = 0.0

# 1. Solicita a quantidade de funcionários
qtd_funcionarios = int(input("Digite a quantidade de funcionários a cadastrar: "))

# Loop para rodar exatamente a quantidade de vezes pedida
for i in range(qtd_funcionarios):
    print(f"\n--- Cadastro do {i+1}º Funcionário ---")
    nome = input("Nome do funcionário: ")
    codigo_cargo = int(input("Código do cargo (1 a 5): "))
    horas_extras = float(input("Quantidade de horas extras trabalhadas no mês: "))
    
    # 2. Busca o código digitado dentro do quadro de funcionários
    cargo_encontrado = None
    for linha in quadro_de_funcionarios:
        if linha[0] == codigo_cargo:
            cargo_encontrado = linha
            break
            
    # 3. Tratamento caso o código não exista
    if cargo_encontrado is None:
        print("Código inválido!")
        continue # Pula para o próximo funcionário sem somar nada
        
    # Se achou o cargo, extrai os valores da lista correspondente
    cargo_nome = cargo_encontrado[1]
    salario_base = cargo_encontrado[2]
    beneficios = cargo_encontrado[3]
    imposto_percentual = cargo_encontrado[4]
    
    # 4. Aplicação das fórmulas da imagem
    valor_hora = salario_base / 220
    valor_horas_extras = horas_extras * valor_hora * 1.5
    imposto = (salario_base + valor_horas_extras) * imposto_percentual
    salario_liquido = salario_base + valor_horas_extras + beneficios - imposto
    
    # Exibe os dados individuais do funcionário
    print(f"\nFuncionário: {nome}")
    print(f"Cargo: {cargo_nome}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    
    # Acumula os dados válidos para o resultado final
    funcionarios_processados += 1
    total_folha_pagamento += salario_liquido

# 5. Exibição do relatório final solicitado
print("\n================ REPORT FINAL ================")
print(f"Total de funcionários processados: {funcionarios_processados}")
print(f"Valor total da folha de pagamento: R$ {total_folha_pagamento:.2f}")
print("==============================================")
