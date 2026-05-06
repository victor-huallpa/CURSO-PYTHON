valores = [True, False]

print("p\tq\tr\tnot(p and q and r)\t(not p) or (not q) or (not r)")

for p in valores:
    for q in valores:
        for r in valores:

            izquierda = not (p and q and r)
            derecha = (not p) or (not q) or (not r)

            print(f"{p}\t{q}\t{r}\t{izquierda}\t\t\t{derecha}")