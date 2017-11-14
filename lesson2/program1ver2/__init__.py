def F(list1, list2,n,j):
    if len(list1) == 0:
        return n
    if list1[n] == list2[j+n]:
        n+=1
        if n == len(list1) or j+n == len(list2):
            list1.remove(list1[0])
            return max(n, F(list1, list2,0,0))
        return F(list1, list2,n,j)
    else:
        j+=1
        if j == len(list2):
            j = 0
            list1.remove(list1[0])
        return max(n, F(list1, list2, 0, j))


list1 = [2, 4, 3, 5, 64, 6, 3, 1, 3, 2, 7, 8, 8]
list2 = [1, 4, 3, 9, 2, 3, 5, 4, 6, 4, 5, 6, 3, 1, 3, 5, 7, 7, 8]

n = 0
j = 0
if len(list1) > len(list2):
    list3 = list1
    list1 = list2
    list2 = list3
print(F(list1, list2, n, j))