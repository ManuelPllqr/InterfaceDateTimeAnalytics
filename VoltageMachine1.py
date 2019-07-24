import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

machine_one = (machines.machineID == 1)

print(machines[machine_one])

fig = plt.figure(1, figsize=(13, 6))
voltList = (machines[machine_one])['volt'].tolist()
datetimeList = (machines[machine_one])['datetime'].tolist()
machineList = (machines[machine_one])['machineID'].tolist()
plt.plot(datetimeList, voltList, label='Voltage',
         color='r', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=2)
plt.xlabel('Date & time')
plt.ylabel('Volt')
plt.legend(loc='lower right')
plt.title('Voltage measure machine 1')
plt.xticks(size=4, rotation=45)

plt.show()
#machines.head()

