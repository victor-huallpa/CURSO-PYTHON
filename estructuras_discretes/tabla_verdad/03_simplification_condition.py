valores = [True, False]

print("p\tq\t(p and q) or (p and not q)\tSimplificando p")

for p in valores:
    for q in valores:
        original = (p and q) or (p and not q)
        simplificando = p
        print(f"{p}\t{q}\t{original}\t\t\t\t{simplificando}")
