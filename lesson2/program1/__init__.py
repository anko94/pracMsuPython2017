def F(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return 0
    if list1[0] == list2[0]:
        list1.remove(list1[0])
        list2.remove(list2[0])
        return F(list1, list2)+1
    else:
        list3 = list1.copy()
        list4 = list2.copy()
        list3.remove(list3[0])
        list4.remove(list4[0])
        return max(F(list3, list2), F(list1, list4))


list1 = [1, 4, 3, 5, 64, 6, 3, 1, 3, 5, 7, 8, 8]
list2 = [1, 4, 3, 9, 2, 3, 5, 4, 6, 4, 5, 6, 3, 1, 3, 5, 7, 7, 8]

print(F(list1, list2))
