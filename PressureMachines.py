import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")

machine_one = (machines.machineID == 1)
machine_two = (machines.machineID == 2)
machine_three = (machines.machineID == 3)
machine_four = (machines.machineID == 4)
machine_five = (machines.machineID == 5)

fig = plt.figure(1, figsize=(13, 6))

pressureList1 = (machines[machine_one])['pressure'].tolist()
datetimeList1 = (machines[machine_one])['datetime'].tolist()
plt.plot(datetimeList1, pressureList1, label='Machine 1',
         color='r', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

pressureList2 = (machines[machine_two])['pressure'].tolist()
datetimeList2 = (machines[machine_two])['datetime'].tolist()
plt.plot(datetimeList2, pressureList2, label='Machine 2',
         color='g', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

pressureList3 = (machines[machine_three])['pressure'].tolist()
datetimeList3 = (machines[machine_three])['datetime'].tolist()
plt.plot(datetimeList3, pressureList3, label='Machine 3',
         color='k', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)


pressureList4 = (machines[machine_four])['pressure'].tolist()
datetimeList4 = (machines[machine_four])['datetime'].tolist()
plt.plot(datetimeList4, pressureList4, label='Machine 4',
         color='y', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

pressureList5 = (machines[machine_five])['pressure'].tolist()
datetimeList5 = (machines[machine_five])['datetime'].tolist()
plt.plot(datetimeList5, pressureList5, label='Machine 5',
         color='c', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

plt.xlabel('Date & time')
plt.ylabel('Pressure')
plt.legend(loc='lower right')
plt.title('Pressure measure per machine')
plt.xticks(size=4, rotation=45)

plt.show()

