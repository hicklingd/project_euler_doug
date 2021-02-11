from datetime import datetime
start = datetime.now()

n_t=285
n_p=165
n_h=144
T=n_t*(n_t+1)/2
P=n_p*(3*n_p-1)/2
H=n_h*(2*n_h-1)

while True:
    if T==P==H:
        print(T)
        break
    elif T== min(T,P,H):
        n_t+=1
        T=n_t*(n_t+1)/2
    elif P== min(T,P,H):
        n_p+=1
        P=n_p*(3*n_p-1)/2
    elif H== min(T,P,H):
        n_h+=1
        H=n_h*(2*n_h-1)

print(datetime.now()-start)