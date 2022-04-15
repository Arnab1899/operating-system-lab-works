if __name__ == "__main__":

    print("Enter Process = ", end="")
    n = int(input()) #mumber of process
    processes = []
    burst_time = []
    priority = []
    print("Enter the Processes, BurstTime, and Priority Value:")
    for i in range(n):
        process, burstTime, priotyTime = input().split()
        processes.append(process)
        burst_time.append(int(burstTime))
        priority.append(int(priotyTime))

    new_burst_time = [x for _, x in sorted(zip(priority, burst_time))]
    new_processes = [x for _,x in sorted(zip(priority, processes))]
    priority.sort() #prority based sorting 

    print("After sort,new table:")
    print(f"Process    BurstTime    Priority")
    for i in range(n):
        print(f"  {new_processes[i]}\t\t\t{new_burst_time[i]}\t\t\t{priority[i]}")

    gantt_chart = "0"
    waiting_time = [0]
    burstTime_new = 0 #sum_of_waiting_time
    for i in range(n):
        burstTime_new += new_burst_time[i]
        gantt_chart += "  " + new_processes[i] + "  " + str(burstTime_new)
        if i != n-1:
            waiting_time.append(burstTime_new)

    print()
    print("GANTT chart: ")
    print(gantt_chart)
    # print(waiting_time)
    print()
    print("Average waiting time: ", sum(waiting_time)/n, "ms")