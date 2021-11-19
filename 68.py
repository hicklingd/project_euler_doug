from datetime import datetime
# this solution takes less than 1ms
# string always starts from the outer node with the lowest vale and therefore we can always start from there

start = datetime.now()

numbers = tuple([i for i in range(11)])
list_numbers = list(numbers)
# we must have node1+node2+node3 == node3+node4+node5 = node5+node6+node7 = node7+node8+node9 = node9+node10+node2
# can only use each number once, could iterate over all possible outcomes, with 5 outernodes our first node has to be
# 6
max_number = 0
node1=6
for node4 in [i for i in range(node1+1,11)]:
    for node2 in [a for a in range(1,6)]:
        for node3 in [b for b in range(1,6) if b not in [node2]]:
            for node5 in [c for c in range(1,6) if c not in [node2, node3]]:
                if node1+node2+node3 == node3+node4+node5:
                    for node6 in [d for d in range(node1+1,11) if d not in [node4]]:
                        for node7 in [e for e in range(1,6) if e not in [node2, node3, node5]]:
                            if node1+node2+node3 == node6+node5+node7:

                                for node8 in [f for f in range(node1+1,11) if f not in [node4, node6]]:

                                    for node9 in [g for g in range(1,6) if g not in [node2, node3, node5, node7]]:

                                        if node1+node2+node3 == node8+node7+node9:

                                            for node10 in [h for h in range(node1+1,11) if h not in [node4, node6, node8]]:

                                                if node1+node2+node3 == node10+node9+node2:
                                                    current_number = int(str(node1)+str(node2)+str(node3)+str(node4)+str(node3)+str(node5)+str(node6)+str(node5)+str(node7)+str(node8)+str(node7)+str(node9)+str(node10)+str(node9)+str(node2))
                                                    if current_number>max_number:
                                                        max_number = current_number


print(max_number)

print(datetime.now() - start)
