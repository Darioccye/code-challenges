x_inicial, y_inicial, x_final, y_final = map(int, input().split())

diferenca_x = (x_final - x_inicial)**2
diferenca_y = (y_final - y_inicial)**2
dif = diferenca_y**0.5 + diferenca_x**0.5

print(int(dif))