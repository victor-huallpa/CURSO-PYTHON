
#ley de doble negacion
#~(~p) ≡ p

valores = [True, False]
print("\tp\t|\t~(~p)\t|\tDoble negacion?")
print("______________________________________________________________")
for p in valores:
    negacionD = not (not p)
    es_igual = (negacionD == p)
    print(f"\t{p}\t|\t{negacionD}\t|\t{es_igual}")

print(f"\np ≡ ~(~p)\nPor ende ley de doble negacion")


