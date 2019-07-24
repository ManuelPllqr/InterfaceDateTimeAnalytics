import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

machine_five = (machines.machineID == 5)

print(machines[machine_five])

fig = plt.figure(1, figsize=(13, 6))
RotateList = (machines[machine_five])['rotate'].tolist()
datetimeList = (machines[machine_five])['datetime'].tolist()
machineList = (machines[machine_five])['machineID'].tolist()
plt.plot(datetimeList, RotateList, label='Rotate',
         color='c', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=2)
plt.xlabel('Date & time')
plt.ylabel('Rotate')
plt.legend(loc='lower right')
plt.title('Rotate measure machine 5')
plt.xticks(size=4, rotation=45)

plt.show()
#machines.head()