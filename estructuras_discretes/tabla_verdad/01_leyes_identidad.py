# P ^ V ≡ a p
# p ∨ F ≡ a p
valores = [True, False]
print("++++++++++++++++++++")
print("+LEYES DE IDENTIDAD+")
print("++++++++++++++++++++")
print(f"p\t|\tp^V\t|\tpvF\t|\tidentidad?")
# print("_______________________________________")
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
for p in valores:
    #verficamos la conjuncion y disyuncion de las preposiciones
    conjuncion = p and True
    disyuncion = p or False

    esIgaul = (conjuncion == p) and (disyuncion == p)

    print(f"{p}\t|\t{conjuncion}\t|\t{disyuncion}\t|\t{esIgaul}")
print(f"\np ≡ p^V | p ≡ pvF\nPor ende son identidad")