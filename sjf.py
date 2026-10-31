
n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append((i+1, bt))

# Sort by burst time
processes.sort(key=lambda x: x[1])

wt = [0] * n
tat = [0] * n

for i in range(1, n):
    wt[i] = wt[i-1] + processes[i-1][1]

for i in range(n):
    tat[i] = wt[i] + processes[i][1]

print("\nProcess\tBT\tWT\tTAT")

for i in range(n):
    pid, bt = processes[i]
    print(f"P{pid}\t{bt}\t{wt[i]}\t{tat[i]}")

print("\nAverage Waiting Time:", sum(wt)/n)
print("Average Turnaround Time:", sum(tat)/n)
