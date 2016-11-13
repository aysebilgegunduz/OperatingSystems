__author__ = 'bilge'
import copy
def find_smallest(indices, process_queue):
    smallest = process_queue[indices[0]]
    for i in indices:
        if smallest[2] > process_queue[i][2]:
            smallest = process_queue[i]
    return smallest

def normalize(waiting_queue):
    for i in finished_queue:
        temp_list = [x for x in waiting_queue if i[0] in x[0]]
        tmp = i[1]
        time = 0
        for j in temp_list:
            tmp = j[2] - tmp
            time += tmp
            tmp = j[2] + 1
        process_queue.append(i + [time])
    return process_queue

waiting_queue = []
process_queue = []
total_btime = 0
n = int(input('Enter the total no of processes: '))
for i in range(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(input('Enter p_name: '))
    process_queue[i].append(int(input('Enter p_arrival: ')))
    process_queue[i].append(int(input('Enter p_bust: ')))
    print('')

process_queue.sort(key = lambda process_queue:process_queue[1])
finished_queue = copy.deepcopy(process_queue)
min_list = min(process_queue, key=lambda x: x[1])
#(idx for idx in indexes if not visited[idx])
min_list = min((min_val for min_val in process_queue if min_val[1] == min_list[1]), key=lambda x:x[2])
total_btime = min_list[1] + 1
waiting_queue.append(min_list[:2] + [min_list[1]])
total_wtime=0
for i in process_queue:
    total_wtime += i[1]
i = process_queue.index(min_list)
process_queue[i][2] = process_queue[i][2] - 1 #1 ilerletip kontrol etmeliyim bu yüzden btime'ı da 1 azalttim.


while len(process_queue) > 0:
    m = [n for n, (i, s, k) in enumerate(process_queue) if s <= total_btime]
    if len(m)>0:
        j = find_smallest(m, process_queue)
        waiting_queue.append(j[:2] + [total_btime])
        total_btime += 1
        i = process_queue.index(j)
        process_queue[i][2] = process_queue[i][2] - 1
        if process_queue[i][2]==0:
            process_queue.pop(i)
process_queue = normalize(waiting_queue)
print('ProcessName\tArrivalTime\tBurstTime\tWaitingTime')
for i in range(n):
    print(process_queue[i][0],'\t\t\t\t',process_queue[i][1],'\t\t\t\t',process_queue[i][2], '\t\t\t\t', process_queue[i][3])

print('Total waiting time: ',total_btime-min_list[1])
average=0
for i in process_queue:
    average += i[3]
print('Average waiting time: ',(average/n))