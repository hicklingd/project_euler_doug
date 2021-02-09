from datetime import datetime
start = datetime.now()
n=1
number=str()
while len(number)<1000000:
    number+=str(n)
    n+=1
total=1
for numb in [10**i-1 for i in range(6)]:
    total*=int(number[numb])

print(total) 



print(datetime.now()-start) 