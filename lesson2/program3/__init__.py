def f(value, power,result):
    if power == 0:
        return result
    if power % 2==1:
        result*=value
    power = (power/2).__int__()
    value*=value
    return f(value, power, result)

result = 1
print(f(3, 5,result))