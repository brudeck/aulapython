times_brasileirao = (
    "Palmeiras", "Flamengo", "Athletico-PR", "Fluminense", "Cruzeiro",
    "Bahia", "Corinthians", "Red Bull Bragantino", "Botafogo", "Coritiba",
    "Atlético-MG", "São Paulo", "Vitória", "Grêmio", "Mirassol",
    "Internacional", "Santos", "Vasco", "Remo", "Chapecoense"
)

print(f"A) Os 5 primeiros colocados: {times_brasileirao[:5]}")

print(f"B) Os 4 últimos colocados: {times_brasileirao[-4:]}")

print(f"C) Times em ordem alfabética: {tuple(sorted(times_brasileirao))}")

posicao_chape = times_brasileirao.index("Chapecoense") + 1
print(f"D) A Chapecoense está na {posicao_chape}ª posição.")
