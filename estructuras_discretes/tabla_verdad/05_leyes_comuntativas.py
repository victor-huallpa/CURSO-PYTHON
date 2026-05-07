#leyes Comuntativas
#pvq ≡ qvp
#p^q ≡ q^p

valores = [True, False]
print("\tp\t|\tq\t|\tpvq\t|\tqvp\t|\tp^q\t|\tq^p\t|\tcomuntativas?")
print("___________________________________________________________________________________________________________________")
for p in valores:
    for q in valores:
        #verifcamos si tanto en disjuncion comuntativa y disyuncion comuntativa son iguales
        disyuncion_p_q = p or q
        disyuncion_q_p = q or p
        conjuncion_p_q = p and q
        conjuncion_q_p = q and p
 
        #validamos respuestas
        es_igual = (disyuncion_p_q == disyuncion_q_p) and (conjuncion_q_p == conjuncion_p_q)
        print(f"\t{p}\t|\t{q}\t|\t{disyuncion_p_q}\t|\t{disyuncion_q_p}\t|\t{conjuncion_p_q}\t|\t{conjuncion_q_p}\t|\t{es_igual}")

print(f"\npvq ≡ qvp | p^q ≡ q^p\nPor ende son comuntativas")


