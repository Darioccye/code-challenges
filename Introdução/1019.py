import math

n = int(input())

hours = math.floor(n/3600)
minutes = math.floor((n - hours*3600)/60)
seconds = math.floor((n - (hours*3600 + minutes*60)))

print("%s:%s:%s" % (hours, minutes, seconds))
