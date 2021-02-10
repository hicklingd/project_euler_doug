from itertools import permutations
from datetime import datetime
start = datetime.now()

comb1 = permutations('0123456789')
n=0
my_list = [17,13,11,7,5,3,2]
def is_divisible(index_divider, number, start, end):
    num_1 = int(''.join(number[start:end]))
    if num_1%my_list[index_divider]!=0:
        return False
    if num_1%my_list[index_divider]==0:
        if index_divider==6:
            return True
        return is_divisible(index_divider+1,number,start-1,end-1)

total=0
for number in list(comb1):
    if is_divisible(0,number,7,10):
        total+=int(''.join(number))
print(total)

print(datetime.now()-start) 
