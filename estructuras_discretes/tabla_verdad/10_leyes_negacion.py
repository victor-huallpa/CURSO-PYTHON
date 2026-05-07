#leyes de neagcion
#pv~p ≡ V
#p^~p ≡ F 

valores = [True, False]
print("\tp\t|\t~p\t|\tpv~p\t|\tp^~p\t|\tnegacion?")
print("___________________________________________________________________________________________________________________")
for p in valores:
    
    #verifcamos si tanto en disjuncion comuntativa y disyuncion comuntativa son iguales
    disyuncion = p or not p
    conjuncion = p and not p

    #validamos respuestas
    es_igual = (disyuncion == True) and (conjuncion == False)
    print(f"\t{p}\t|\t{not p}\t|\t{disyuncion}\t|\t{conjuncion}\t|\t{es_igual}")

print(f"\npv~p ≡ V | p^~p ≡ F\nPor ende son negaciones")


