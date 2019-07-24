import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

machine_four = (machines.machineID == 4)

print(machines[machine_four])

fig = plt.figure(1, figsize=(13, 6))
RotateList = (machines[machine_four])['rotate'].tolist()
datetimeList = (machines[machine_four])['datetime'].tolist()
machineList = (machines[machine_four])['machineID'].tolist()
plt.plot(datetimeList, RotateList, label='Rotate',
         color='y', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=2)
plt.xlabel('Date & time')
plt.ylabel('Rotate')
plt.legend(loc='lower right')
plt.title('Rotate measure machine 4')
plt.xticks(size=4, rotation=45)

plt.show()
#machines.head()