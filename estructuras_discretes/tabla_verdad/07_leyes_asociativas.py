#leyes asociativas
#(pvq) v r ≡ p v (qvr)
#(p^q) ^ r ≡ p ^ (q^r)


valores = [True, False]
print("\tp\t|\tq\t|\tr\t|\t(pvq)vr\t|\tpv(qvr)\t|\t(p^q)^r\t|\tp^(q^r)\t|\tasociativa?")
print("___________________________________________________________________________________________________________________")
for p in valores:
    for q in valores:
        for r in valores:

            #variables para cada caso de asocitiva
            disyuncion_p_q_r = (p or q) or r
            disyuncion_q_r_p = p or (q or r)
            conjuncion_p_q_r = (p and q) and r
            conjuncion_q_r_p = p and (q and r)


            negacion_disyuncion = not (p or q)
            equi_nega_disyun = not p and not q
    
            #validamos respuestas
            es_igual = (disyuncion_p_q_r == disyuncion_q_r_p) and (conjuncion_p_q_r == conjuncion_q_r_p)
            print(f"\t{p}\t|\t{q}\t|\t{r}\t|\t{disyuncion_p_q_r}\t|\t{disyuncion_p_q_r}\t|\t{conjuncion_p_q_r}\t|\t{conjuncion_q_r_p}\t|\t{es_igual}")

print(f"\n(pvq) v r ≡ p v (qvr) | (p^q) ^ r ≡ p ^ (q^r)\nPor ende son asociativas")


