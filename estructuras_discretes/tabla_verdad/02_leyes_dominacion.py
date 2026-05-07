#letes de dominacion
#pvV ≡ V
#p^F ≡ F

valores = [True, False]
print("\tp\t|\tpvV\t|\tp^F\t|\tdominacion?")
print("___________________________________________________")
for p in valores:

    #creamos disyuncion y conjuncion para las dominnancias
    disyuncion = p or True
    conjuncion = p and False
    
    #verifcamos si es dominacion
    esIgual = (disyuncion == True) and (conjuncion == False)

    print(f"\t{p}\t|\t{disyuncion}\t|\t{conjuncion}\t|\t{esIgual}")

print(f"\nV ≡ pvV | F ≡ p^F\nPor ende son dominaicon")


