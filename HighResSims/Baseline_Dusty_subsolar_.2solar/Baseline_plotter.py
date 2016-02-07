############################################################
############# Plotting File for Contour Plots ##############
################## Data read from Cloudy ###################
################ Helen Meskhidze, Fall 2015 ################
#################### Elon University #######################
#------------------------------------------------------------------------------------------------------
'''
The inputs this code takes are .grd and .txt files from Cloudy. 
It can take in as many input files (in case you have a grid and haven't concatenated all the files)- just change the numFiles value 
This code outputs a set of contour plots, saved to the working directory
'''
#------------------------------------------------------------------------------------------------------
#Packages importing
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
headerloc = "/Users/helen/Documents/Thesis_Research/github_repo/starburst_atlas/headers_dir/headers.txt"
# ------------------------------------------------------------------------------------------------------

#data files' names from source directory constructed here. default source directory is working directory
numFiles = 8 #change this if you have more/less files
gridFiles = [None]*numFiles
emissionFiles = [None]*numFiles

for i in range(numFiles):
	for file in os.listdir('.'):
		if file.endswith("{:d}_subsolar_highres.2.grd".format(i+1)):
			gridFiles[i] = file
			#keep track of all the files you'll be importing by printing 
			print file
		if file.endswith("5_{:d}_subsolar_highres.2emissionlines_abs.txt".format(i+1)):
			emissionFiles[i] = file
			#keep track of all the files you'll be importing by printing 
			print file
print ("Files names constructed")
# ------------------------------------------------------------------------------------------------------
#Patches data
#this section adds the rectangles on the plots of the three other studies 
#for the Kewley and Levesque data
verts = [
    (1., 7.97712125471966000000), # left, bottom
    (1., 9.57712125471966000000), # left, top
    (2., 10.57712125471970000000), # right, top
    (2., 8.97712125471966000000), # right, bottom
    (0., 0.)] # ignored
codes = [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.CLOSEPOLY]
path = Path(verts, codes)
#for the Kewley 01 data
verts2 = [
    (2.4, 9.243038049), # left, bottom
    (2.4, 11.0211893), # left, top
    (2.6, 11.0211893), # right, top
    (2.6, 9.243038049), # right, bottom
    (0, 0.)] # ignored
path = Path(verts, codes)
path2 = Path(verts2, codes)
#for the  Moy et al data
verts3 = [
    (1., 6.86712125471966000000), # left, bottom
    (1., 10.18712125471970000000), # left, top
    (3., 12.18712125471970000000), # right, top
    (3., 8.86712125471966000000), # right, bottom
    (0., 0.)] # ignored 
path = Path(verts, codes)
path3 = Path(verts3, codes)
# ------------------------------------------------------------------------------------------------------
#the patches routine: to add patches for others peoples' data onto our plots. 
#Adds patches to the first subplot
def add_patches(ax):
	patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
	patch2 = patches.PathPatch(path2, facecolor='blue', lw=0)
	patch = patches.PathPatch(path, facecolor='grey', lw=0)
	ax1.add_patch(patch3)
	ax1.add_patch(patch2)
	ax1.add_patch(patch)
# ------------------------------------------------------------------------------------------------------
#the subplot routine
plt.figure(figsize=(12,10))

def add_sub_plot(sub_num, elinesplot):
	numplots = 16
	plt.subplot(numplots/4.,4,sub_num) #row, column
	
	#choose which z array, then which subplot
	z_subnum = z_total[elinesplot]
	z_line = z_subnum[:,:,sub_num-1]
	
	contour1 = plt.contour(x_axis, y_axis, z_line, levels, colors='k', origin='lower', extent=extent) #teal contours, dashed
	contourmap = plt.imshow(z_line, cmap='Reds', extent= extent, aspect = "auto",origin='lower', vmin=0, vmax =4)

	plt.scatter(max_values[line[elinesplot][sub_num-1],2], max_values[line[elinesplot][sub_num-1],3], c ='k',marker = '*')
	plt.annotate(headers[line[elinesplot][sub_num-1]], xy=(8,11),  xytext=(4,8.5), fontsize = 10)
	
	plt.annotate(max_values[line[elinesplot][sub_num-1],0], xy = (max_values[line[elinesplot][sub_num-1],2], max_values[line[elinesplot][sub_num-1],3]), 
		xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10, color='k')
	if sub_num == 4:
		cb = plt.colorbar(contourmap, pad = 0.05, ticks=np.arange(0,4.5,0.5))
		cb.ax.tick_params(labelsize=10) 
	if sub_num == 8:
		cb = plt.colorbar(contourmap, pad = 0.05, ticks=np.arange(0,4.0,0.5))
		cb.ax.tick_params(labelsize=10) 	
	if sub_num == 12:
		cb = plt.colorbar(contourmap, pad = 0.05, ticks=np.arange(0,4.0,0.5))
		cb.ax.tick_params(labelsize=10) 	
	if sub_num == 0:
		cb = plt.colorbar(contourmap, pad = 0.05, ticks=np.arange(0,4.0,0.5))
		cb.ax.tick_params(labelsize=10) 	
	#if sub_num == (4,8,12,16):
		#axColor = plt.axes([7,7.5,0,0.5])
	
	#axis limits
	yt_min = 8 ; yt_max = 23; xt_min = 0; xt_max = 10 
	plt.ylim(yt_min,yt_max); plt.xlim(xt_min,xt_max) 

	#ticks
	plt.yticks(arange(yt_min+1,yt_max,1),fontsize=10)
	plt.xticks(arange(xt_min+1,xt_max,1), fontsize = 10)
	

	#axes labels 
	if sub_num == 0:
		plt.tick_params(labelbottom = 'on')
		plt.xticks(arange(xt_min+1,xt_max+1,1), fontsize = 10)
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
	if sub_num == 12:
		plt.tick_params(labelbottom = 'off')
	if sub_num%(numplots/4) == 1:
		plt.tick_params(labelleft = 'on')
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
	else:
		plt.tick_params(labelleft = 'off')
	if sub_num > 12:
		plt.tick_params(labelbottom = 'on')
		plt.xticks(arange(xt_min,xt_max,1), fontsize = 10)
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
	#else:
	#	plt.tick_params(labelbottom = 'off')
	if sub_num == 1:
		plt.yticks(arange(yt_min+1,yt_max+1,1),fontsize=10)
	if sub_num == 13:
		plt.yticks(arange(yt_min,yt_max,1),fontsize=10)
		plt.xticks(arange(xt_min,xt_max,1), fontsize = 10)
	if sub_num == 16 :
		plt.xticks(arange(xt_min+1,xt_max+1,1), fontsize = 10)
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
		plt.yticks(arange(yt_min+1,yt_max+1,1),fontsize=10)
	
	#to print progress to the terminal
	if sub_num == numplots/2:
		print("half the sub-plots of plot{:d} are complete".format(elinesplot+1))	
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
#there are the emission line names properly formatted
print("Importing headers from header file")
headersFile = open(headerloc,'r')
headers = headersFile.read().splitlines()
headersFile.close()
# ---------------------------------------------------
concatenated_data = zeros((len(Emissionlines),len(Emissionlines[0])))
max_values = zeros((len(concatenated_data[0]),4))

#select the scaling factor
#for 4860
incidentnum = 58 #reference index of 4860
incidentline = 4860. #wavelength
incident = Emissionlines[:,58] 
print("Scaling data")
#take the ratio of incident and all the lines and put it all in an array concatenated_data
for i in range(len(Emissionlines)):
	for j in range(len(Emissionlines[0])):
			if math.log(incidentline*(float(Emissionlines[i,j])/float(Emissionlines[i,incidentnum])), 10) > 0:
				concatenated_data[i,j] = math.log(incidentline*(float(Emissionlines[i,j])/float(Emissionlines[i,incidentnum])), 10)
			else:
				concatenated_data[i,j] == 0
print("Finding peaks")
#find the maxima (having cut the arrays already) to plot onto the contour plots
for j in range(len(concatenated_data[0])):
	max_values[j,0] = max(concatenated_data[:,j])
	max_values[j,1] = argmax(concatenated_data[:,j], axis = 0)
	max_values[j,2] = hdens_values[max_values[j,1]]
	max_values[j,3] = phi_values[max_values[j,1]]

#to round off the maxima 
max_values[:,0] = [ '%.1f' % elem for elem in max_values[:,0] ]
print("Data arranged")

# ---------------------------------------------------
gridarray = zeros((len(Emissionlines),2))
gridarray[:,0] = hdens_values
gridarray[:,1] = phi_values

x = gridarray[:,0]
y = gridarray[:,1]

# ---------------------------------------------------
#change desired lines to plot here! indexes of desired lines 
line = [
		#UV1Lines
	[0, 1, 2, 3, 5, 165, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
	#977, 991, 1026, 1216, 1218, 1239, 1240, 1243, 1263, 1304, 1308, 1397, 1402, 1406, 1486, 1531

		#UV2line 
	[16, 17, 18, 19, 20, 21, 23, 24, 25, 27, 29, 30,31, 32, 33, 34],
	#1549, 1640, 1665, 1671, 1750, 1860, 1888, 1907, 2297, 2321, 2471, 2326, 2335, 2665, 2798
		
		#Optical Lines
	[36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
	#NE 3  3343A, NE 5  3426, 3646, 3726, 3727, 3729, 3869, 3889, 3933, 4026, 4070, 4074, 4078, 4102, 4340, 4363

		#Optical Lines 2
	[53, 55, 56, 57, 59, 60, 61, 64, 65, 66, 67, 68, 69, 70, 71, 73],
	#NE 4  4720A, AR 4  4740, 4861, O III 4959, O  3  5007, O  1  5577, N  2  5755, HE 1  5876, O  1  6300;
	#S  3  6312, O  1  6363, H  1  6563, N  2  6584, S II  6716, S  2  6720, S II  6731
		
		#IR Lines
	[75, 76, 77, 78, 79, 80, 81, 82, 84, 83, 85, 86, 87, 88, 89, 90],
	#AR 5  7005A, AR 3  7135A, TOTL  7325A, AR 3  7751, 6LEV  8446, CA2X  8498, CA2Y  8542, CA2Z  8662; 
	#CA 2  8579A, S  3  9069, H  1  9229, S  3  9532... H  1  9546
		#More Lines
	[97,112, 107, 110, 108, 111, 106, 109, 104, 101, 102, 105, 99, 103, 98, 100],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	
] 

# ---------------------------------------------------
Nx = len(np.where(y == y[0])[0])
Ny = len(np.where(x == x[0])[0])

x_axis = x[0:Nx]
y_axis = np.unique(y)
extent = [min(x_axis),max(x_axis),min(y_axis),max(y_axis)]
# ---------------------------------------------------

z_total = [None] * (len(line)-1)
#create z array for this plot
for i in range(len(z_total)):
	zi1 = [concatenated_data[:,line[i]]]
	zi2 = np.reshape(zi1,(Ny,Nx,16))
	z_total[i] = zi2
# ---------------------------------------------------
#plotting features (and contour levels)
 #remove space between plots
#levels = arange(10**-1,10, .2) #teal levels
plt.subplots_adjust(wspace=0, hspace=0) #remove space between plots
levels = arange(10**-2,10**2, 1) #black levels

# ---------------------------------------------------
#loop through desired plots and desired subplots
print("Beginning plotting")
plt.clf()
for j in range (len(z_total)): 
	for i in range(16):
		add_sub_plot(i,j)
	ax1 = plt.subplot(4,4,1)
	add_patches(ax1)
	#plt.show()
	plt.savefig(("Full_lines_%d.pdf")%j)
	print("plot {:d} complete".format(j+1))
	plt.clf()
if (time.clock() - t0) > 120:
	print(time.clock() - t0)/60., "minutes process time"
else: 
	print(time.clock() - t0, "seconds process time")
