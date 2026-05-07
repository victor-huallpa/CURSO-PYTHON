#leyes de idempotencia
#pvp ≡ p
#p^p ≡ p

valores = [True, False]
print("\tp\t|\tpvp\t|\tp^p\t|\tIdempotente?")
print("______________________________________________________________")
for p in valores:
    disyuncion = p or p
    conjuncion = p and p
    es_igual = (disyuncion == p) and (conjuncion == p)
    print(f"\t{p}\t|\t{disyuncion}\t|\t{conjuncion}\t|\t{es_igual}")

print(f"\np ≡ pvp | p ≡ p^p\nPor ende son idempotentes")


