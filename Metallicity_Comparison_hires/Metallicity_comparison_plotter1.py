############################################################
####### Plotting File for Metallicity Contour Plots ########
################## Data read from Cloudy ###################
################ Helen Meskhidze, Fall 2015 ################
#################### Elon University #######################
#------------------------------------------------------------------------------------------------------
'''
The inputs this code takes are .grd and .txt files from Cloudy for the solar, supersolar, and subsolar cases
It can take in as many input files (in case you have a grid and haven't concatenated all the files)- just change the numFiles value 
This code outputs the first set of metallicity contour plots, saved to the working directory. 
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
headerloc = "/Users/helen/Documents/Elon/Thesis_Research/github_repo/starburst_atlas/headers_dir/headers.txt"
# ------------------------------------------------------------------------------------------------------
#input data files loaded in here
        
numFilesSolar = 15
numFilesSubSolar = 8
numFilesSuperSolar = 8

gridFilessolar = [None]*numFilesSolar
emissionFilessolar = [None]*numFilesSolar
gridFilessubsolar = [None]*numFilesSubSolar
emissionFilessubsolar = [None]*numFilesSubSolar
gridFilessupersolar = [None]*numFilesSuperSolar
emissionFilessupersolar = [None]*numFilesSuperSolar

for i in range(numFilesSolar):
	for file in os.listdir('./baseline'):
		if file.endswith("padova_cont_5_highres_0{:d}.grd".format(i+1)):
			gridFilessolar[i] = file
			print file
		if file.endswith("padova_cont_5_highres_0{:d}emissionlines_abs.txt".format(i+1)):
			emissionFilessolar[i] = file
			print file

for i in range(numFilesSubSolar):
	for file in os.listdir('./subsolar'):
		if file.endswith("padova_cont_5_{:d}_subsolar_highres.2.grd".format(i+1)):
			gridFilessubsolar[i] = file
			print file
		if file.endswith("padova_cont_5_{:d}_subsolar_highres.2emissionlines_abs.txt".format(i+1)):
			emissionFilessubsolar[i] = file
			print file

for i in range(numFilesSuperSolar):
	for file in os.listdir('./supersolar'):
		if file.endswith("padova_cont_5_{:d}_supersolar_highres.2.grd".format(i+1)):
			gridFilessupersolar[i] = file
			print file
		if file.endswith("padova_cont_5_{:d}_supersolar_highres.2emissionlines_abs.txt".format(i+1)):
			emissionFilessupersolar[i] = file			
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
	patch2 = patches.PathPatch(path2, facecolor='blue', lw=0)
	patch = patches.PathPatch(path, facecolor='grey', lw=0)
	ax1.add_patch(patch3)
	ax1.add_patch(patch2)
	ax1.add_patch(patch)
# ------------------------------------------------------------------------------------------------------

#the add subplots routines
#FIRST SUBSOLAR
plt.figure(figsize=(13,10))
numplots = 18
width = 3 
def add_sub_plot_subsolar(eline,sub_num, set,rows):

	plt.subplot(rows,4,sub_num)
	
	#choose which z array, then which subplot
	z_subnum_subsolar = z_total_subsolar[set]
	z_line_subsolar = z_subnum_subsolar[:,:,eline]
	
	contour1 = plt.contour(x_axis_subsolar, y_axis_subsolar, z_line_subsolar, levels, colors='k', origin='lower', extent=extent) #teal contours, dashed
	contourmap = plt.imshow(z_line_subsolar, cmap='Reds', extent= extent, aspect = "auto",origin='lower', vmin=0, vmax =4)

	
	plt.scatter(max_values_subsolar[line[set][eline],2], max_values_subsolar[line[set][eline],3], c ='k',marker = '*')
	if set ==2:
		plt.annotate(headers[line[set][eline]], xy=(3,8.5),  xytext=(3,8.5), fontsize = 10)
	else:
		plt.annotate(headers[line[set][eline]], xy=(3,8.5),  xytext=(3,8.5), fontsize = 10)

	plt.annotate(max_values_subsolar[line[set][eline],0], xy = (max_values_subsolar[line[set][eline],2], max_values_subsolar[line[set][eline],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	if sub_num == 1:
		plt.title("Subsolar (0.2 Z$\odot$)", fontsize = 12)
	
	if sub_num == 1:
		plt.annotate("a)", xy=(8,11),  xytext=(0.5,21), fontsize = 10, fontweight='bold')
	if sub_num == 5:
		plt.annotate("b)", xy=(8,11),  xytext=(0.5,21), fontsize = 10,fontweight='bold')
	if sub_num == 9:	
		plt.annotate("c)", xy=(8,11),  xytext=(0.5,21), fontsize = 10,fontweight='bold')
	if sub_num == 13:
		plt.annotate("d)", xy=(8,11),  xytext=(0.5,21), fontsize = 10,fontweight='bold')

	yt_min = 8
	yt_max = 17

	xt_min = 0
	xt_max = 6
	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min+1,yt_max,1),fontsize=10)
	plt.xticks(arange(xt_min+1,xt_max,1), fontsize = 10)
	if sub_num in [1,5,9,13,17,21] : 
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
	if sub_num in [13] : 
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
		plt.tick_params(labelbottom = 'on')
		plt.xticks(arange(xt_min,xt_max,1), fontsize = 10)		

#SOLAR
def add_sub_plot_solar(eline,sub_num, set, rows):

	plt.subplot(rows,4,sub_num)
	#choose which z array, then which subplot
	z_subnum_solar = z_total_solar[set]
	z_line_solar = z_subnum_solar[:,:,eline]
	
	contour1 = plt.contour(x_axis_solar, y_axis_solar, z_line_solar, levels, colors='k', origin='lower', extent=extent) #teal contours, dashed
	contourmap = plt.imshow(z_line_solar, cmap='Reds', extent= extent, aspect = "auto",origin='lower', vmin=0, vmax =4)
	

	plt.scatter(max_values_solar[line[set][eline],2], max_values_solar[line[set][eline],3], c ='k',marker = '*')
	if set ==2:
		plt.annotate(headers[line[set][eline]], xy=(3,8.5),  xytext=(3,8.5), fontsize = 10)
	else:
		plt.annotate(headers[line[set][eline]], xy=(3,8.5),  xytext=(3,8.5), fontsize = 10)
	plt.annotate(max_values_solar[line[set][eline],0], xy = (max_values_solar[line[set][eline],2], max_values_solar[line[set][eline],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	if sub_num == 2:
		plt.title("Solar", fontsize = 12)
	if sub_num in [1,5,9,13,17,21] : 
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
	if sub_num in [21,22,23] : 
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
	yt_min = 8
	yt_max = 17

	xt_min = 0
	xt_max = 6
	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min+1,yt_max,1),fontsize=10)
	plt.xticks(arange(xt_min+1,xt_max,1), fontsize = 10)
	plt.tick_params(labelleft = 'off')
	if sub_num in [14] : 
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
		plt.tick_params(labelbottom = 'on')
		plt.xticks(arange(xt_min,xt_max,1), fontsize = 10)		

#SUPERSOLAR
def add_sub_plot_supersolar(eline,sub_num,set, rows):

	plt.subplot(rows,4,sub_num)
	#choose which z array, then which subplot
	z_subnum_supersolar = z_total_supersolar[set]
	z_line_supersolar = z_subnum_supersolar[:,:,eline]
	
	contour1 = plt.contour(x_axis_supersolar, y_axis_supersolar, z_line_supersolar, levels, colors='k', origin='lower', extent=extent) #teal contours, dashed
	contourmap = plt.imshow(z_line_supersolar, cmap='Reds', extent= extent, aspect = "auto",origin='lower', vmin=0, vmax =4)

	plt.scatter(max_values_supersolar[line[set][eline],2], max_values_supersolar[line[set][eline],3], c ='k',marker = '*')
	if set ==2:
		plt.annotate(headers[line[set][eline]], xy=(3,8.5),  xytext=(3,8.5), fontsize = 10)
	else:
		plt.annotate(headers[line[set][eline]], xy=(3,8.5),  xytext=(3,8.5), fontsize = 10)

	plt.annotate(max_values_supersolar[line[set][eline],0], xy = (max_values_supersolar[line[set][eline],2], max_values_supersolar[line[set][eline],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	
	if sub_num == 3:
		plt.title("Supersolar (5.0 Z$\odot$)", fontsize = 12)
	if sub_num in [1,5,9,13,17,21] : 
		plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)')
	if sub_num in [21,22,23] : 
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
	yt_min = 8
	yt_max = 17

	xt_min = 0
	xt_max = 6
	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min+1,yt_max,1),fontsize=10)
	plt.xticks(arange(xt_min+1,xt_max,1), fontsize = 10)
	plt.tick_params(labelleft = 'off')
	if sub_num in [15] : 
		plt.xlabel('Log($n _{\mathrm{H}}  $)')
		plt.tick_params(labelbottom = 'on')		
		plt.xticks(arange(xt_min,xt_max+1,1), fontsize = 10)		

# ---------------------------------------------------
#this is where the grid information (phi and hdens) is read in and saved to grid. 

os.chdir("./baseline")

for i in range(numFilesSolar):
	gridIsolar = [];
	with open(gridFilessolar[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		for row in csvReader:
			gridIsolar.append(row)
	gridIsolar = asarray(gridIsolar)
	gridIsolar = gridIsolar[1:,6:8]
	if ( i == 0 ):
		gridsolar = gridIsolar
	else :
		gridsolar = concatenate((gridsolar,gridIsolar))

for i in range(numFilesSolar):
	emissionLineIsolar = [];
	with open(emissionFilessolar[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		headers = csvReader.next()
		for row in csvReader:
			emissionLineIsolar.append(row)
	emissionLineIsolar = asarray(emissionLineIsolar)
	emissionLineIsolar = emissionLineIsolar[:,1:]
	if ( i == 0 ):
		Emissionlinessolar = emissionLineIsolar
	else :
		Emissionlinessolar = concatenate((Emissionlinessolar,emissionLineIsolar))

# ---------------------------------------------------

os.chdir("../subsolar")

for i in range(numFilesSubSolar):
	gridIsubsolar = [];
	with open(gridFilessubsolar[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		for row in csvReader:
			gridIsubsolar.append(row)
	gridIsubsolar = asarray(gridIsubsolar)
	gridIsubsolar = gridIsubsolar[1:,6:8]
	if ( i == 0 ):
		gridsubsolar = gridIsubsolar
	else :
		gridsubsolar = concatenate((gridsubsolar,gridIsubsolar))

for i in range(numFilesSubSolar):
	emissionLineIsubsolar = [];
	with open(emissionFilessubsolar[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		headers = csvReader.next()
		for row in csvReader:
			emissionLineIsubsolar.append(row)
	emissionLineIsubsolar = asarray(emissionLineIsubsolar)
	emissionLineIsubsolar = emissionLineIsubsolar[:,1:]
	if ( i == 0 ):
		Emissionlinessubsolar = emissionLineIsubsolar
	else :
		Emissionlinessubsolar = concatenate((Emissionlinessubsolar,emissionLineIsubsolar))

# ---------------------------------------------------

os.chdir("../supersolar")

for i in range(numFilesSuperSolar):
	gridIsupersolar = [];
	with open(gridFilessupersolar[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		for row in csvReader:
			gridIsupersolar.append(row)
	gridIsupersolar = asarray(gridIsupersolar)
	gridIsupersolar = gridIsupersolar[1:,6:8]
	if ( i == 0 ):
		gridsupersolar = gridIsupersolar
	else :
		gridsupersolar = concatenate((gridsupersolar,gridIsupersolar))

for i in range(numFilesSuperSolar):
	emissionLineIsupersolar = [];
	with open(emissionFilessupersolar[i], 'rb') as f:
		csvReader = csv.reader(f, delimiter='\t')
		headers = csvReader.next()
		for row in csvReader:
			emissionLineIsupersolar.append(row)
	emissionLineIsupersolar = asarray(emissionLineIsupersolar)
	emissionLineIsupersolar = emissionLineIsupersolar[:,1:]
	if ( i == 0 ):
		Emissionlinessupersolar = emissionLineIsupersolar
	else :
		Emissionlinessupersolar = concatenate((Emissionlinessupersolar,emissionLineIsupersolar))

print "all data read in"

os.chdir("../")

hdens_values_solar = gridsolar[:,1]
phi_values_solar = gridsolar[:,0]

hdens_values_subsolar = gridsubsolar[:,1]
phi_values_subsolar = gridsubsolar[:,0]

hdens_values_supersolar = gridsupersolar[:,1]
phi_values_supersolar = gridsupersolar[:,0]
# --------------------------------------------------
'''
#To fix when hdens > 10
print "beginning modifications to hdens solar array"

hdens_values_solar_2 = empty(shape=[0, 1])
phi_values_solar_2 = empty(shape=[0, 1])
Emissionlines_solar_2 = empty(shape=[0, len(Emissionlinessolar[0,:])])

for i in range(len(hdens_values_solar)):
	if (float(hdens_values_solar[i]) < 6.100) & (float(phi_values_solar[i]) < 17.100) : 
		hdens_values_solar_2 = append(hdens_values_solar_2, hdens_values_solar[i])
		phi_values_solar_2 = append(phi_values_solar_2, phi_values_solar[i])
		Emissionlines_solar_2 = vstack([Emissionlines_solar_2, Emissionlinessolar[i,:]])
#overwrite old arrays
hdens_values_solar = hdens_values_solar_2
phi_values_solar = phi_values_solar_2
Emissionlinessolar = Emissionlines_solar_2

print "modifications to hdens solar array complete"
print "beginning modifications to hdens subsolar array"

hdens_values_subsolar_2 = empty(shape=[0, 1])
phi_values_subsolar_2 = empty(shape=[0, 1])
Emissionlines_subsolar_2 = empty(shape=[0, len(Emissionlinessubsolar[0,:])])

for i in range(len(hdens_values_subsolar)):
	if (float(hdens_values_subsolar[i]) < 6.100) & (float(phi_values_subsolar[i]) < 17.100) :
		hdens_values_subsolar_2 = append(hdens_values_subsolar_2, hdens_values_subsolar[i])
		phi_values_subsolar_2 = append(phi_values_subsolar_2, phi_values_subsolar[i])
		Emissionlines_subsolar_2 = vstack([Emissionlines_subsolar_2, Emissionlinessubsolar[i,:]])
#overwrite old arrays
hdens_values_subsolar = hdens_values_subsolar_2
phi_values_subsolar = phi_values_subsolar_2
Emissionlinessubsolar = Emissionlines_subsolar_2

print "modifications to hdens subsolar array complete"
print "beginning modifications to hdens supersolar array"

hdens_values_supersolar_2 = empty(shape=[0, 1])
phi_values_supersolar_2 = empty(shape=[0, 1])
Emissionlines_supersolar_2 = empty(shape=[0, len(Emissionlinessupersolar[0,:])])

for i in range(len(hdens_values_supersolar)):
	if (float(hdens_values_supersolar[i]) < 6.100) & (float(phi_values_supersolar[i]) < 17.100) : 
		hdens_values_supersolar_2 = append(hdens_values_supersolar_2, hdens_values_supersolar[i])
		phi_values_supersolar_2 = append(phi_values_supersolar_2, phi_values_supersolar[i])
		Emissionlines_supersolar_2 = vstack([Emissionlines_supersolar_2, Emissionlinessupersolar[i,:]])
#overwrite old arrays
hdens_values_supersolar = hdens_values_supersolar_2
phi_values_supersolar = phi_values_supersolar_2
Emissionlinessupersolar = Emissionlines_supersolar_2
print "modifications to hdens supersolar array complete"
'''
# ---------------------------------------------------
#there are the emission line names properly formatted
print("Importing headers from header file")
headersFile = open(headerloc,'r')
headers = headersFile.read().splitlines()
headersFile.close()
# ---------------------------------------------------


concatenated_data_solar = zeros((len(Emissionlinessolar),len(Emissionlinessolar[0])))
concatenated_data_subsolar = zeros((len(Emissionlinessubsolar),len(Emissionlinessupersolar[0])))
concatenated_data_supersolar = zeros((len(Emissionlinessubsolar),len(Emissionlinessupersolar[0])))

max_values_solar = zeros((len(concatenated_data_solar[0]),4))
max_values_subsolar = zeros((len(concatenated_data_subsolar[0]),4))
max_values_supersolar = zeros((len(concatenated_data_supersolar[0]),4))

print "scaling data"
#select the scaling factor

#for 1215
#incident = Emissionlines[1:,4] 

#for 4860
incidentnum = 58
incident = Emissionlinessolar[:,58] 
incident = Emissionlinessubsolar[:,58] 
incident = Emissionlinessupersolar[:,58] 


#take the ratio of incident and all the lines and put it all in an array concatenated_data
for i in range(len(Emissionlinessolar)):
	for j in range(len(Emissionlinessolar[0])):
			if math.log(4860.*(float(Emissionlinessolar[i,j])/float(Emissionlinessolar[i,incidentnum])), 10) > 0:
				concatenated_data_solar[i,j] = math.log(4860.*(float(Emissionlinessolar[i,j])/float(Emissionlinessolar[i,incidentnum])), 10)
			else:
				concatenated_data_solar[i,j] == 0

for i in range(len(Emissionlinessubsolar)):
	for j in range(len(Emissionlinessubsolar[0])):
			if math.log(4860.*(float(Emissionlinessubsolar[i,j])/float(Emissionlinessubsolar[i,incidentnum])), 10) > 0:
				concatenated_data_subsolar[i,j] = math.log(4860.*(float(Emissionlinessubsolar[i,j])/float(Emissionlinessubsolar[i,incidentnum])), 10)
			else:
				concatenated_data_subsolar[i,j] == 0

for i in range(len(Emissionlinessupersolar)):
	for j in range(len(Emissionlinessupersolar[0])):
			if math.log(4860.*(float(Emissionlinessupersolar[i,j])/float(Emissionlinessupersolar[i,incidentnum])), 10) > 0:
				concatenated_data_supersolar[i,j] = math.log(4860.*(float(Emissionlinessupersolar[i,j])/float(Emissionlinessupersolar[i,incidentnum])), 10)
			else:
				concatenated_data_supersolar[i,j] == 0

#find the maxima to plot onto the contour plots
for j in range(len(concatenated_data_solar[0])):
	max_values_solar[j,0] = max(concatenated_data_solar[:,j])
	max_values_solar[j,1] = argmax(concatenated_data_solar[:,j], axis = 0)
	max_values_solar[j,2] = hdens_values_solar[max_values_solar[j,1]]
	max_values_solar[j,3] = phi_values_solar[max_values_solar[j,1]]

for j in range(len(concatenated_data_subsolar[0])):
	max_values_subsolar[j,0] = max(concatenated_data_subsolar[:,j])
	max_values_subsolar[j,1] = argmax(concatenated_data_subsolar[:,j], axis = 0)
	max_values_subsolar[j,2] = hdens_values_subsolar[max_values_subsolar[j,1]]
	max_values_subsolar[j,3] = phi_values_subsolar[max_values_subsolar[j,1]]

for j in range(len(concatenated_data_supersolar[0])):
	max_values_supersolar[j,0] = max(concatenated_data_supersolar[:,j])
	max_values_supersolar[j,1] = argmax(concatenated_data_supersolar[:,j], axis = 0)
	max_values_supersolar[j,2] = hdens_values_supersolar[max_values_supersolar[j,1]]
	max_values_supersolar[j,3] = phi_values_supersolar[max_values_supersolar[j,1]]	

#to round off the maxima 
max_values_solar[:,0] = [ '%.1f' % elem for elem in max_values_solar[:,0] ]
max_values_subsolar[:,0] = [ '%.1f' % elem for elem in max_values_subsolar[:,0] ]
max_values_supersolar[:,0] = [ '%.1f' % elem for elem in max_values_supersolar[:,0] ]

print "data arranged"

# ---------------------------------------------------

#Creating the grid to interpolate with for contours. 
gridarraysolar = zeros((len(Emissionlinessolar),2))
gridarraysolar[:,0] = hdens_values_solar
gridarraysolar[:,1] = phi_values_solar

gridarraysubsolar = zeros((len(Emissionlinessubsolar),2))
gridarraysubsolar[:,0] = hdens_values_subsolar
gridarraysubsolar[:,1] = phi_values_subsolar

gridarraysupersolar = zeros((len(Emissionlinessupersolar),2))
gridarraysupersolar[:,0] = hdens_values_supersolar
gridarraysupersolar[:,1] = phi_values_supersolar


xsolar = gridarraysolar[:,0]
ysolar = gridarraysolar[:,1]

xsubsolar = gridarraysubsolar[:,0]
ysubsolar = gridarraysubsolar[:,1]

xsupersolar = gridarraysupersolar[:,0]
ysupersolar = gridarraysupersolar[:,1]

#change desired lines here!
line = [[1,3,7,18],
		[41,57,61,67],
		[76,77,85,105]]

#create z array for this plot
zsolar = [None] * (len(line))
zsubsolar = [None] * (len(line))
zsupersolar = [None] * (len(line))

#create z array for this plot
for i in range(len(line)):
	zsolar[i] = [concatenated_data_solar[:,line[i]]]
	zsubsolar[i] = [concatenated_data_subsolar[:,line[i]]]
	zsupersolar[i] = [concatenated_data_supersolar[:,line[i]]]
# ---------------------------------------------------
Nxsolar = len(np.where(ysolar == ysolar[0])[0])
Nxsubsolar = len(np.where(ysubsolar == ysubsolar[0])[0])
Nxsupersolar = len(np.where(ysupersolar == ysupersolar[0])[0])

Nysolar = len(np.where(xsolar == xsolar[0])[0])
Nysubsolar = len(np.where(xsubsolar == xsubsolar[0])[0])
Nysupersolar = len(np.where(xsupersolar == xsupersolar[0])[0])

x_axis_solar = xsolar[0:Nxsolar]
x_axis_subsolar = xsubsolar[0:Nxsubsolar]
x_axis_supersolar = xsupersolar[0:Nxsupersolar]

y_axis_solar = np.unique(ysolar)
y_axis_subsolar = np.unique(ysubsolar)
y_axis_supersolar = np.unique(ysupersolar)


extent = [min(x_axis_solar),max(x_axis_solar),min(y_axis_solar),max(y_axis_solar)]

z_new0_solar = np.reshape(zsolar[0],(Nysolar,Nxsolar,len(line[0])))
z_new1_solar = np.reshape(zsolar[1],(Nysolar,Nxsolar,len(line[0])))
z_new2_solar = np.reshape(zsolar[2],(Nysolar,Nxsolar,len(line[0])))


z_total_solar = [z_new0_solar,z_new1_solar,z_new2_solar]

z_new0_subsolar = np.reshape(zsubsolar[0],(Nysubsolar,Nxsubsolar,len(line[0])))
z_new1_subsolar = np.reshape(zsubsolar[1],(Nysubsolar,Nxsubsolar,len(line[0])))
z_new2_subsolar = np.reshape(zsubsolar[2],(Nysubsolar,Nxsubsolar,len(line[0])))


z_total_subsolar = [z_new0_subsolar,z_new1_subsolar,z_new2_subsolar]

z_new0_supersolar = np.reshape(zsupersolar[0],(Nysupersolar,Nxsupersolar,len(line[0])))
z_new1_supersolar = np.reshape(zsupersolar[1],(Nysupersolar,Nxsupersolar,len(line[0])))
z_new2_supersolar = np.reshape(zsupersolar[2],(Nysupersolar,Nxsupersolar,len(line[0])))


z_total_supersolar = [z_new0_supersolar,z_new1_supersolar,z_new2_supersolar]

#---------------------------------------------------
#plot
plt.subplots_adjust(wspace=0, hspace=0) #remove space between plots
#levels = arange(10**-1,10, .2)
levels = arange(10**-2,10**2, 1)
# ---------------------------------------------------
plotnames = ["UV_MetallicityComp_patched.pdf", "Optical_MetallicityComp_patched.pdf","IR_MetallicityComp_patched.pdf"] 

subplots_ref2 = [1,5,9,13]#,17,21]
for i in range(3):
	counter = 0
	print "plot started"
	for j in subplots_ref2:
		add_sub_plot_subsolar(counter,j,i,4)
		add_sub_plot_solar(counter,j+1,i,4)
		add_sub_plot_supersolar(counter,j+2,i,4)
		ax1= plt.subplot(counter,j,i,4)
		add_patches(ax1)
		counter += 1
		
	print "plot saving"
	plt.savefig(plotnames[i])
	print "plot saved"
	plt.clf()

if (time.clock() - t0) > 120:
	print((time.clock() - t0)/60., "minutes process time")
else: 
	print(time.clock() - t0, "seconds process time")
