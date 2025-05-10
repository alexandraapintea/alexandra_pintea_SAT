import copy

def pl_resolve(ci, cj):
    resolvents = []
    for i in ci:
        for j in cj:
            if i == -j:
                new_clause = list(set(ci) - {i}) + list(set(cj) - {j})
                resolvents.append(sorted(set(new_clause)))
                return resolvents, True
    return [], False
def pl_resolution(cnf):
    new_clauses = set()
    while True:
        n = len(cnf)
        pairs = [(cnf[i], cnf[j]) for i in range(n) for j in range(i + 1, n)]
        for (ci, cj) in pairs:
            resolvents, found = pl_resolve(ci, cj)
            if found:
                for clause in resolvents:
                    if not clause:
                        return False  # Clauza vida ⇒ nesatisfiabil
                new_clauses.update(tuple(cl) for cl in resolvents)
        if new_clauses.issubset(set(tuple(cl) for cl in cnf)):
            return True  # Nu se mai pot genera clauze noi ⇒ satisfiabil
        for c in new_clauses:
            if list(c) not in cnf:
                cnf.append(list(c))
def read_clauses():
    print("Introduceti clauze CNF in format numeric (ex: 1 -2 3 0). ENTER-ul apasat de 2 ori opreste introducerea:")
    clauses = []
    while True:
        line = input("Clauza: ").strip()
        if not line:
            break
        try:
            numbers = list(map(int, line.split()))
        except ValueError:
            print("Introduceti doar numere intregi separate prin spatiu.")
            continue
        if not numbers:
            continue
        if numbers[-1] != 0:
            print("Fiecare clauza trebuie sa se termine cu 0.")
            continue
        clause = numbers[:-1]
        clauses.append(clause)
    return clauses
if __name__ == "__main__":
    clauses = read_clauses()
    if not clauses:
        print("Nu ati introdus nicio clauza.")
    else:
        result = pl_resolution(clauses)
        if result:
            print("Aceasta formula este satisfiabila")
        else:
            print("Aceasta formula este nesatisfiabila.")