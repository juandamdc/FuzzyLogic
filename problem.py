from FuzzyMembershipFuction import *
import FIS as sys

lv_bad = TriangularMembershipFunction(-2,1,4)
lv_normal = TrapezoidalMembershipFunction(3,5,7,9)
lv_good = TriangularMembershipFunction(7,10,13)

problem = sys.FIS(['gameplay', 'controls', 'graphics'], ['quality'], [(1,10)], ['lv_bad', 'lv_normal', 'lv_good'], [lv_bad, lv_normal, lv_good], defuzzificationStrategy='BOA')

problem.AddRule(['gameplay'], ['lv_bad'], ['quality'], ['lv_bad'])
problem.AddRule(['controls'], ['lv_bad'], ['quality'], ['lv_bad'])
problem.AddRule(['graphics', 'gameplay', 'controls'], ['lv_bad', 'lv_normal', 'lv_normal'], ['quality'], ['lv_normal'])
problem.AddRule(['graphics', 'gameplay', 'controls'], ['lv_normal', 'lv_normal', 'lv_normal'], ['quality'], ['lv_normal'])
problem.AddRule(['graphics', 'gameplay', 'controls'], ['lv_normal', 'lv_good', 'lv_good'], ['quality'], ['lv_good'])
problem.AddRule(['graphics', 'gameplay', 'controls'], ['lv_good', 'lv_good', 'lv_good'], ['quality'], ['lv_good'])


values = dict()
print("Enter gameplay: ")
values['gameplay'] = int(input())

print("Enter controls: ")
values['controls'] = int(input())

print("Enter graphics: ")
values['graphics'] = int(input())

outputs = problem.Run(values)

for key in outputs.keys():
    print(f'{key}: {outputs[key]}')