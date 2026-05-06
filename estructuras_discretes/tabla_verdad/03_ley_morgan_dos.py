# Segunda ley de De Morgan:
# La negación de una disyunción equivale a la conjunción
# de las negaciones.
#
#   not (p or q) == (not p) and (not q)
#
# Explicación:
# Si NO es cierto que p o q sean verdaderos,
# entonces ambos deben ser falsos.
valores = [True, False]

print("p\tq\tnot(p or q)\t(not p) and (not q)")

for p in valores:
    for q in valores:

        izquierda = not (p or q)
        derecha = (not p) and (not q)

        print(f"{p}\t{q}\t{izquierda}\t\t{derecha}")