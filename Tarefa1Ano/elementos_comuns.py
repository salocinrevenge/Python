'''
6 12 18 17 4 15 5 11
12 11 13 7 17 0 5 11 0 2
'''
A=input().split()
B=input().split()
C=[]

for elementoemA in A:
    for elementoemB in B:
        repetiu = False
        for elementoemC in C:
            if elementoemA == elementoemC:
                repetiu = True
        if elementoemA == elementoemB and not repetiu:
            C.append(elementoemA)
for elementoemC in C:
    print(elementoemC, end=" ")