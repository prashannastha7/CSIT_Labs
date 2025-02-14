'''
Program to implement the csp
'''

from __future__ import print_function

from simpleai.search import CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')

domains = dict((v, ['red', 'green', 'blue']) for v in variables)

# function that returns True if the neighbors of the variables have different values
def const_different(variables, values):
    # expect the value of the neighbors to be different
    return values[0] != values[1]

# constraints between neighbors (states) to have different colors (values)
constraints = [
    (('WA', 'NT'), const_different),
    (('WA', 'SA'), const_different),
    (('SA', 'NT'), const_different),
    (('SA', 'Q'), const_different),
    (('NT', 'Q'), const_different),
    (('SA', 'NSW'), const_different),
    (('Q', 'NSW'), const_different),
    (('SA', 'V'), const_different),
    (('NSW', 'V'), const_different),
]

my_problem = CspProblem(variables, domains, constraints)

print(backtrack(my_problem))
print(backtrack(
        my_problem,
        variable_heuristic=MOST_CONSTRAINED_VARIABLE
    ))
print(backtrack(
    my_problem,
    variable_heuristic=HIGHEST_DEGREE_VARIABLE))
print(backtrack(
    my_problem,
    value_heuristic=LEAST_CONSTRAINING_VALUE
))
print(backtrack(
    my_problem,
    variable_heuristic=MOST_CONSTRAINED_VARIABLE,
    value_heuristic=LEAST_CONSTRAINING_VALUE
))
print(backtrack(
    my_problem,
    variable_heuristic=HIGHEST_DEGREE_VARIABLE,
    value_heuristic=LEAST_CONSTRAINING_VALUE
))
print(min_conflicts(my_problem))
