from names import *
import random

def prog1(n: int, m: int, seed: int = None) -> Formula:
    if seed is not None:
        random.seed(seed)

    clauses = []

    for _ in range(m):
        literals = []
        used_vars = set()

        while len(literals) < 3:
            var = random.randint(1, n)
            if var in used_vars:
                continue
            sigma = random.randint(0, 1)
            literals.append(Literal(var, sigma))
            used_vars.add(var)

        clauses.append(Clause(literals))

    return Formula(clauses, n, m)