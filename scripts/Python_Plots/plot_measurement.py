from method_plot import *
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import Subplot
import numpy as np
import csv # to read the data file

# Read Data --->
# header
head = ['time', 'EpoExtra', 'EpoStdExtra', 'EpoSurface', 
        'EpoStdSurface', 'EpoIntra', 'EpoStdIntra']
# data as dictionary
data = {}
# for unknown reasons for-loops must be in this order
with open('../../data/Data_Epo.txt') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    temp=[]
    for i in range(0,len(head)):
        temp.append([])
    for j in file:
        for i in range(0,len(head)):
            temp[i].append(float(j[i]))

    for i in range(0,len(head)):
        data[head[i]] = temp[i]        
# <--- Read Data
        
# ---> plot
# use plot function
plotwitherrors(data['time'], 'min' ,data['EpoExtra'], 'a Unit' ,data['EpoStdExtra'])
plotwitherrors(data['time'], 'min' ,data['EpoSurface'], 'a Unit' ,data['EpoStdSurface'])
plotwitherrors(data['time'], 'min' ,data['EpoIntra'], 'a Unit' ,data['EpoStdIntra'])


# <--- plot