import itertools

class DPLLSolverOptimized:
    def __init__(self, cnf):
        self.cnf = [list(set(clause)) for clause in cnf if clause]
    def solve(self):
        return self.dpll(self.cnf)
    def dpll(self, clauses):
        clauses = self.pure_literal_elimination(clauses)
        while True:
            unit_literals = self.get_unit_literals(clauses)
            if not unit_literals:
                break
            for lit in unit_literals:
                new_clauses = []
                for clause in clauses:
                    if lit in clause:
                        continue
                    new_clause = [l for l in clause if l != -lit]
                    if not new_clause and -lit in clause:
                        return False
                    new_clauses.append(new_clause)
                clauses = new_clauses
        if not clauses:
            return True
        if [] in clauses:
            return False
        literal = self.choose_literal(clauses)
        return (
            self.dpll(self.assign_literal(clauses, literal)) or
            self.dpll(self.assign_literal(clauses, -literal))
        )
    def assign_literal(self, clauses, lit):
        new_clauses = []
        for clause in clauses:
            if lit in clause:
                continue
            new_clause = [l for l in clause if l != -lit]
            if not new_clause and -lit in clause:
                return [[]]
            new_clauses.append(new_clause)
        return new_clauses
    def pure_literal_elimination(self, clauses):
        all_literals = list(itertools.chain(*clauses))
        pure_literals = {lit for lit in set(all_literals) if -lit not in all_literals}
        return [clause for clause in clauses if not any(lit in clause for lit in pure_literals)]
    def get_unit_literals(self, clauses):
        return [clause[0] for clause in clauses if len(clause) == 1]
    def choose_literal(self, clauses):
        flat = list(itertools.chain(*clauses))
        return max(set(flat), key=flat.count)
# ====== Exemplu de testare ======
if __name__ == "__main__":
    formula = [
        [1],
        [1, 2,3],
        [-1,2],
        [2]
    ]

    solver = DPLLSolverOptimized(formula)
    result = solver.solve()
    print("Rezultat:", "Formula este SATISFIABILA" if result else "Formula este NESATISFIABILA")