from dataclasses import dataclass


@dataclass
class Literal:
    index: int
    sigma: int


@dataclass
class Clause:
    literals: list

    def __init__(self, literals: list):
        self.literals = literals
        self.op = "OR"


@dataclass
class Formula:
    clauses: list
    num_vars: int
    num_clauses: int

    def __init__(self, clauses: list, num_vars: int, num_clauses: int):
        self.clauses = clauses
        self.num_vars = num_vars
        self.num_clauses = num_clauses
        self.op = "AND"