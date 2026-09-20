from names import Formula
from dpll import dpll


def prog2(formula: Formula):
    assignment = {}
    result, ass = dpll(formula.clauses, assignment)
    if result:
        #print("FORMULA IS SATISFIABLE")
        #print("Assignment:", ass)
        return True, ass
    else:
        #print("FORMULA IS UNSATISFIABLE")
        return False, None