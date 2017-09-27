from lesson2.program2.notintexception import NotIntException

def d(list, index, l):
    if index == len(list):
        return l
    i = (len(l)/2).__int__()
    up = len(l)
    down = 0
    a = list[index]
    while i>=0 and not (l[i-1]<=a and l[i]>=a):
        if a < l[i-1]:
            up = i
            i -= ((up-down)/2)
        else :
            down = i
            i += ((up - down)/2)
        i = i.__int__()
    if i >= 0 and l[i-1]!=a:
        l[i] = a
    return d(list, index+1,l)


if __name__ == "__main__":

    list = [2,3,3,3,5,6,8,1,2,3,4,5,6]

    for i in range(len(list)):
        if not type(list[i]) is int:
            raise NotIntException("Element of the list isn't integer")
    l = []
    r = 100000
    for i in range(len(list)+1):
        if i==0:
            l.append(-r)
        else:
            l.append(r)
    l = d(list,0,l)
    i = 1
    sum = 0
    while(l[i]!=r):
        sum+=1
        i+=1
    print(sum)


