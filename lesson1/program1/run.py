N = 9
listN = []
for i in range(0,9) :
    listN.append(0)

sum=0
list = [2,5,7,1,8,9,4,5,1,2,3,4,1]
for i in range(0, len(list)) :
    listN[list[i]-1]+=1
for i in range(0,9) :
    if listN[i] != 0 :
        sum += 1

print(sum)