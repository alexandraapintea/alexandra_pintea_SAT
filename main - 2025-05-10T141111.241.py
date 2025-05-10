def int_to_literal(n):
    letter = chr(64 + abs(n))  # 1 -> A, 2 -> B, etc.
    return f"¬{letter}" if n < 0 else letter
def generate_clauses_from_input():
    print("Introduceti clauze in format numeric (ex.: 1 2 -3 0). Fiecare clauza trebuie sa se termine cu 0. Apasarea de 2 ori pe ENTER opreste generarea clauzelor.")
    numeric_clauses = []
    logical_clauses = []
    while True:
        line = input("Clauza: ").strip()
        if line == "":
            break
        try:
            values = list(map(int, line.split()))
        except ValueError:
            print("Clauza invalida: trebuie sa contina doar numere intregi.")
            continue
        if not values or values[-1] != 0:
            print("Fiecare clauza trebuie sa se termine cu 0.")
            continue
        values = values[:-1]  # elimina 0 de la final
        if len(values) != len(set(values)):
            print("Clauza invalida: un literal apare de mai multe ori.")
            continue
        # verifica daca un literal si opusul sau apar in aceeasi clauza (clauza tautologica)
        #if any(-v in values for v in values):
            #print("Clauza invalida: un literal si negatia lui apar in aceeasi clauza.")
            #continue
        numeric_clauses.append(values)
        logical_clauses.append([int_to_literal(v) for v in values])
    return numeric_clauses, logical_clauses
if __name__ == "__main__":
    clauses_num, clauses_logic = generate_clauses_from_input()
    print("\nClauze logice:")
    for i, clause in enumerate(clauses_logic, 1):
        print(f"Clauza {i}: {' ∨ '.join(clause)}")