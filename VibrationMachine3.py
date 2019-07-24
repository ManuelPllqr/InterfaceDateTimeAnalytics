import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

machine_three = (machines.machineID == 3)

print(machines[machine_three])

fig = plt.figure(1, figsize=(13, 6))
pressureList = (machines[machine_three])['vibration'].tolist()
datetimeList = (machines[machine_three])['datetime'].tolist()
machineList = (machines[machine_three])['machineID'].tolist()
plt.plot(datetimeList, pressureList, label='Pressure',
         color='k', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=2)
plt.xlabel('Date & time')
plt.ylabel('Vibration')
plt.legend(loc='lower right')
plt.title('Vibration measure machine 3')
plt.xticks(size=4, rotation=45)

plt.show()
#machines.head