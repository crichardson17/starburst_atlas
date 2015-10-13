############################################################
####### Plotting File for Metallicity Contour Plots ########
################## Data read from Cloudy ###################
################ Helen Meskhidze, Fall 2015 ################
############################################################
#------------------------------------------------------------------------------------------------------
'''
The inputs this code takes are .grd and .txt files from Cloudy for the dustfree, superdustfree, and dusty cases
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
from matplotlib.backends.backend_pdf import PdfPages
import time
# ------------------------------------------------------------------------------------------------------
# keep track of how long the code takes to run 
t0 = time.clock()
headerloc = "/Users/helen/Documents/git_atlas_complete/headers_dir/headers.txt"
# ------------------------------------------------------------------------------------------------------
#input data files loaded in here
        
numFilesdusty = 15
numFilesdustfree = 6

gridFilesdusty = [None]*numFilesdusty
emissionFilesdusty = [None]*numFilesdusty
gridFilesdustfree = [None]*numFilesdustfree
emissionFilesdustfree = [None]*numFilesdustfree

for i in range(numFilesdusty):
	for file in os.listdir('./dusty'):
		if file.endswith("padova_cont_5_highres_0{:d}.grd".format(i+1)):
			gridFilesdusty[i] = file
			print file
		if file.endswith("padova_cont_5_highres_0{:d}emissionlines_abs.txt".format(i+1)):
			emissionFilesdusty[i] = file
			print file
for i in range(numFilesdustfree):
	for file in os.listdir('./dustfree'):
		if file.endswith("padova_cont_highres_dustfree{:d}.grd".format(i+1)):
			gridFilesdustfree[i] = file
			print file
		if file.endswith("padova_cont_highres_dustfreeemissionlines_abs{:d}.txt".format(i+1)):
			emissionFilesdustfree[i] = file
			print file


print "Data files found; proceeding to read data"

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
#Dust free
def add_sub_plot_dustfree(eline,sub_num, set, rows):

	plt.subplot(rows,4,sub_num)
	#choose which z array, then which subplot
	z_subnum_dustfree = z_total_dustfree[set]
	z_line_dustfree = z_subnum_dustfree[:,:,eline]
	
	contour = plt.contour(x_axis_dustfree, y_axis_dustfree, z_line_dustfree, levels, colors='c', linestyles = 'dashed', extent=extent) #teal contours, dashed
	contour2 = plt.contour(x_axis_dustfree, y_axis_dustfree, z_line_dustfree, levels2, colors='k', linewidths=1.5) #black contours, solid
	

	plt.scatter(max_values_dustfree[line[set][eline],2], max_values_dustfree[line[set][eline],3], c ='k',marker = '*')
	if set ==2:
		plt.annotate(headers[line[set][eline]], xy=(10,11),  xytext=(4,8.5), fontsize = 10)
	else:
		plt.annotate(headers[line[set][eline]], xy=(10,11),  xytext=(4,8.5), fontsize = 10)
	plt.annotate(max_values_dustfree[line[set][eline],0], xy = (max_values_dustfree[line[set][eline],2], max_values_dustfree[line[set][eline],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	plt.tick_params(labelleft = 'off')
	if sub_num in [1,5,9,13,17,21] : 
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
		plt.tick_params(labelleft = 'on')

	if sub_num in [13,14,15,16] : 
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
		plt.tick_params(labelbottom = 'on')
	yt_min = 8
	yt_max = 17

	xt_min = 0
	xt_max = 10
	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min,yt_max+1,1),fontsize=10)
	plt.xticks(arange(xt_min,xt_max,1), fontsize = 10)
	

	if sub_num == 3:
		figtext(0.5,.915,'Dustfree', fontsize=12, ha='center')

	if sub_num == 11:
		figtext(0.5,.48,'Dustfree', fontsize=12, ha='center')

#Dusty
plt.figure(figsize=(13,10))
numplots = 16
width = 4
def add_sub_plot_dusty(eline,sub_num, set,rows):

	plt.subplot(rows,4,sub_num)
	
	#choose which z array, then which subplot
	z_subnum_dusty = z_total_dusty[set]
	z_line_dusty = z_subnum_dusty[:,:,eline]
	
	contour = plt.contour(x_axis_dusty, y_axis_dusty, z_line_dusty, levels, colors='c', linestyles = 'dashed', extent=extent) #teal contours, dashed
	contour2 = plt.contour(x_axis_dusty, y_axis_dusty, z_line_dusty, levels2, colors='k', linewidths=1.5) #black contours, solid
	
	plt.scatter(max_values_dusty[line[set][eline],2], max_values_dusty[line[set][eline],3], c ='k',marker = '*')
	if set ==2:
		plt.annotate(headers[line[set][eline]], xy=(10,11),  xytext=(4,8.5), fontsize = 10)
	else:
		plt.annotate(headers[line[set][eline]], xy=(10,11),  xytext=(4,8.5), fontsize = 10)

	plt.annotate(max_values_dusty[line[set][eline],0], xy = (max_values_dusty[line[set][eline],2], max_values_dusty[line[set][eline],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	if sub_num == 1:
		plt.title("dusty (0.2 Z$\odot$)", fontsize = 12)
	yt_min = 8
	yt_max = 17

	xt_min = 0
	xt_max = 10

	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min,yt_max+1,1),fontsize=10)
	plt.xticks(arange(xt_min,xt_max,1), fontsize = 10)
	plt.tick_params(labelleft = 'off')
	if sub_num in [1,5,9,13,17,21] : 
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
		plt.tick_params(labelleft = 'on')

	if sub_num in [13,14,15, 16] : 
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
		plt.tick_params(labelbottom = 'on')
	
	if sub_num == 7:
		figtext(0.5,.7,'Dusty', fontsize=12, ha='center')

	if sub_num == 15:
		figtext(0.5,.265,'Dusty', fontsize=12, ha='center')


# ---------------------------------------------------
#this is where the grid information (phi and hdens) is read in and saved to grid. 

os.chdir("./dustfree")

for i in range(numFilesdustfree):
	gridIdustfree = [];
	with open(gridFilesdustfree[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		for row in csvReader:
			gridIdustfree.append(row)
	gridIdustfree = asarray(gridIdustfree)
	gridIdustfree = gridIdustfree[1:,6:8]
	if ( i == 0 ):
		griddustfree = gridIdustfree
	else :
		griddustfree = concatenate((griddustfree,gridIdustfree))

for i in range(numFilesdustfree):
	emissionLineIdustfree = [];
	with open(emissionFilesdustfree[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		headers = csvReader.next()
		for row in csvReader:
			emissionLineIdustfree.append(row)
	emissionLineIdustfree = asarray(emissionLineIdustfree)
	emissionLineIdustfree = emissionLineIdustfree[:,1:]
	if ( i == 0 ):
		Emissionlinesdustfree = emissionLineIdustfree
	else :
		Emissionlinesdustfree = concatenate((Emissionlinesdustfree,emissionLineIdustfree))

# ---------------------------------------------------

os.chdir("../dusty")

for i in range(numFilesdusty):
	gridIdusty = [];
	with open(gridFilesdusty[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		for row in csvReader:
			gridIdusty.append(row)
	gridIdusty = asarray(gridIdusty)
	gridIdusty = gridIdusty[1:,6:8]
	if ( i == 0 ):
		griddusty = gridIdusty
	else :
		griddusty = concatenate((griddusty,gridIdusty))

for i in range(numFilesdusty):
	emissionLineIdusty = [];
	with open(emissionFilesdusty[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		headers = csvReader.next()
		for row in csvReader:
			emissionLineIdusty.append(row)
	emissionLineIdusty = asarray(emissionLineIdusty)
	emissionLineIdusty = emissionLineIdusty[:,1:]
	if ( i == 0 ):
		Emissionlinesdusty = emissionLineIdusty
	else :
		Emissionlinesdusty = concatenate((Emissionlinesdusty,emissionLineIdusty))

print "all data read in"

os.chdir("../")

hdens_values_dustfree = griddustfree[:,1]
phi_values_dustfree = griddustfree[:,0]

hdens_values_dusty = griddusty[:,1]
phi_values_dusty = griddusty[:,0]

# --------------------------------------------------

#To fix when hdens > 10
print "beginning modifications to hdens dustfree array"

hdens_values_dustfree_2 = empty(shape=[0, 1])
phi_values_dustfree_2 = empty(shape=[0, 1])
Emissionlines_dustfree_2 = empty(shape=[0, len(Emissionlinesdustfree[0,:])])

for i in range(len(hdens_values_dustfree)):
	if (float(hdens_values_dustfree[i]) < 10.100) & (float(phi_values_dustfree[i]) < 17.100) : 
		hdens_values_dustfree_2 = append(hdens_values_dustfree_2, hdens_values_dustfree[i])
		phi_values_dustfree_2 = append(phi_values_dustfree_2, phi_values_dustfree[i])
		Emissionlines_dustfree_2 = vstack([Emissionlines_dustfree_2, Emissionlinesdustfree[i,:]])
#overwrite old arrays
hdens_values_dustfree = hdens_values_dustfree_2
phi_values_dustfree = phi_values_dustfree_2
Emissionlinesdustfree = Emissionlines_dustfree_2

print "modifications to hdens dustfree array complete"
print "beginning modifications to hdens dusty array"

hdens_values_dusty_2 = empty(shape=[0, 1])
phi_values_dusty_2 = empty(shape=[0, 1])
Emissionlines_dusty_2 = empty(shape=[0, len(Emissionlinesdusty[0,:])])

for i in range(len(hdens_values_dusty)):
	if (float(hdens_values_dusty[i]) < 10.100) & (float(phi_values_dusty[i]) < 17.100) : 
		hdens_values_dusty_2 = append(hdens_values_dusty_2, hdens_values_dusty[i])
		phi_values_dusty_2 = append(phi_values_dusty_2, phi_values_dusty[i])
		Emissionlines_dusty_2 = vstack([Emissionlines_dusty_2, Emissionlinesdusty[i,:]])
#overwrite old arrays
hdens_values_dusty = hdens_values_dusty_2
phi_values_dusty = phi_values_dusty_2
Emissionlinesdusty = Emissionlines_dusty_2

print "modifications to hdens dusty array complete"


# ---------------------------------------------------
#there are the emission line names properly formatted
print("Importing headers from header file")
headersFile = open(headerloc,'r')
headers = headersFile.read().splitlines()
headersFile.close()
# ---------------------------------------------------


concatenated_data_dustfree = zeros((len(Emissionlinesdustfree),len(Emissionlinesdustfree[0])))
concatenated_data_dusty = zeros((len(Emissionlinesdusty),len(Emissionlinesdusty[0])))

max_values_dustfree = zeros((len(concatenated_data_dustfree[0]),4))
max_values_dusty = zeros((len(concatenated_data_dusty[0]),4))

print "scaling data"
#select the scaling factor

#for 1215
#incident = Emissionlines[1:,4] 

#for 4860
incidentnum = 58
incident = Emissionlinesdustfree[:,58] 
incident = Emissionlinesdusty[:,58] 


#take the ratio of incident and all the lines and put it all in an array concatenated_data
for i in range(len(Emissionlinesdustfree)):
	for j in range(len(Emissionlinesdustfree[0])):
			if math.log(4860.*(float(Emissionlinesdustfree[i,j])/float(Emissionlinesdustfree[i,incidentnum])), 10) > 0:
				concatenated_data_dustfree[i,j] = math.log(4860.*(float(Emissionlinesdustfree[i,j])/float(Emissionlinesdustfree[i,incidentnum])), 10)
			else:
				concatenated_data_dustfree[i,j] == 0

for i in range(len(Emissionlinesdusty)):
	for j in range(len(Emissionlinesdusty[0])):
			if math.log(4860.*(float(Emissionlinesdusty[i,j])/float(Emissionlinesdusty[i,incidentnum])), 10) > 0:
				concatenated_data_dusty[i,j] = math.log(4860.*(float(Emissionlinesdusty[i,j])/float(Emissionlinesdusty[i,incidentnum])), 10)
			else:
				concatenated_data_dusty[i,j] == 0

#find the maxima to plot onto the contour plots
for j in range(len(concatenated_data_dustfree[0])):
	max_values_dustfree[j,0] = max(concatenated_data_dustfree[:,j])
	max_values_dustfree[j,1] = argmax(concatenated_data_dustfree[:,j], axis = 0)
	max_values_dustfree[j,2] = hdens_values_dustfree[max_values_dustfree[j,1]]
	max_values_dustfree[j,3] = phi_values_dustfree[max_values_dustfree[j,1]]

for j in range(len(concatenated_data_dusty[0])):
	max_values_dusty[j,0] = max(concatenated_data_dusty[:,j])
	max_values_dusty[j,1] = argmax(concatenated_data_dusty[:,j], axis = 0)
	max_values_dusty[j,2] = hdens_values_dusty[max_values_dusty[j,1]]
	max_values_dusty[j,3] = phi_values_dusty[max_values_dusty[j,1]]

#to round off the maxima 
max_values_dustfree[:,0] = [ '%.1f' % elem for elem in max_values_dustfree[:,0] ]
max_values_dusty[:,0] = [ '%.1f' % elem for elem in max_values_dusty[:,0] ]

print "data arranged"

# ---------------------------------------------------

#Creating the grid to interpolate with for contours. 
gridarraydustfree = zeros((len(Emissionlinesdustfree),2))
gridarraydustfree[:,0] = hdens_values_dustfree
gridarraydustfree[:,1] = phi_values_dustfree

gridarraydusty = zeros((len(Emissionlinesdusty),2))
gridarraydusty[:,0] = hdens_values_dusty
gridarraydusty[:,1] = phi_values_dusty


xdustfree = gridarraydustfree[:,0]
ydustfree = gridarraydustfree[:,1]

xdusty = gridarraydusty[:,0]
ydusty = gridarraydusty[:,1]

line = [[76,87,111,104],
		[101,105,99,98]]

#create z array for this plot
zdustfree = [None] * (len(line))
zdusty = [None] * (len(line))

#create z array for this plot
for i in range(len(line)):
	zdustfree[i] = [concatenated_data_dustfree[:,line[i]]]
	zdusty[i] = [concatenated_data_dusty[:,line[i]]]
# ---------------------------------------------------
Nxdustfree = len(np.where(ydustfree == ydustfree[0])[0])
Nxdusty = len(np.where(ydusty == ydusty[0])[0])

Nydustfree = len(np.where(xdustfree == xdustfree[0])[0])
Nydusty = len(np.where(xdusty == xdusty[0])[0])

x_axis_dustfree = xdustfree[0:Nxdustfree]
x_axis_dusty = xdusty[0:Nxdusty]

y_axis_dustfree = np.unique(ydustfree)
y_axis_dusty = np.unique(ydusty)


extent = [min(x_axis_dustfree),max(x_axis_dustfree),min(y_axis_dustfree),max(y_axis_dustfree)]

z_new0_dustfree = np.reshape(zdustfree[0],(Nydustfree,Nxdustfree,len(line[0])))
z_new1_dustfree = np.reshape(zdustfree[1],(Nydustfree,Nxdustfree,len(line[0])))


z_total_dustfree = [z_new0_dustfree,z_new1_dustfree]

z_new0_dusty = np.reshape(zdusty[0],(Nydusty,Nxdusty,len(line[0])))
z_new1_dusty = np.reshape(zdusty[1],(Nydusty,Nxdusty,len(line[0])))


z_total_dusty = [z_new0_dusty,z_new1_dusty]

# ---------------------------------------------------

#plot
plt.subplots_adjust(wspace=0, hspace=.4)
 #remove space between plots
levels = arange(10**-1,10, .2)
levels2 = arange(10**-2,10**2, 1)
# ---------------------------------------------------

counter =1
for i in range (4):
	add_sub_plot_dustfree(i,counter,0,4)
	add_sub_plot_dusty(i,counter+4,0,4)
	counter = counter + 1

for i in range (4):
	add_sub_plot_dustfree(i,counter+4,1,4)
	add_sub_plot_dusty(i,counter+8,1,4)
	counter = counter + 1
#plt.show()
plt.savefig("IR_Dust_Comparison.pdf")

if (time.clock() - t0) > 120:
	print((time.clock() - t0)/60., "minutes process time")
else: 
	print(time.clock() - t0, "seconds process time")


