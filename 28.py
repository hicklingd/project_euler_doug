from datetime import datetime
start = datetime.now()
highest=1
total=1
count=0
gap=2
while count<500:
    count+=1
    for i in range(highest+gap,highest+5*(gap),gap):
        total+=i
    gap+=2
    highest=i

print(total)
#669171001
print(datetime.now()-start)    