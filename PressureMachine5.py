import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

machine_five = (machines.machineID == 1)

print(machines[machine_five])

fig = plt.figure(1, figsize=(13, 6))
pressureList = (machines[machine_five])['pressure'].tolist()
datetimeList = (machines[machine_five])['datetime'].tolist()
machineList = (machines[machine_five])['machineID'].tolist()
plt.plot(datetimeList, pressureList, label='Pressure',
         color='c', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=2)
plt.xlabel('Date & time')
plt.ylabel('Pressure')
plt.legend(loc='lower right')
plt.title('Pressure measure machine 5')
plt.xticks(size=4, rotation=45)

plt.show()
#machines.head