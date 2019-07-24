import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource

machines = pd.read_csv("MachineData.csv")
machines.head()
machines.shape
print(machines)

"""type(False)

booleans = []

for l in machines.machineID:
    if l == 1:
        booleans.append(True)
    else:
        booleans.append(False)

print(booleans[0:5])"""


"""type(False)
booleans = []
for number in machines.machineID:
    if number == 1:
        booleans.append(True)
    else:
        booleans.append(False)
print(booleans[0:5])
print(len(booleans))

machine_one = pd.Series(booleans)

"""
machine_one = (machines.machineID == 2)
#print(machine_one.head())
print(machines[machine_one])
#print(machine_one)
fig = plt.figure(1, figsize=(13, 6))
voltList = (machines[machine_one])['volt'].tolist()
datetimeList = (machines[machine_one])['datetime'].tolist()
machineList = (machines[machine_one])['machineID'].tolist()
plt.plot(datetimeList, voltList, label='Voltage',
         color='g', marker='o', markerfacecolor='k',
         linestyle='-', linewidth=3)
plt.xlabel('Date & time')
plt.ylabel('Volt')
plt.legend(loc='lower right')
plt.title('Voltage measure machine 2')

plt.xticks(size=4, rotation=45)
plt.show()
#machines.head()
