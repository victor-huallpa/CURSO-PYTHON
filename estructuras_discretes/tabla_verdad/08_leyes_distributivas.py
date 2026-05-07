#leyes distributivas
#p v (q ^ r) ≡ (p v q) ^ (p v r)
#p ^ (q v r) ≡ (p ^ q) v (p ^ r)


valores = [True, False]
print("\tp\t|\tq\t|\tr\t|\tpv(q^r)\t|\t(pvq)^(pvr)\t|\t(p^(qvr)\t|\t(p^q)v(p^r)\t|\distributiva?")
print("___________________________________________________________________________________________________________________")
for p in valores:
    for q in valores:
        for r in valores:

            #variables para cada caso de asocitiva
            
            dis_q_conj_q_r = p or (q and r)
            equi_dis_q_conj_q_r = (p or q) and (p or r)
            conj_p_disyu_q_r = p and (q or r)
            equi_conj_p_disyu_q_r = (p and q) or (p and r)

    
            #validamos respuestas
            es_igual = (dis_q_conj_q_r == equi_dis_q_conj_q_r) and (conj_p_disyu_q_r == equi_conj_p_disyu_q_r)
            print(f"\t{p}\t|\t{q}\t|\t{r}\t|\t{dis_q_conj_q_r}\t|\t{equi_dis_q_conj_q_r}\t|\t{conj_p_disyu_q_r}\t|\t{equi_conj_p_disyu_q_r}\t|\t{es_igual}")

print(f"\np v (q ^ r) ≡ (p v q) ^ (p v r) | p ^ (q v r) ≡ (p ^ q) v (p ^ r)\nPor ende son aosciativas")


