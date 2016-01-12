############################################################
##### Plotting File for No Column density simulations ######
################## Data read from Cloudy ###################
################ Helen Meskhidze, Fall 2015 ################
#################### Elon University #######################
#------------------------------------------------------------------------------------------------------
'''
The inputs this code takes are .grd and .txt files from Cloudy
It can take in as many input files (in case you have a grid and haven't concatenated all the files)- just change the numFiles value 
This code outputs a set of contour plots, saved to the working directory
'''
#Imports
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
import time

# ------------------------------------------------------------------------------------------------------
# keep track of how long the code takes to run 
t0 = time.clock()
headerloc = "/Users/helen/Documents/git_atlas_complete/headers_dir/headers.txt"
# ------------------------------------------------------------------------------------------------------
#input data files loaded in here

# ------------------------------------------------------------------------------------------------------
#inputs
for file in os.listdir('.'):
    if file.endswith("1.grd"):
    	gridfile1 = file

for file in os.listdir('.'):
    if file.endswith("2.grd"):
    	gridfile2 = file

for file in os.listdir('.'):
    if file.endswith("3.grd"):
    	gridfile3 = file
# ------------------------

for file in os.listdir('.'):
    if file.endswith("1.txt"):
    	Elines1 = file

for file in os.listdir('.'):
    if file.endswith("2.txt"):
    	Elines2 = file

for file in os.listdir('.'):
    if file.endswith("3.txt"):
    	Elines3 = file
    	 	
# ------------------------------------------------------------------------------------------------------
#Patches data
#this section adds the rectangles on the plots of the three other studies 
#for the Kewley and Levesque data
verts = [
    (1., 7.97712125471966000000), # left, bottom
    (1., 9.57712125471966000000), # left, top
    (2., 10.57712125471970000000), # right, top
    (2., 8.97712125471966000000), # right, bottom
    (0., 0.), # ignored
    ]
codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]
path = Path(verts, codes)

#for the Kewley 01 data
verts2 = [
    (2.4, 9.243038049), # left, bottom
    (2.4, 11.0211893), # left, top
    (2.6, 11.0211893), # right, top
    (2.6, 9.243038049), # right, bottom
    (0, 0.), # ignored
    ]
path = Path(verts, codes)
path2 = Path(verts2, codes)

#for the  Moy et al data
verts3 = [
    (1., 6.86712125471966000000), # left, bottom
    (1., 10.18712125471970000000), # left, top
    (3., 12.18712125471970000000), # right, top
    (3., 8.86712125471966000000), # right, bottom
    (0., 0.), # ignored
    ]
path = Path(verts, codes)
path3 = Path(verts3, codes)
# ------------------------------------------------------------------------------------------------------
#the routine to add patches for others peoples' data onto our plots. 
def add_patches(ax):
	patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
	patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
	patch = patches.PathPatch(path, facecolor='red', lw=0)
	ax1.add_patch(patch3)
	ax1.add_patch(patch2)
	ax1.add_patch(patch)
# ------------------------------------------------------------------------------------------------------
plt.figure(figsize=(13,10))

#the add subplot routine
def add_sub_plot(sub_num, elinesplot):
	numplots = 16
	plt.subplot(numplots/4.,4,sub_num) #define rows and columns by desired amount of subplots
	
	rbf = scipy.interpolate.Rbf(x, y, z[elinesplot][:,sub_num-1], function='linear')
	zi = rbf(xi, yi)
	
	contour = plt.contour(xi,yi,zi, levels, colors='c', linestyles = 'dashed') #teal contours, dashed
	contour2 = plt.contour(xi,yi,zi, levels2, colors='k', linewidths=1.5) #black contours, solid
	
	plt.scatter(max_values[line[elinesplot][sub_num-1],2], max_values[line[elinesplot][sub_num-1],3], c ='k',marker = '*')
	plt.annotate(headers[line[elinesplot][sub_num-1]], xy=(8,11),  xytext=(6,8.5), fontsize = 10)
	plt.annotate(max_values[line[elinesplot][sub_num-1],0], xy = (max_values[line[elinesplot][sub_num-1],2], max_values[line[elinesplot][sub_num-1],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	
	if sub_num == numplots / 2.:
		print "half the plots are complete"
#axis limits

	yt_min = 8
	yt_max = 21
	xt_min = 0
	xt_max = 10
	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min+1,yt_max,1),fontsize=10)
	plt.xticks(arange(xt_min+1,xt_max,1), fontsize = 10)
	#here we make sure we have all the correct axes labeled. 
	if sub_num in [2,3,4,6,7,8,10,11,12,14,15,16]:
		plt.tick_params(labelleft = 'off')
	else:
		plt.tick_params(labelleft = 'on')
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
	
	if sub_num in [1,2,3,4,5,6,7,8,9,10,11,12]:
		plt.tick_params(labelbottom = 'off')
	else: 		
		plt.tick_params(labelbottom = 'on')
		plt.xlabel('Log($n _{\mathrm{H}}  $)')

	if sub_num == 1:
		plt.yticks(arange(yt_min+1,yt_max+1,1),fontsize=10)
	if sub_num == 13:
		plt.yticks(arange(yt_min,yt_max,1),fontsize=10)
		plt.xticks(arange(xt_min,xt_max,1), fontsize = 10)
	if sub_num == 16 :
		plt.xticks(arange(xt_min+1,xt_max+1,1), fontsize = 10)
# ---------------------------------------------------
#this is where the grid information (phi and hdens) is read in and saved to grid. 
#Dusty sim
grid1 = [];
grid2 = [];
grid3 = [];

with open(gridfile1, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		grid1.append(row);
	grid1  = asarray(grid1)
with open(gridfile2, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		grid2.append(row);
	grid2  = asarray(grid2)
with open(gridfile3, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		grid3.append(row);
	grid3  = asarray(grid3)

#here is where the data for each line is read in and saved to dataEmissionlines
dataEmissionlines1 = [];
dataEmissionlines2 = [];
dataEmissionlines3 = [];

with open(Elines1, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		dataEmissionlines1.append(row);		
	dataEmissionlines1  = asarray(dataEmissionlines1)

with open(Elines2, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers2 = csvReader.next()
	for row in csvReader:
		dataEmissionlines2.append(row);		
	dataEmissionlines2  = asarray(dataEmissionlines2)

with open(Elines3, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers3 = csvReader.next()
	for row in csvReader:
		dataEmissionlines3.append(row);		
	dataEmissionlines3  = asarray(dataEmissionlines3)
print "import files complete"
# ---------------------------------------------------
#for grid
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

grid = concatenate((grid1new,grid2new, grid3new))
hdens_values = grid[:,1]
phi_values = grid[:,0]

#for concatenating Emission lines data
Emissionlines = concatenate((dataEmissionlines1[:,1:],dataEmissionlines2[:,1:], dataEmissionlines3[:,1:]))

# ---------------------------------------------------
#To fix when hdens > 10 
#many of my grids were run off with hdens up to 12 so we needed to cut off part of the data 
#first create temorary arrays 
print("modifications begun")
hdens_values_2 = empty(shape=[0, 1])
phi_values_2 = empty(shape=[0, 1])
Emissionlines_2 = empty(shape=[0, len(Emissionlines[0,:])])

#save data in range desired to temp arrays
for i in range(len(hdens_values)):
	if float(hdens_values[i]) < 10.100 : 
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


concatenated_data = zeros((len(Emissionlines),len(Emissionlines[0])))
max_values = zeros((len(concatenated_data[0]),4))

#select the scaling factor

#for 1215
#incident = Emissionlines[1:,4] 

#for 4860
incident = Emissionlines[:,58] 

#take the ratio of incident and all the lines and put it all in an array concatenated_data
for i in range(len(Emissionlines)):
	for j in range(len(Emissionlines[0])):
			if math.log(4860.*(float(Emissionlines[i,j])/float(Emissionlines[i,58])), 10) > 0:
				concatenated_data[i,j] = math.log(4860.*(float(Emissionlines[i,j])/float(Emissionlines[i,58])), 10)
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
print "data arranged"

# ---------------------------------------------------

#Creating the grid to interpolate with for contours. 
gridarray = zeros((len(Emissionlines),2))
gridarray[:,0] = hdens_values
gridarray[:,1] = phi_values

x = gridarray[:,0]
y = gridarray[:,1]

#change desired lines here!
line = [
		#UV1Lines
	[0, 1, 2, 5, 165, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17],
	#977, 991, 1026, 1216, 1218, 1239, 1240, 1243, 1263, 1304, 1308, 1397, 1402, 1406, 1486, 1531

		#UV2line 
	[18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34],
	#1549, 1640, 1665, 1671, 1750, 1860, 1888, 1907, 2297, 2321, 2471, 2326, 2335, 2665, 2798
		
		#Optical Lines
	[36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
	#NE 3  3343A, NE 5  3426, 3646, 3726, 3727, 3729, 3869, 3889, 3933, 4026, 4070, 4074, 4078, 4102, 4340, 4363

		#Optical Lines 2
	[56, 57, 59, 60, 61, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74],
	#NE 4  4720A, AR 4  4740, 4861, O III 4959, O  3  5007, O  1  5577, N  2  5755, HE 1  5876, O  1  6300;
	#S  3  6312, O  1  6363, H  1  6563, N  2  6584, S II  6716, S  2  6720, S II  6731
		
		#IR Lines
	[75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
	#AR 5  7005A, AR 3  7135A, TOTL  7325A, AR 3  7751, 6LEV  8446, CA2X  8498, CA2Y  8542, CA2Z  8662; 
	#CA 2  8579A, S  3  9069, H  1  9229, S  3  9532... H  1  9546

		#Rest Lines
	[3,4,15,22,37,53,54,55,58,63,78,89,90,91,93,94],

		#More Lines
	[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112],

		#More Lines 2
	[113,114,115,116,117,118,119,120,121,122,123,124,125,126,127]
] 

#create z array for this plot
z = [concatenated_data[:,line[0]],concatenated_data[:,line[1]], concatenated_data[:,line[2]], concatenated_data[:,line[3]], concatenated_data[:,line[4]], concatenated_data[:,line[5]], concatenated_data[:,line[6]], concatenated_data[:,line[7]]]
#z1 = concatenated_data[:,line[1]]

# ---------------------------------------------------
# Interpolate
print "starting interpolation"
xi, yi = linspace(x.min(), x.max(), 10), linspace(y.min(), y.max(), 10) 
xi, yi = meshgrid(xi, yi)
# ---------------------------------------------------
print "interpolatation complete; now plotting"
#plot
plt.subplots_adjust(wspace=0, hspace=0) #remove space between plots
levels = arange(10**-1,10, .2)
levels2 = arange(10**-2,10**2, 1)
# ---------------------------------------------------
for j in range (8):
	plt.clf()
	for i in range(16):
		add_sub_plot(i,j)
	ax1 = plt.subplot(4,4,1)
	add_patches(ax1)

	print "complete"
	plt.savefig(("Full_lines_%d.pdf") % j)
	plt.clf()
# ---------------------------------------------------

if (time.clock() - t0) > 120:
	print((time.clock() - t0)/60., "minutes process time")
else: 
	print(time.clock() - t0, "seconds process time")

