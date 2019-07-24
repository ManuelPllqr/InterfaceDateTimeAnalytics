import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")

machine_one = (machines.machineID == 1)
machine_two = (machines.machineID == 2)
machine_three = (machines.machineID == 3)
machine_four = (machines.machineID == 4)
machine_five = (machines.machineID == 5)

fig = plt.figure(1, figsize=(13, 6))

rotateList1 = (machines[machine_one])['rotate'].tolist()
datetimeList1 = (machines[machine_one])['datetime'].tolist()
plt.plot(datetimeList1, rotateList1, label='Machine 1',
         color='r', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

rotateList2 = (machines[machine_two])['rotate'].tolist()
datetimeList2 = (machines[machine_two])['datetime'].tolist()
plt.plot(datetimeList2, rotateList2, label='Machine 2',
         color='g', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

rotateList3 = (machines[machine_three])['rotate'].tolist()
datetimeList3 = (machines[machine_three])['datetime'].tolist()
plt.plot(datetimeList3, rotateList3, label='Machine 3',
         color='k', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)


rotateList4 = (machines[machine_four])['rotate'].tolist()
datetimeList4 = (machines[machine_four])['datetime'].tolist()
plt.plot(datetimeList4, rotateList4, label='Machine 4',
         color='y', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

rotateList5 = (machines[machine_five])['rotate'].tolist()
datetimeList5 = (machines[machine_five])['datetime'].tolist()
plt.plot(datetimeList5, rotateList5, label='Machine 5',
         color='c', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

plt.xlabel('Date & time')
plt.ylabel('Rotate')
plt.legend(loc='lower right')
plt.title('Rotate measure per machine')
plt.xticks(size=4, rotation=45)

plt.show()

