from datetime import datetime
start = datetime.now()
#ceiling length is 4
highest = 918273645
def check_highest(final,highest):
    if len(final)==9:
            testing_set = set()
            for number in final:
                testing_set.add(number)
                if len(testing_set)==9 and not '0' in testing_set and int(final)>highest:
                    return True
    else:
        return False
#n=2 will have a number >=5000, n=3 100<=number<=332, n=4 25<=number<=33 n=5 6<=number<=9
# therefore we can say that n=3,4 will be strictly smaller and that the highest for n=5 will be when umber is 9
for i in range(24,9876):
    if i>=5000:
        final = str(i) + str(i*2)
        if check_highest(final, highest):
            highest = int(final)
print(highest)
print(datetime.now()-start) 