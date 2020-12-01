from Rule import Rule
from InferenceMethod import *
from DefuzzificationStrategy import *

class FIS:
    def __init__(self, inputVariables, outputVariables, domainOutputVariables, linguisticVariables, linguisticVariablesMembershipFunction, inferenceMethod = 'Mamdani', defuzzificationStrategy = 'DiscreteCOA'):
        self.inputVariables = inputVariables
        self.outputVariables = outputVariables
    
        self.membershipFunctions = dict()
        for variable, function in zip(linguisticVariables, linguisticVariablesMembershipFunction):
            self.membershipFunctions[variable] = function
    
        self.domainOutputVariables = dict()
        for variable, domain in zip(outputVariables, domainOutputVariables):
            self.domainOutputVariables[variable] = domain

        self.inferenceMethod = inferenceMethod
        self.defuzzificationStrategy = defuzzificationStrategy
        self.rules = []

    def AddRule(self, inputVariables, linguisticInputVariables, outputVariables, linguisticOutputVariables):
        membershipFunctionsDict = dict()

        for inputVariable, linguisticVariable in zip(inputVariables, linguisticInputVariables):
            membershipFunctionsDict[inputVariable] = self.membershipFunctions[linguisticVariable]
        
        for outputVariable, linguisticVariable in zip(outputVariables, linguisticOutputVariables):
            membershipFunctionsDict[outputVariable] = self.membershipFunctions[linguisticVariable]
            self.rules.append(Rule(inputVariables, outputVariable, membershipFunctionsDict))
    
    def Run(self, inputVariablesValues):
        outputFunctions = None
        outputValues = dict()

        if self.inferenceMethod == 'Mamdani':
            outputFunctions = Mamdani(self.rules, inputVariablesValues)
        elif self.inferenceMethod == 'Larsen':
            outputFunctions = Larsen(self.rules, inputVariablesValues)
        else:
            pass

        if self.inferenceMethod == 'Mamdani' or self.inferenceMethod == 'Larsen':
            if self.defuzzificationStrategy == 'DiscreteCOA':
                for variable in self.outputVariables:
                    outputValues[variable] = DiscreteCOA(outputFunctions[variable], self.domainOutputVariables[variable])
            elif self.defuzzificationStrategy == 'BOA':
                for variable in self.outputVariables:
                    outputValues[variable] = BOA(outputFunctions[variable], self.domainOutputVariables[variable])
            elif self.defuzzificationStrategy == 'DiscreteMOM':
                for variable in self.outputVariables:
                    outputValues[variable] = DiscreteMOM(outputFunctions[variable], self.domainOutputVariables[variable])
            else:
                pass
        else:
            pass

        return outputValues