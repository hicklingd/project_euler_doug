from itertools import permutations
from math import factorial
from datetime import datetime
start = datetime.now()
#9!=362880 so max can be assumed to be 7 digits
factorials = tuple([factorial(digit) for digit in range(10)])
sumn=0
for number5 in range(10,100000):
    total=0
    number5_s = [int(nu) for nu in str(number5)]
    max_num = max(number5_s)
    digit_c = number5_s.count(max_num)
    if max_num ==1 and max_num ==2:
        continue
    if max_num == 3 and number5>42:
        continue
    if max_num == 4 and number5>168:
        continue
    if max_num == 5 and number5>840:
        continue
    if max_num == 6 and number5>5040:
        continue
    if max_num == 7 and number5>35280:
        continue
    if max_num == 8 and number5>282240:
        continue
    

    

    for digit in number5_s:
        total+=factorials[digit]
    if total==number5:
        sumn+=number5
print(sumn)
print(datetime.now()-start) 