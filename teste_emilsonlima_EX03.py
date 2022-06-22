import json

maior_vl = 0
menor_vl = 0
dia_maior = 0
dia_menor = 0
soma = 0
contagem = 0
media = 0
with open("C:\\Users\\Milso\\Desktop\\TESTE\\dados.json") as arq_json:
    dados = json.load(arq_json)

for i in dados:
        if(maior_vl <= 0):
            maior_vl = i["valor"]
            menor_vl = i["valor"]
            dia_menor = i["dia"]
            dia_maior = i["dia"]
        if(i["valor"] != 0):
            contagem += 1
            soma += i["valor"]
            if(i["valor"] < menor_vl):
                menor_vl = i["valor"]
                dia_menor = i["dia"]
            if(i["valor"] > maior_vl):
                maior_vl = i["valor"]
                dia_maior = i["dia"]
media = soma/contagem

print(f"O menor faturamento foi de R${menor_vl:.2f} no dia {dia_menor}.")
print(f"O maior faturamento foi de R${maior_vl:.2f} no dia {dia_maior}.")
print(f"A média de faturamento foi de R${media:.2f}.")


