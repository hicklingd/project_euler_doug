from datetime import datetime
print(datetime.now())
start = datetime.now()

num = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
num_n = num.split('\n')
py = []
for i in num_n:
    current = i.split(' ')
    current = [int(nn) for nn in current]
    py.append(current)
#row is a rnum col is a _num so r33_23 is row 33 col 23
rows = ['r'+str(i) for i in range(1,16)]
#pyr = [rows[n] for i in range(rows[n][-1]) for n in range(len(rows))]
row = 1
keys_c = []
for i in range(len(rows)+1):
    keys_c.append(['r'+str(i)+'_'+str(ab) for ab in range(i)])
keys_c = keys_c[1:]
#create dict
dict_total = {}
for i in range(len(keys_c)):
    dict_temp = dict(zip(keys_c[i], py[i]))
    dict_total_n = {**dict_total, **dict_temp}
    dict_total = dict_total_n

for i in dict_total:
    current = i.split('_')
    #col = 0
    if current[1] == '0' and current[0][1:] != '1':
        #print('r'+str(int(current[0][1:])-1)+'_0')
        dict_total[i] = dict_total[i]+dict_total['r'+str(int(current[0][1:])-1)+'_0']
    # col = final
    elif int(current[1])+1 == int(current[0][1:]) and current[0][1:] != '1':
        dict_total[i] = dict_total[i]+dict_total['r'+str(int(current[0][1:])-1)+'_'+str(int(current[0][1:])-2)]

    elif current[0][1:] != '1':
        if dict_total['r'+str(int(current[0][1:])-1)+'_'+str(int(current[1])-1)]>dict_total['r'+str(int(current[0][1:])-1)+'_'+str(int(current[1]))]:
            dict_total[i] = dict_total[i]+dict_total['r'+str(int(current[0][1:])-1)+'_'+str(int(current[1])-1)]
        else:
            dict_total[i] = dict_total[i]+dict_total['r'+str(int(current[0][1:])-1)+'_'+str(int(current[1]))]
    

maximum = max(dict_total.values())

print(datetime.now()-start)