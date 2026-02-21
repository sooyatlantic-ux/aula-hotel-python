# Código 1: Usando o FOR
print("--- Ordem Crescente (sem o 13) ---")
for andar in range(1, 21):
    if andar == 13:
        continue
    print(andar)

# Código 2: Usando o WHILE
print("\n--- Usando o While ---")
contador = 1
while contador <= 20:
    if contador != 13:
        print(contador)
    contador += 1

# Código 3: Ordem Decrescente
print("\n--- Ordem Decrescente ---")
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)