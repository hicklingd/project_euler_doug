from datetime import datetime
from itertools import permutations
start = datetime.now()
numbers =[str(i) for i in range(1,10)]
numbers_t = tuple(numbers)
#3 times 2
done=set()
sum_t=0
comb1 = permutations(numbers_t,3)
for num1 in comb1:
    numbers_temp = list(numbers_t)
    for numbers1 in num1:
        numbers_temp.remove(numbers1)
    comb2 = permutations(numbers_temp,2)
    for num2 in comb2:
        lnum = list(num2)
        num3 = list(num1)+lnum
        multiple1 = int(''.join(list(num1)))*int(''.join(list(lnum)))
        checking_num1 = num3 + [num4 for num4 in str(multiple1)]
        checking_num1.sort()
        if tuple(checking_num1)== numbers_t:
            done.add(multiple1)
#4 times 1
comb = permutations(numbers_t,4)
for i in comb:
    numbers_c = list(numbers_t)
    for number_cc in i:
        numbers_c.remove(number_cc)
    for number_ccc in numbers_c:
        number_ct = list(i)
        number_ct+=number_ccc
        multiple = int(''.join(list(i)))*int(number_ccc)
        multiple_str = [dec for dec in str(multiple)]
        checking_num = multiple_str +number_ct
        checking_num.sort()
        if tuple(checking_num) == numbers_t:
            done.add(multiple)
print(sum(done))
print(datetime.now()-start) 