valores = [True, False]

print("p\tq\t(q -> p)\t(q -> p) or (q -> p")

for p in valores:
    for q in valores:
        p_imp_q = (not p) or q
        q_imp_p = (not q) or p
        resultado = p_imp_q or q_imp_p
        print(f"{p}\t{q}\t{p_imp_q}\t{q_imp_p}\t{resultado}")