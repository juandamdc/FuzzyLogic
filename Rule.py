

class Rule:
    def __init__(self, inputVariables, outputVariable, linguisticMembershipFunctions):
        self.inputVariables = inputVariables
        self.outputVariable = outputVariable
        self.linguisticMembershipFunctions = linguisticMembershipFunctions

    def EvaluateMamdani(self, inputVariablesValues):
        alpha = min([self.linguisticMembershipFunctions[variable](inputVariablesValues[variable]) for variable in self.inputVariables])

        def evaluate(x):
            return min(alpha, self.linguisticMembershipFunctions[self.outputVariable](x))

        return evaluate

    def EvaluateLarsen(self, inputVariablesValues):
        alpha = min([self.linguisticMembershipFunctions[variable](inputVariablesValues[variable]) for variable in self.inputVariables])

        def evaluate(x):
            return alpha * self.linguisticMembershipFunctions[self.outputVariable](x)

        return evaluate