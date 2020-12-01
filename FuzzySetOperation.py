
def Complement(func):
    def evaluate(x):
        return 1 - func(x)
    return evaluate

def Or(func1, func2):
    def evaluate(x):
        return max(func1(x), func2(x))
    return evaluate

def And(func1, func2):
    def evaluate(x):
        return min(func1(x), func2(x))
    return evaluate