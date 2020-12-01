from FuzzySetOperation import Or
from Rule import *

def Mamdani(rules, input):
    outputFunctions = dict()

    for rule in rules:
        if outputFunctions.get(rule.outputVariable, None) is None:
            outputFunctions[rule.outputVariable] = rule.EvaluateMamdani(input)
        else:
            outputFunctions[rule.outputVariable] = Or(outputFunctions[rule.outputVariable], rule.EvaluateMamdani(input))

    return outputFunctions

def Larsen(rules, input):
    outputFunctions = dict()

    for rule in rules:
        if outputFunctions.get(rule.outputVariable, None) is None:
            outputFunctions[rule.outputVariable] = rule.EvaluateLarsen(input)
        else:
            outputFunctions[rule.outputVariable] = Or(outputFunctions[rule.outputVariable], rule.EvaluateLarsen(input))

    return outputFunctions