SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

TOTAL = SP + RJ + MG + ES + OUTROS
PERC_SP = SP / TOTAL * 100
PERC_RJ = RJ / TOTAL * 100
PERC_MG = MG / TOTAL * 100
PERC_ES = ES / TOTAL * 100
PERC_OUTROS = OUTROS / TOTAL * 100

print(f'SP representou {PERC_SP:.2f}% do valor total mensal')
print(f'RJ representou {PERC_RJ:.2f}% do valor total mensal')
print(f'MG representou {PERC_MG:.2f}% do valor total mensal')
print(f'ES representou {PERC_ES:.2f}% do valor total mensal')
print(f'Outros estados representaram {PERC_OUTROS:.2f}% do valor total mensal')