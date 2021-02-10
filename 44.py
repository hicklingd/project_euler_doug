from datetime import datetime
start = datetime.now()

def is_pang(number1):
    if (1+(24*number1+1)**0.5)%6==0:
        return True
    return False

j=1
break_c=True
while break_c == True:
    num_1 = j*(3*j-1)/2
    for n in range(1,j):
        num_2 = n*(3*n-1)/2        
        num_3 = num_1-num_2
        if is_pang(num_3):
            num_4 = num_1+num_2
            if is_pang(num_4):
                print(num_1-num_2)
                break_c=False 
    j+=1

print(datetime.now()-start)