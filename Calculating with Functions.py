def zero(operation = None): 
    if operation is None:
        return 0
    else:
        return operation(0)
def one(operation = None): 
    if operation is None:
        return 1
    else:
        return operation(1)
def two(operation = None):
    if operation is None:
        return 2
    else:
        return operation(2)
def three(operation = None):
    if operation is None:
        return 3
    else:
        return operation(3)
def four(operation = None):
    if operation is None:
        return 4
    else:
        return operation(4)
def five(operation = None):
    if operation is None:
        return 5
    else:
        return operation(5)
def six(operation = None):
    if operation is None:
        return 6
    else:
        return operation(6)
def seven(operation = None):
    if operation is None:
        return 7
    else:
        return operation(7)
def eight(operation = None):
    if operation is None:
        return 8
    else:
        return operation(8)
def nine(operation = None):
    if operation is None:
        return 9
    else:
        return operation(9)

def plus(num): 
    return lambda x: x + num
def minus(num): 
    return lambda x: x - num
def times(num): 
    return lambda x: x * num
def divided_by(num): 
    return lambda x: int(x/num)