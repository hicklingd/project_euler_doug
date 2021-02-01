from datetime import datetime
start = datetime.now()
gap=2
n=0
count=0
full=[1]
while count<1000:
    count+=1
    for i in range(full[-1]+gap,full[-1]+3*(gap),gap):
        n+=1
        full.append(i)
        if n==4:
            n=0
            gap+=2
print(sum(full))
#669171001
print(datetime.now()-start)    