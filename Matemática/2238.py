import time
start = time.time()

A, B, C, D = map(int, input().split())

lis = [A, B, C, D]
lis.sort()
n = []

for i in range(A, lis[-1]+1, A):
    if (i % B) != 0:
        if (C % i) == 0:
            if (D % i) != 0:
                n.append(i)
                break

if len(n) == 0:
    print("-1")
else:
    print(n[0])
print(f'For loop: {time.time() - start} seconds')
print(n)