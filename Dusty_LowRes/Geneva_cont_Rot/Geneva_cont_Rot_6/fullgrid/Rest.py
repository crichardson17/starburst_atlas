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
# ------------------------
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
# -------------------------
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

#the subplot routine

def add_sub_plot(sub_num):
	numplots = 16

	plt.subplot(numplots/4.,4,sub_num)
	
	rbf = scipy.interpolate.Rbf(x, y, z[:,sub_num-1], function='linear')
	zi = rbf(xi, yi)

	contour = plt.contour(xi,yi,zi, levels, colors='c', linestyles = 'dashed')
	contour2 = plt.contour(xi,yi,zi, levels2, colors='k', linewidths=1.5)
	
	plt.scatter(max_values[line[sub_num-1],2], max_values[line[sub_num-1],3], c ='k',marker = '*')
	plt.annotate(headers[line[sub_num-1]], xy=(8,11),  xytext=(6,8.5), fontsize = 10)
	plt.annotate(max_values[line[sub_num-1],0], xy= (max_values[line[sub_num-1],2], max_values[line[sub_num-1],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	
	if sub_num == numplots / 2.:
		print "half the plots are complete"
#axis limits


	yt_min = 8
	yt_max = 23
	xt_min = 0
	xt_max = 12
	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min+1,yt_max,1),fontsize=10)
	plt.xticks(arange(xt_min+1,xt_max,1), fontsize = 10)

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
# ---------------------------------------------------

#for concatenating Emission lines data
Emissionlines = concatenate((dataEmissionlines1[:,1:],dataEmissionlines2[:,1:],dataEmissionlines3[:,1:]))

#for lines
headers = headers[1:]

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
print "data arranged"

# ---------------------------------------------------

#Creating the grid to interpolate with for contours. 
gridarray = zeros((len(concatenated_data),2))
gridarray[:,0] = hdens_values
gridarray[:,1] = phi_values

x = gridarray[:,0]
y = gridarray[:,1]

# ---------------------------------------------------



#change desired lines here!


line = [3,4,15,22,37,53,54,55,57,62,77,88,89,90,92,93]

#create z array for this plot
z = concatenated_data[:,line[:]]

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
plt.suptitle("Dusty Rest of the Lines", fontsize=14)
# ---------------------------------------------------
for i in range(16):
	add_sub_plot(i)
ax1 = plt.subplot(4,4,1)
add_patches(ax1)

print "complete"

plt.savefig('Dusty_Rest.pdf')
plt.clf()
print "figure saved"




