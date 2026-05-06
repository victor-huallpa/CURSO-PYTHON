print("p\tq\tr\t\t(p^q)\t\t->r")
values = [True, False]
for p in values:
    for q in values:
        for r in values:
            p_en_q = p and q
            # result = 
            if p_en_q == True and r == False:
                result = False
            else:
                result = True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

            print(f"{p}\t{q}\t{r}\t\t{p_en_q}\t\t{result}")
