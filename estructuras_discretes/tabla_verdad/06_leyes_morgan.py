#leyes de morgan
#~(p^q) ≡ ~p v ~q
#~(pvq) ≡ ~p ^ ~q


valores = [True, False]
print("\tp\t|\tq\t|\t~(p^q)\t|\t~q v ~q\t|\t~(pvq)\t|\t~p ^ ~q\t|\tmorgan?")
print("___________________________________________________________________________________________________________________")
for p in valores:
    for q in valores:
        #verifcamos si tanto en disjuncion comuntativa y disyuncion comuntativa son iguales
        negacion_conjuncion = not (p and q)
        equi_nega_conj = not p or not q

        negacion_disyuncion = not (p or q)
        equi_nega_disyun = not p and not q
 
        #validamos respuestas
        es_igual = (negacion_conjuncion == equi_nega_conj) and (negacion_disyuncion == equi_nega_disyun)
        print(f"\t{p}\t|\t{q}\t|\t{negacion_conjuncion}\t|\t{equi_nega_conj}\t|\t{negacion_disyuncion}\t|\t{equi_nega_disyun}\t|\t{es_igual}")

print(f"\n~(p^q) ≡ ~p v ~q | ~(pvq) ≡ ~p ^ ~q\nPor ende son leyes de Morgan")


