media = 0
n_pos = 0
for n in range(6):
    number = float(input())
    if number > 0:
        media += number
        n_pos += 1

print("%s valores positivos" % n_pos)
print("%s" % format(float(media/n_pos), ".1f"))
