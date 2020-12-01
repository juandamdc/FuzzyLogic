from scipy.integrate import quad

def DiscreteCOA(membershipFunction, domain):
    return sum([ x * membershipFunction(x) for x in range(domain[0], domain[1] + 1)]) / sum([membershipFunction(x) for x in range(domain[0], domain[1] + 1)])


def BOA(membershipFunction, domain, iters = 100):
    totalArea = quad(membershipFunction, domain[0], domain[1]) 
    halfArea = totalArea[0] / 2

    lim_inf = domain[0]
    lim_sup = domain[1]
    z0 = (lim_inf + lim_sup) / 2
    iter_num = 0
    while iter_num < iters:
        calcArea_left = quad(membershipFunction, domain[0], z0)[0]
        calcArea_right = quad(membershipFunction, z0, domain[1])[0]
            
        if abs(calcArea_left - halfArea) < 0.01:
            break

        if calcArea_left > halfArea:
            lim_sup = z0
            z0 = (lim_inf + lim_sup) / 2
        else:
            lim_inf = z0
            z0 = (lim_inf + lim_sup) / 2

        iter_num += 1

    return z0


def DiscreteMOM(membershipFunction, domain):
    maxValue = max([membershipFunction(x) for x in range(domain[0], domain[1] + 1)])
    reachMaximum = [x for x in range(domain[0], domain[1] + 1) if membershipFunction(x) == maxValue]
    return sum(reachMaximum) / len(reachMaximum)