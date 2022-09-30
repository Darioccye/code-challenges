import math

age_days = int(input())

anos = math.floor(age_days/365)
meses = math.floor((age_days - anos*365)/30)
dias = math.floor(age_days - (anos*365 + meses*30))

print("%s ano(s)" % anos)
print("%s mes(es)" % meses)
print("%s dia(s)" % dias)

