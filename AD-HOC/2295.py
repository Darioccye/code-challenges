alcool, gasolina, kalc, kgas = list(map(float, input().split()))

rendimento_alcool = kalc/alcool
rendimento_gasolina = kgas/gasolina

if rendimento_gasolina >= rendimento_alcool:
    print("G")
if rendimento_alcool > rendimento_gasolina:
    print("A")
