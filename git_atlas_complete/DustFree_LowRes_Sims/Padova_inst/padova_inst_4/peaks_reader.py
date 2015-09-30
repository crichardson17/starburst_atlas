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
#input files
for file in os.listdir('.'):
    if file.endswith(".grd"):
    	inputfile = file

for file in os.listdir('.'):
    if file.endswith(".txt"):
    	inputfile2 = file
#this is where the grid information (phi and hdens) is read in and saved to grid. 
grid = [];
with open(inputfile, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		grid.append(row);
	grid  = asarray(grid)
# ---------------------------------------------------

#here is where the data for each line is read in and saved to dataEmissionlines
dataEmissionlines = [];
with open(inputfile2, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		dataEmissionlines.append(row);		
	dataEmissionlines  = asarray(dataEmissionlines)
print "import files complete"
# ---------------------------------------------------
#for grid
phi_values = grid[1:len(dataEmissionlines)+1,6]
hdens_values = grid[1:len(dataEmissionlines)+1,7]

#for lines
headers = headers[1:]
Emissionlines = dataEmissionlines[:, 1:]
concatenated_data = zeros((len(Emissionlines),len(Emissionlines[0])))
max_values = zeros((len(Emissionlines[0]),4))

#select the scaling factor

#for 1215
#incident = Emissionlines[1:,4] 

#for 4860
incident = Emissionlines[:,57] 

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


#find the maxima to plot onto the contour plots
for j in range(len(concatenated_data[0])):
	max_values[j,0] = max(concatenated_data[:,j])
	max_values[j,1] = argmax(concatenated_data[:,j], axis = 0)
	max_values[j,2] = hdens_values[max_values[j,1]]
	max_values[j,3] = phi_values[max_values[j,1]]

#to round off the maxima 
max_values[:,0] = [ '%.1f' % elem for elem in max_values[:,0] ]

savetxt('peaks', max_values, delimiter='\t')




