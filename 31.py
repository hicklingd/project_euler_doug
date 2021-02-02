from datetime import datetime
start = datetime.now()
coins = [1,2,5,10,20,50,100,200]
total=0
for coin1 in range(2):
    if coin1*200==200:
        total+=1
    else:
        for coin2 in range(3):
            if 200*coin1+100*coin2==200:
                total+=1
            else:
                for coin3 in range(5):
                    if 200*coin1+100*coin2+50*coin3==200:
                        total+=1
                    elif 200*coin1+100*coin2+50*coin3>200:
                        break
                    else:
                        for coin4 in range(11):
                            if 200*coin1+100*coin2+50*coin3+20*coin4==200:
                                total+=1
                            elif 200*coin1+100*coin2+50*coin3+20*coin4>200:
                                break
                            else:
                                for coin5 in range(21):
                                    if 200*coin1+100*coin2+50*coin3+20*coin4+10*coin5==200:
                                        total+=1
                                    elif 200*coin1+100*coin2+50*coin3+20*coin4+10*coin5>200:
                                        break
                                    else:
                                        for coin6 in range(41):
                                            if 200*coin1+100*coin2+50*coin3+20*coin4+10*coin5+5*coin6==200:
                                                total+=1
                                            elif 200*coin1+100*coin2+50*coin3+20*coin4+10*coin5+5*coin6>200:
                                                break
                                            else:
                                                for coin7 in range(101):
                                                    if 200*coin1+100*coin2+50*coin3+20*coin4+10*coin5+5*coin6+2*coin7==200:
                                                        total+=1
                                                    elif 200*coin1+100*coin2+50*coin3+20*coin4+10*coin5+5*coin6+2*coin7>200:
                                                        break
                                                    else:
                                                        for coin8 in range(201):
                                                            if 200*coin1+100*coin2+50*coin3+20*coin4+10*coin5+5*coin6+2*coin7+1*coin8==200:
                                                                total+=1



print(total)

print(datetime.now()-start)    