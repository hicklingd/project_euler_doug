from datetime import datetime
start = datetime.now()
summ = 0
for num in range(2,354294):
    num1=str(num)
    total=0
    for i in num1:
        total+=int(i)**5
    if total==num:
        summ+=num
print(summ)
print(datetime.now()-start)    