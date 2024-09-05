fat_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

fat_total = sum(fat_estados.values())

print("Percentual de representação por estado:")
for estado, valor in fat_estados.items():
    pct = (valor / fat_total) * 100
    print(f"{estado}: {pct:.2f}%")
