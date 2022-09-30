a = input()
b = input()

c = a.split()
d = b.split()

first_code = int(c[0])
first_qty = float(c[1])
first_price = float(c[2])

second_code = int(d[0])
second_qty = float(d[1])
second_price = float(d[2])

fp_total = first_qty*first_price
sp_total = second_qty*second_price
total = fp_total+sp_total
total = format(total, ".2f")

print("VALOR A PAGAR: R$ %s" % total)