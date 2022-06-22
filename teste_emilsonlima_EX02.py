valor_inicial = 1
valor_secundario = 1
soma_valor = 0
valor_busca = int(input("Digite qual valor você deseja buscar: "))
while soma_valor < valor_busca:
    soma_valor = valor_inicial + valor_secundario
    valor_inicial = valor_secundario
    valor_secundario = soma_valor
    if valor_busca == 1 or soma_valor == valor_busca:
        print("O numero faz parte da sequencia")
    elif soma_valor > valor_busca:
        print("O numero não faz parte da sequencia")


