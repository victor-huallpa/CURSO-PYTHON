# P ^ V ≡ a p
# p ∨ F ≡ a p
valores = [True, False]
print("++++++++++++++++++++")
print("+LEYES DE IDENTIDAD+")
print("++++++++++++++++++++")
print(f"p\t|\tp^V\t|\tpvF")
# print("_______________________________________")
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
for val in valores:
    
    if val == True: resul = True
    else: resul =False
    if val == False: resul1 = False
    else: resul1 = True
    print(f"{val}\t|\t{resul}\t|\t{resul1}")
print(f"\np ≡ p^V | p ≡ pvF\nPor ende son identidad")