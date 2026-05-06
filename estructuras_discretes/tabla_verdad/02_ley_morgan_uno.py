# Primera ley de De Morgan:
# La negación de una conjunción equivale a la disyunción
# de las negaciones.
#
#   not (p and q) == (not p) or (not q)
#
# Explicación:
# Si NO es cierto que p y q sean verdaderos al mismo tiempo,
# entonces al menos uno de ellos debe ser falso.
valores = [True, False]

print("p\tq\tr\tnot(p and q and r)\t(not p) or (not q) or (not r)")

for p in valores:
    for q in valores:
        for r in valores:

            izquierda = not (p and q and r)
            derecha = (not p) or (not q) or (not r)

            print(f"{p}\t{q}\t{r}\t{izquierda}\t\t\t{derecha}")