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
headerloc = "/Users/helen/Documents/Elon/Thesis_Research/github_repo/starburst_atlas/headers_dir/headers.txt"
# ------------------------------------------------------------------------------------------------------

#data files' names from source directory constructed here. default source directory is working directory
numFiles = 3 #change this if you have more/less files
gridFiles = [None]*numFiles
emissionFiles = [None]*numFiles

for i in range(numFiles):
	for file in os.listdir('.'):
		if file.endswith("padova_cont_2_{:d}.grd".format(i+1)):
			gridFiles[i] = file
			#keep track of all the files you'll be importing by printing 
			#print file
		if file.endswith("padova_cont_2_{:d}.txt".format(i+1)):
			emissionFiles[i] = file
			#keep track of all the files you'll be importing by printing 
			#print file
print ("Files names constructed")

# ---------------------------------------------------
#this is where the grid information (phi and hdens) is read in and saved to grid. 
print("Beginning file import")
for i in range(numFiles):
	gridI = [];
	with open(gridFiles[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		for row in csvReader:
			gridI.append(row)
	gridI = asarray(gridI)
	gridI = gridI[1:,6:8]
	if ( i == 0 ):
		grid = gridI
	else :
		grid = concatenate((grid,gridI))

for i in range(numFiles):
	emissionLineI = [];
	with open(emissionFiles[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		headers = csvReader.next()
		for row in csvReader:
			emissionLineI.append(row)
	emissionLineI = asarray(emissionLineI)
	emissionLineI = emissionLineI[:,1:]
	if ( i == 0 ):
		Emissionlines = emissionLineI
	else :
		Emissionlines = concatenate((Emissionlines,emissionLineI))

hdens_values = grid[:,1]
phi_values = grid[:,0]
print("Import files complete")

#To fix when hdens > 10 
#many of my grids were run off with hdens up to 12 so we needed to cut off part of the data 
#first create temorary arrays 

print("modifications begun")

hdens_values_2 = empty(shape=[0, 1])
phi_values_2 = empty(shape=[0, 1])
Emissionlines_2 = empty(shape=[0, len(Emissionlines[0,:])])

#save data in range desired to temp arrays
for i in range(len(hdens_values)):
	if (float(hdens_values[i]) < 6.100) & (float(phi_values[i]) < 17.100) : 
		hdens_values_2 = append(hdens_values_2, hdens_values[i])
		phi_values_2 = append(phi_values_2, phi_values[i])
		Emissionlines_2 = vstack([Emissionlines_2, Emissionlines[i,:]])

#overwrite old arrays
hdens_values = hdens_values_2
phi_values = phi_values_2
Emissionlines = Emissionlines_2
print("modifications complete")
# ---------------------------------------------------
# ---------------------------------------------------
#there are the emission line names properly formatted
print("Importing headers from header file")
headersFile = open(headerloc,'r')
headers = headersFile.read().splitlines()
headersFile.close()
# ---------------------------------------------------
#constructing grid by scaling 

#select the scaling factor
#for 1215
#incident = Emissionlines[1:,4] 
concatenated_data = zeros((len(Emissionlines),len(Emissionlines[0])))
max_values = zeros((len(concatenated_data[0]),4))

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
print "data arranged"

# ---------------------------------------------------

#Creating the grid to interpolate with for contours. 
gridarray = zeros((len(concatenated_data),2))
gridarray[:,0] = hdens_values
gridarray[:,1] = phi_values

x = gridarray[:,0]
y = gridarray[:,1]

# ---------------------------------------------------
savetxt('peaks_Padova_cont_2', max_values, delimiter='\t')




