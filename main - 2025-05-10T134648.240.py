def dp(clauses):
    atoms = {abs(lit) for clause in clauses for lit in clause}
    return dp_recursive(list(atoms), clauses, {})
def dp_recursive(atoms, clauses, values):
    while True:
        if not clauses:
            for a in atoms:
                if a not in values:
                    values[a] = True
            return values
        if [] in clauses:
            return None
        pure = next((lit for lit in set(l for c in clauses for l in c)
                     if -lit not in (l for c in clauses for l in c)), None)
        unit = next((c[0] for c in clauses if len(c) == 1), None)
        if pure:
            values[abs(pure)] = pure > 0
            clauses = [c for c in clauses if pure not in c]
        elif unit:
            values[abs(unit)] = unit > 0
            clauses = [[l for l in c if l != -unit] for c in clauses if unit not in c]
        else:
            break
    for a in atoms:
        if a not in values:
            for guess in [True, False]:
                v = values.copy()
                v[a] = guess
                new_clauses = [[l for l in c if l != (-a if guess else a)]
                               for c in clauses if (a if guess else -a) not in c]
                result = dp_recursive(atoms, new_clauses, v)
                if result:
                    return result
    return None

def read_clauses():
    print("Introduceti clauze CNF in format numeric, fiecare terminata cu 0 (ex: 1 -2 0). ENTER apasat de 2 ori opreste introducerea:")
    clauses = []
    while True:
        line = input("Clauza: ").strip()
        if not line:
            break
        try:
            parts = list(map(int, line.split()))
        except ValueError:
            print("Introduceti doar numere intregi separate prin spatiu.")
            continue
        if parts[-1] != 0:
            print("Fiecare clauza trebuie sa se termine cu 0.")
            continue
        clauses.append(parts[:-1])
    return clauses
if __name__ == "__main__":
    clauses = read_clauses()
    if not clauses:
        print("Nu ati introdus nicio clauza.")
    else:
        result = dp(clauses)
        if result is None:
            print("Aceasta formula este nesatisfiabila.")
        else:
            print("Aceasta formula este satisfiabila.")