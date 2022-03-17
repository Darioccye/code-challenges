start = int(input())

while start != 0:
    picos = 0
    casos = ([int(i) for i in input().split()])
    if start == 2:
        picos += 2
    else:
        for i in range(start):
            if i == start-1:
                if casos[i-1] > casos[i] < casos[0]:
                    picos += 1
                if casos[i-1] < casos[i] > casos[0]:
                    picos += 1
            elif i == 0:
                if casos[start-1] > casos[i] < casos[i+1]:
                    picos += 1
                if casos[start-1] < casos[i] > casos[i+1]:
                    picos += 1
            else:
                if casos[i-1] > casos[i] < casos[i+1]:
                    picos += 1
                elif casos[i-1] < casos[i] > casos[i+1]:
                    picos += 1
    print(picos)
    start = int(input())
