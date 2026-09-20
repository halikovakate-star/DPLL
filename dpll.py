from names import Literal, Clause


def is_empty_formula(clauses):
    return len(clauses) == 0

def has_empty_clause(clauses):
    for clause in clauses:
        if len(clause.literals) == 0:
            return True
    return False

def find_unit_clause(clauses):
    for clause in clauses:
        if len(clause.literals) == 1:
            return clause.literals[0]
    return None

def assign_variable(assignment, var, value):
    assignment[var] = value

def get_opposite_literal(literal):
    if literal.sigma == 1:
        return Literal(literal.index, 0)
    else:
        return Literal(literal.index, 1)

def remove_clauses_with_literal(clauses, literal):
    new_clauses = []
    for clause in clauses:
        contains_literal = False
        for lit in clause.literals:
            if lit.index == literal.index and lit.sigma == literal.sigma:
                contains_literal = True
                break
        if not contains_literal:
            new_clauses.append(clause)
    return new_clauses

def remove_opposite_literals(clauses, literal):
    new_clauses = []
    for clause in clauses:
        new_literals = []
        for lit in clause.literals:
            if not (lit.index == literal.index and lit.sigma != literal.sigma):
                new_literals.append(lit)
        new_clauses.append(Clause(new_literals))
    return new_clauses

def apply_unit_rule(clauses, assignment):
    changed = True
    while changed:
        changed = False
        unit_lit = find_unit_clause(clauses)
        if unit_lit is not None:
            assign_variable(assignment, unit_lit.index, unit_lit.sigma)
            clauses = remove_clauses_with_literal(clauses, unit_lit)
            clauses = remove_opposite_literals(clauses, unit_lit)
            changed = True
    return clauses

def find_pure_literal(clauses):
    var_signs = {}
    for clause in clauses:
        for lit in clause.literals:
            if lit.index not in var_signs:
                var_signs[lit.index] = set()
            var_signs[lit.index].add(lit.sigma)

    for var, signs in var_signs.items():
        if len(signs) == 1:
            sigma = signs.pop()
            return Literal(var, sigma)
    return None

def apply_pure_rule(clauses, assignment):
    changed = True
    while changed:
        changed = False
        pure_lit = find_pure_literal(clauses)
        if pure_lit is not None:
            assign_variable(assignment, pure_lit.index, pure_lit.sigma)
            clauses = remove_clauses_with_literal(clauses, pure_lit)
            changed = True
    return clauses

def choose_branching_variable(clauses):
    var_count = {}
    for clause in clauses:
        for lit in clause.literals:
            if lit.index not in var_count:
                var_count[lit.index] = 0
            var_count[lit.index] += 1

    max_count = -1
    chosen_var = None
    for var, count in var_count.items():
        if count > max_count:
            max_count = count
            chosen_var = var
    return chosen_var

def apply_branching(clauses, assignment):
    var = choose_branching_variable(clauses)
    if var is None:
        return True, assignment

    lit_false = Literal(var, 0)
    new_clauses = remove_clauses_with_literal(clauses, lit_false)
    new_clauses = remove_opposite_literals(new_clauses, lit_false)
    new_assignment = assignment.copy()
    assign_variable(new_assignment, var, 0)
    result, ass = dpll(new_clauses, new_assignment)
    if result:
        assignment.update(ass)
        return True, assignment

    lit_true = Literal(var, 1)
    new_clauses = remove_clauses_with_literal(clauses, lit_true)
    new_clauses = remove_opposite_literals(new_clauses, lit_true)
    new_assignment = assignment.copy()
    assign_variable(new_assignment, var, 1)
    result, ass = dpll(new_clauses, new_assignment)
    if result:
        assignment.update(ass)
        return True, assignment

    return False, None

def dpll(clauses, assignment):
    if is_empty_formula(clauses):
        return True, assignment

    if has_empty_clause(clauses):
        return False, None

    clauses = apply_unit_rule(clauses, assignment)

    if is_empty_formula(clauses):
        return True, assignment

    if has_empty_clause(clauses):
        return False, None

    clauses = apply_pure_rule(clauses, assignment)

    if is_empty_formula(clauses):
        return True, assignment

    if has_empty_clause(clauses):
        return False, None

    return apply_branching(clauses, assignment)