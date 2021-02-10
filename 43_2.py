from itertools import permutations
from datetime import datetime
start = datetime.now()
#could build the numer rather than check it whcich would be quicker
comb1 = permutations('0123456789')
n=0
my_list = [17,13,11,7,5,3,2]

my_dict = dict()
def m_u_1000(divider):
    num=0
    num_set = set()
    while num<1000:
        num+=divider
        num_set.add(num)
    return num_set

my_dict = {k:m_u_1000(k) for k in my_list }
        
def is_divisible(index_divider, number, start, end):
    num_1 = int(''.join(number[start:end]))
    if num_1 not in my_dict[my_list[index_divider]]:
        return False
    elif index_divider==6:
        return True
    else:
        return is_divisible(index_divider+1,number,start-1,end-1)

total=0
for number in list(comb1):
    if is_divisible(0,number,7,10):
        total+=int(''.join(number))
print(total)
    

print(datetime.now()-start)