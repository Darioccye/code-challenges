num_postos, dist_int = map(int, input().split())
pontos = [int(i) for i in input().split()]

pontos_distantes_demais = 0

for i in range(1, num_postos):
    if (pontos[i]-pontos[i-1]) > dist_int:
        pontos_distantes_demais += 1
    if i == num_postos-1:
        if (42195-pontos[i]) > dist_int:
            pontos_distantes_demais += 1

if pontos_distantes_demais == 0:
    print("S")
elif pontos_distantes_demais != 0:
    print("N")


