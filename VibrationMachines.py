import pandas as pd
import matplotlib.pyplot as plt

machines = pd.read_csv("MachineData.csv")

machine_one = (machines.machineID == 1)
machine_two = (machines.machineID == 2)
machine_three = (machines.machineID == 3)
machine_four = (machines.machineID == 4)
machine_five = (machines.machineID == 5)

fig = plt.figure(1, figsize=(13, 6))

vibrationList1 = (machines[machine_one])['vibration'].tolist()
datetimeList1 = (machines[machine_one])['datetime'].tolist()
plt.plot(datetimeList1, vibrationList1, label='Machine 1',
         color='r', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

vibrationList2 = (machines[machine_two])['vibration'].tolist()
datetimeList2 = (machines[machine_two])['datetime'].tolist()
plt.plot(datetimeList2, vibrationList2, label='Machine 2',
         color='g', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

vibrationList3 = (machines[machine_three])['vibration'].tolist()
datetimeList3 = (machines[machine_three])['datetime'].tolist()
plt.plot(datetimeList3, vibrationList3, label='Machine 3',
         color='k', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)


vibrationList4 = (machines[machine_four])['vibration'].tolist()
datetimeList4 = (machines[machine_four])['datetime'].tolist()
plt.plot(datetimeList4, vibrationList4, label='Machine 4',
         color='y', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

vibrationList5 = (machines[machine_five])['vibration'].tolist()
datetimeList5 = (machines[machine_five])['datetime'].tolist()
plt.plot(datetimeList5, vibrationList5, label='Machine 5',
         color='c', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)

plt.xlabel('Date & time')
plt.ylabel('Vibration')
plt.legend(loc='lower right')
plt.title('Vibration measure per machine')
plt.xticks(size=4, rotation=45)

plt.show()

