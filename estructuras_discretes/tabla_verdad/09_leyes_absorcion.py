#leyes de absorcion
#pv(p^q) ≡ p
#p ^ (pvq) ≡ p 

valores = [True, False]
print("\tp\t|\tq\t|\tpv(p^q)\t|\tp^(pvq)\t|\tobasorcion?")
print("___________________________________________________________________________________________________________________")
for p in valores:
    for q in valores:
        #verifcamos si tanto en disjuncion comuntativa y disyuncion comuntativa son iguales
        disyuncion_p_conjuncion_p_q = p or (p and q)
        conjuncion_p_disyuncion_p_q = p and (p or q)
 
        #validamos respuestas
        es_igual = (disyuncion_p_conjuncion_p_q == p) and (conjuncion_p_disyuncion_p_q == p)
        print(f"\t{p}\t|\t{q}\t|\t{disyuncion_p_conjuncion_p_q}\t|\t{conjuncion_p_disyuncion_p_q}\t|\t{es_igual}")

print(f"\npv(p^q) ≡ p | p ^ (pvq) ≡ p\nPor ende son absorcion")


