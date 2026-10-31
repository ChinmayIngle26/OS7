
n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for P{i+1}: "))
    processes.append(bt)

wt = [0] * n
tat = [0] * n

for i in range(1, n):
    wt[i] = wt[i-1] + processes[i-1]

for i in range(n):
    tat[i] = wt[i] + processes[i]

print("\nProcess\tBT\tWT\tTAT")

for i in range(n):
    print(f"P{i+1}\t{processes[i]}\t{wt[i]}\t{tat[i]}")

print("\nAverage Waiting Time:", sum(wt)/n)
print("Average Turnaround Time:", sum(tat)/n)
