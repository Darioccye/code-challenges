p1_string = input()
p2_string = input()

p1 = p1_string.split()
p2 = p2_string.split()

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

dist = ((x2-x1)**2 + (y2 - y1)**2)**0.5

print(format(dist, ".4f"))

