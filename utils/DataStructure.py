
def objTest(obj, functions, args):
    result = []
    for fun, arg in zip(functions[1:], args[1:]):
        result += getattr(obj, fun)(*arg),
        print(fun, arg, result[-1])
    return result
