faturamento_diario = [
    2200, 2300, 1800, 2400, 2100, 0, 0, 2500, 3000, 3100, 2800, 2600, 
    2700, 0, 0, 2200, 2400, 2300, 1900, 2900, 2500, 0, 0, 2000, 
    2300, 2200, 2500, 2800, 0, 0
]

faturamento_filtrado = [f for f in faturamento_diario if f > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_da_media = sum(1 for f in faturamento_filtrado if f > media_mensal)

print(f"Menor faturamento do mês: R${menor_faturamento:.2f}")
print(f"Maior faturamento do mês: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")
