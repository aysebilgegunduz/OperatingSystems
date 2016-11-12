__author__ = 'bilge'
def find_smallest(indices, process_queue):
    smallest = process_queue[indices[0]]
    for i in indices:
        if smallest[2] > process_queue[i][2]:
            smallest = process_queue[i]
    return smallest

waiting_queue = []
process_queue = []
total_wtime = 0
total_btime = 0
n = int(input('Enter the total no of processes: '))
for i in range(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(input('Enter p_name: '))
    process_queue[i].append(int(input('Enter p_arrival: ')))
    process_queue[i].append(int(input('Enter p_bust: ')))
    print('')

process_queue.sort(key = lambda process_queue:process_queue[1])
min_list = min(process_queue, key=lambda x: x[1])
total_btime = min_list[2]
waiting_queue.append(min_list + [min_list[1]])
total_btime = min_list[2]
i = process_queue.index(min_list)
process_queue.pop(i)

for i in range(n-1):
    m = [n for n, (i, s, k) in enumerate(process_queue) if s <= total_btime]
    if len(m)>0:
        j = find_smallest(m, process_queue)
        waiting_queue.append(j + [total_btime - j[1]])
        total_btime += j[2]
        process_queue.remove(j)

print('ProcessName\tArrivalTime\tBurstTime\tWaitingTime')
for i in range(n):
    print(waiting_queue[i][0],'\t\t\t\t',waiting_queue[i][1],'\t\t\t\t',waiting_queue[i][2], '\t\t\t\t', waiting_queue[i][3])

print('Total waiting time: ',total_btime)
average=0
for i in waiting_queue:
    average += i[3]
print('Average waiting time: ',(average/n))