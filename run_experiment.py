from prog1 import prog1
from prog2 import prog2


def generate_samples(n, m, num_samples=100):
    formulas = []
    for seed in range(num_samples):
        formula = prog1(n, m, seed)
        formulas.append(formula)
    return formulas


def check_satisfiability(formulas):
    sat_count = 0
    for formula in formulas:
        result, _ = prog2(formula)
        if result:
            sat_count += 1
    return sat_count

def calculate_r(n, m, num_samples=100):
    formulas = generate_samples(n, m, num_samples)
    sat_count = check_satisfiability(formulas)
    r = sat_count / num_samples
    return r