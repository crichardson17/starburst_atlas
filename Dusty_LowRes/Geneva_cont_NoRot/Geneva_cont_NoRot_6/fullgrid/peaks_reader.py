import csv
import matplotlib.pyplot as plt
from numpy import *
import scipy.interpolate
import math 
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.patches as patches
from matplotlib.path import Path
import os
# ---------------------------------------------------
print "Starting"
numFiles = 3
gridfile = [None]*numFiles
Elines = [None]*numFiles

for i in range(3):
	for file in os.listdir('.'):
		if file.endswith("Geneva_cont_NoRot_6_{:d}.grd".format(i+1)):
			gridfile[i] = file
			print file
		if file.endswith("Geneva_cont_6_{:d}.txt".format(i+1)):
			Elines[i] = file
			print file

# ---------------------------------------------------
#this is where the grid information (phi and hdens) is read in and saved to grid. 
grid1 = [];
grid2 = [];
grid3 = [];


with open(gridfile[0], 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		grid1.append(row);
	grid1  = asarray(grid1)
with open(gridfile[1], 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		grid2.append(row);
	grid2  = asarray(grid2)
with open(gridfile[2], 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		grid3.append(row);
	grid3  = asarray(grid3)

#here is where the data for each line is read in and saved to dataEmissionlines

dataEmissionlines1 = [];
dataEmissionlines2 = [];
dataEmissionlines3 = [];

with open(Elines[0], 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		dataEmissionlines1.append(row);		
	dataEmissionlines1  = asarray(dataEmissionlines1)

with open(Elines[1], 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers2 = csvReader.next()
	for row in csvReader:
		dataEmissionlines2.append(row);		
	dataEmissionlines2  = asarray(dataEmissionlines2)

with open(Elines[2], 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers3 = csvReader.next()
	for row in csvReader:
		dataEmissionlines3.append(row);		
	dataEmissionlines3  = asarray(dataEmissionlines3)
print "import files complete"
# ---------------------------------------------------
#for concatenating grid

#pull the phi and hdens values from each of the runs. exclude header lines 
grid1new = zeros((len(grid1[:,0])-1,2))
grid1new[:,0] = grid1[1:,6]
grid1new[:,1] = grid1[1:,7]

grid2new = zeros((len(grid2[:,0])-1,2))
x = array(17.00000)
grid2new[:,0]  = repeat(x,len(grid2[:,0])-1)
grid2new[:,1] = grid2[1:,6]

grid3new = zeros((len(grid3[:,0])-1,2))
grid3new[:,0] = grid3[1:,6]
grid3new[:,1] = grid3[1:,7]

grid = concatenate((grid1new,grid2new,grid3new))
hdens_values = grid[:,1]
phi_values = grid[:,0]

Emissionlines = concatenate((dataEmissionlines1[:,1:],dataEmissionlines2[:,1:],dataEmissionlines3[:,1:]))
headers = headers[1:]
# ---------------------------------------------------

# ---------------------------------------------------

#To fix when hdens > 10

hdens_values_2 = empty(shape=[0, 1])
phi_values_2 = empty(shape=[0, 1])
Emissionlines_2 = empty(shape=[0, len(Emissionlines[0,:])])

for i in range(len(hdens_values)):
	if float(hdens_values[i]) < 10.100 : 
		hdens_values_2 = append(hdens_values_2, hdens_values[i])
		phi_values_2 = append(phi_values_2, phi_values[i])
		Emissionlines_2 = vstack([Emissionlines_2, Emissionlines[i,:]])

#overwrite old arrays
hdens_values = hdens_values_2
phi_values = phi_values_2
Emissionlines = Emissionlines_2


concatenated_data = zeros((len(Emissionlines),len(Emissionlines[0])))
max_values = zeros((len(concatenated_data[0]),4))
# ---------------------------------------------------
#constructing grid by scaling 

#select the scaling factor
#for 1215
#incident = Emissionlines[1:,4] 

#for 4860
incident = concatenated_data[:,57] 

#take the ratio of incident and all the lines and put it all in an array concatenated_data
for i in range(len(Emissionlines)):
	for j in range(len(Emissionlines[0])):
			if math.log(4860.*(float(Emissionlines[i,j])/float(Emissionlines[i,57])), 10) > 0:
				concatenated_data[i,j] = math.log(4860.*(float(Emissionlines[i,j])/float(Emissionlines[i,57])), 10)
			else:
				concatenated_data[i,j] == 0

# for 1215
#for i in range(len(Emissionlines)):
#	for j in range(len(Emissionlines[0])):
#			if math.log(1215.*(float(Emissionlines[i,j])/float(Emissionlines[i,4])), 10) > 0:
#				concatenated_data[i,j] = math.log(1215.*(float(Emissionlines[i,j])/float(Emissionlines[i,4])), 10)
#			else:
#				concatenated_data[i,j] == 0

# ---------------------------------------------------

#find the maxima to plot onto the contour plots
for j in range(len(concatenated_data[0])):
	max_values[j,0] = max(concatenated_data[:,j])
	max_values[j,1] = argmax(concatenated_data[:,j], axis = 0)
	max_values[j,2] = hdens_values[max_values[j,1]]
	max_values[j,3] = phi_values[max_values[j,1]]

#to round off the maxima 
max_values[:,0] = [ '%.1f' % elem for elem in max_values[:,0] ]
print "peaks pulled"

# ---------------------------------------------------

#Creating the grid to interpolate with for contours. 
gridarray = zeros((len(concatenated_data),2))
gridarray[:,0] = hdens_values
gridarray[:,1] = phi_values

x = gridarray[:,0]
y = gridarray[:,1]

# ---------------------------------------------------
savetxt('peaks', max_values, delimiter='\t')
print "peaks saved"




