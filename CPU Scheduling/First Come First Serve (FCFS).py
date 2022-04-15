if __name__ == "__main__":

    n = int(input()) #mumber of process
    processes = []
    burst_time = []
    for i in range(n):
        process, burstTime = input().split()
        processes.append(process)
        burst_time.append(int(burstTime))


    gantt_chart = "0"
    waiting_time = [0]
    burstTime_new = 0 #sum_of_waiting_time
    for i in range(n):
        burstTime_new += burst_time[i]
        gantt_chart += "  " + processes[i] + "  " + str(burstTime_new)
        if i != n-1:
            waiting_time.append(burstTime_new)
 
    print("My GANTT chart is: ")
    print(gantt_chart)

    print("Average waiting time is: ", sum(waiting_time)/n)