valores = [True, False]

print("p\tq\tnot(p and q)\t(not p) or (not q)")
for p in valores:
    for q in valores:
        izquierda = not (p and q)
        derecha = (not p) or (not q)
        print(f"{p}\t{q}\t{izquierda}\t\t\t{derecha}")