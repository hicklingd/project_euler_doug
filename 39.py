import operator
from datetime import datetime
start = datetime.now()
#a^2+b^2=c^2
my_dict = dict()
for a in range(1,500):
    max_b = 500 if a<250 else 1000-2*a
    for b in range(a,max_b):
        c=(a**2+b**2)**0.5
        if c%1==0 and a+b+c<=1000:
            if a+b+c in my_dict:
                my_dict[a+b+c]+=1
            else:
                my_dict[a+b+c]=1

print(max(my_dict, key=lambda key: my_dict[key]))
print(datetime.now()-start) 