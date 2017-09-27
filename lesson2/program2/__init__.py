from lesson2.program2.notintexception import NotIntException

def d(list, index, beforeIndex, k):
    if index == len(list):
        return k
    if list[beforeIndex]<list[index]:
        return d(list, index+1,index, k+1)
    else:
        return max(d(list, index+1, index, 1),d(list, index+1,beforeIndex, k))


if __name__ == "__main__":

    list = [2,3,3,3,5,6,8,1,2,3,4]

    for i in range(len(list)):
        if not type(list[i]) is int:
            raise NotIntException("Element of the list isn't int")
    print(d(list,0,0,0))
