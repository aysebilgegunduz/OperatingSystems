__author__ = 'bilge'

process_queue = []
total_wtime = 0
total_btime = 0
n = int(input('Enter the total no of processes: '))
for i in range(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(input('Enter p_name: '))
    process_queue[i].append(int(input('Enter p_priority: ')))
    process_queue[i].append(int(input('Enter p_bust: ')))
    print('')

process_queue.sort(key = lambda process_queue:process_queue[1])
i = 0
#total_wtime = process_queue[i][2]
total_btime = process_queue[i][2]
for i in range(n):
    if i >0:
        total_btime += process_queue[i][2]
        process_queue[i].append(total_btime)
    else:
        process_queue[i].append(total_btime)


print('ProcessName\tPriority\tBurstTime\tWaitingTime')
for i in range(n):
    print(process_queue[i][0],'\t\t\t\t',process_queue[i][1],'\t\t\t',process_queue[i][2], '\t\t\t', process_queue[i][3]-process_queue[i][2])

print('Total waiting time: ',total_btime)
average=0
for i in process_queue:
    average += (i[3]-i[2])
print('Average waiting time: ',(average/n))