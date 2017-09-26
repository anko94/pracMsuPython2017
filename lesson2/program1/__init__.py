list1 = [1,4,3,5,64,6,3,1,3,5,7,8,8]
list2 = [1,4,3,9,2,3,5,4,6,4,5,6,3,1,3,5,7,7,8]

n = len(list1)
k = len(list2)
F = []
for i in range(n):
    l = []
    for j in range(k):
        l.append(0)
    F.append(l)

for i in range(n):
    for j in range(k):
        if(list1[i] == list2[j]):
            F[i][j] = F[i-1][j-1]+1
        else:
            F[i][j] = max(F[i-1][j], F[i][j-1])

print(F[n-1][k-1])