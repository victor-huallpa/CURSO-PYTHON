#letes de dominacion
#pvV ≡ V
#p^F ≡ F

valores = [True, False]
print("\tp\t|\tpvV\t|\tp^F")
print("___________________________________________________")
for p in valores:
    if p == True or p == False: resul = True
    if p != True or p != False: resul1 = False
    print(f"\t{p}\t|\t{resul}\t|\t{resul1}")

print(f"\nV ≡ pvV | F ≡ p^F\nPor ende son dominaicon")


