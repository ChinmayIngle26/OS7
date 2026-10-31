
import psutil
import time
import os

print("System Performance Analysis")
print("----------------------------")

print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

memory = psutil.virtual_memory()

print("Total RAM:", round(memory.total / (1024**3), 2), "GB")
print("Used RAM:", round(memory.used / (1024**3), 2), "GB")
print("Memory Usage:", memory.percent, "%")

print("\nCurrent Process Information")

process = psutil.Process(os.getpid())

print("Process ID:", process.pid)
print("CPU Usage:", process.cpu_percent(interval=1), "%")
print("Memory Usage:",
      round(process.memory_info().rss / (1024**2), 2), "MB")
