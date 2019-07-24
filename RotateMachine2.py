import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

machine_two = (machines.machineID == 2)

print(machines[machine_two])

fig = plt.figure(1, figsize=(13, 6))
RotateList = (machines[machine_two])['rotate'].tolist()
datetimeList = (machines[machine_two])['datetime'].tolist()
machineList = (machines[machine_two])['machineID'].tolist()
plt.plot(datetimeList, RotateList, label='Rotate',
         color='g', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=2)
plt.xlabel('Date & time')
plt.ylabel('Rotate')
plt.legend(loc='lower right')
plt.title('Rotate measure machine 2')
plt.xticks(size=4, rotation=45)

plt.show()
#machines.head()