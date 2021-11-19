from datetime import datetime

# works a bit like the smallest increasing subsequence or something like that
start = datetime.now()

target = 100
numbers_range_object = range(1, target)
progress_list = [1] + [0]*target


for number in numbers_range_object:
    # for each number we go through and add it to all the indices that it can be added too
    for i in range(number, target+1):
        # for each number we are adding to each index the value of the position with index i-number
        progress_list[i] += progress_list[i-number]

# once this is finished we get the final number in the list as our total
print(progress_list[-1])





# print(count)
print(datetime.now() - start)
