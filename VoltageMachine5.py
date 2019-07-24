import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button


plt.subplot(1, 1, 1)
machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

machine_one = (machines.machineID == 5)
#datet = (machines.datetime == "1:00:00")
#print(machine_one.head())
print(machines[machine_one])
#print(machine_one)
fig = plt.figure(1, figsize=(13, 6))
voltList = (machines[machine_one])['volt'].tolist()

datetimeList = (machines[machine_one])['datetime'].tolist()
machineList = (machines[machine_one])['machineID'].tolist()
plt.plot(datetimeList, voltList, label='Voltage',
         color='c', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)
plt.xlabel('Date & time')
plt.ylabel('Volt')
plt.legend(loc='lower right')
plt.title('Voltage measure machine 5')

#plt.xticks([])

plt.xticks(size=4, rotation=45)

"""
plt.subplots_adjust(bottom=0.4)

bxbox=plt.axes([0.14, 0.15, 0.25, 0.06])
axbox=plt.axes([0.65, 0.15, 0.25, 0.06])
#confirmbox=plt.axes([0.35, 0.08, 0.3, 0.06])
text_box = TextBox(axbox, 'Start date', initial="xxxx-xx-xx 00:00:00")
text_box = TextBox(bxbox, 'End date', initial="xxxx-xx-xx 00:00:00")
#text_box = TextBox(confirmbox, 'End date', initial="xxxx-xx-xx 00:00:00")

button1 = plt.axes([0.35, 0.08, 0.3, 0.06])
b1 = Button(ax=button1,
            label='Confirm time',
            color='red',
            hovercolor='blue')"""

plt.show()
#machines.head()
