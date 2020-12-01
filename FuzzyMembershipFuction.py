
def TriangularMembershipFunction(a1, a2, a3):
    def evaluate(x):
        if x <= a1:
            return 0
        elif x <= a2:
            return (x - a1) / (a2 - a1)
        elif x < a3:
            return (a3 - x) / (a3 - a2)
        else:
            return 0
    return evaluate

def TrapezoidalMembershipFunction(a1, a2, a3, a4):
    def evaluate(x):
        if x <= a1:
            return 0
        elif x <= a2:
            return (x - a1) / (a2 - a1)
        elif x <= a3:
            return 1
        elif x < a4:
           return (a4 - x) / (a4 - a3)
        else:
            return 0
    return evaluate

def NullSetMembershipFunction(x):
    return 0

def UniverseSetMembershipFunction(x):
    return 1