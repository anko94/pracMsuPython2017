list = [1,3,5,3,2,4.0,6,7,4,3]

for i in range(len(list)):
    if(not list[i] is int):
        raise NotIntException