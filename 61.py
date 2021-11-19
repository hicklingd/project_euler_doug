from datetime import datetime
# bit messy because i didnt understand the problem at first and did it the wrong way 

start = datetime.now()

tri_numbers = [int(i*(i+1)/2) for i in range(30,200) if len(str(i*(i+1)/2))==6]

squ_numbers = [int(i**2) for i in range(20,101) if len(str(i**2))==4]

pent_numbers = [int(i*(3*i-1)/2) for i in range(10,100) if len(str(i*(3*i-1)/2))==6]

hex_numbers = [int(i*(2*i-1)) for i in range(0,100) if len(str(i*(2*i-1)))==4]

hept_numbers = [int(i*(5*i-3)/2) for i in range(0,100) if len(str(i*(5*i-3)/2))==6]

oct_numbers= [int(i*(3*i-2)) for i in range(0,100) if len(str(i*(3*i-2)))==4]

all_numbers = [tri_numbers, squ_numbers, pent_numbers, hex_numbers, hept_numbers]





for count_1, basket_1 in enumerate(all_numbers):
    for n_1 in oct_numbers:
        for n_2 in basket_1:
            if str(n_1)[2:] == str(n_2)[:-2] and n_1 not in [n_2]:

                for count_2, basket_2 in enumerate(all_numbers):
                    if count_2 not in [count_1]:
                        for n_3 in basket_2:
                            if str(n_2)[2:] == str(n_3)[:-2] and n_3 not in [n_1, n_2]:

                                for count_3, basket_3 in enumerate(all_numbers):
                                    if count_3 not in [count_1, count_2]:
                                        for n_4 in basket_3:
                                            if str(n_3)[2:] == str(n_4)[:-2] and n_4 not in [n_1, n_2, n_3]:

                                                for count_4, basket_4 in enumerate(all_numbers):
                                                    if count_4 not in [count_1, count_2, count_3]:
                                                        for n_5 in basket_4:
                                                            if str(n_4)[2:] == str(n_5)[:-2] and n_5 not in [n_1, n_2,
                                                                                                             n_3, n_4]:

                                                                for count_5, basket_5 in enumerate(all_numbers):
                                                                    if count_5 not in [count_1, count_2, count_3, count_4]:
                                                                        for n_6 in basket_5:
                                                                            if str(n_5)[2:] == str(n_6)[
                                                                                               :-2] and n_6 not in [n_1,
                                                                                                                    n_2,
                                                                                                                    n_3,
                                                                                                                    n_4, n_5]:
                                                                                if str(n_6)[2:] == str(n_1)[:-2]:
                                                                                    print(n_1+n_2+n_3+n_4+n_5+n_6)



print(datetime.now() - start)
