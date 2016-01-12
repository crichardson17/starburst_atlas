
############################################################
######## Plotting File for etemp across LOC plane  #########
################## Data read from Cloudy ###################
################ Helen Meskhidze, Fall 2015 ################
#################### Elon University #######################
#------------------------------------------------------------------------------------------------------
'''
The inputs this code takes are .ovr and .grd files from Cloudy. 
This code outputs contours of electron temperature and ionization parameter across the LOC plane
'''
#------------------------------------------------------------------------------------------------------
#Begin with packages
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
    if file.endswith("1.ovr"):
    	temp1 = file

for file in os.listdir('.'):
    if file.endswith("2.ovr"):
    	temp2 = file
    	
for file in os.listdir('.'):
    if file.endswith("3.ovr"):
    	temp3 = file   
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

#the subplot routine (this will create 1 subplot but patches I think only works with subplots?)
numplots = 1
def add_sub_plot(sub_num):

	plt.subplot(1,1,1)
	
	rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
	zi = rbf(xi, yi)

	#io parameter interpolation
	rbf2 = scipy.interpolate.Rbf(xio, yio, zio, function='linear')
	zion = rbf2(xion, yion)

	#our contours. Teal for .2 dex and black for 1 dex
	contour = plt.contour(xi,yi,zi, levels, colors='c', linestyles = 'dashed')
	contour2 = plt.contour(xi,yi,zi, levels2, colors='k', linewidths=1.5)
	contour3 = plt.contour(xion,yion, zion, levelsio, colors='r', linewidths = 1.5) #linestyles = 'dashed')

	plt.clabel(contour2, inline=1, fontsize=10, fmt='%1.1f')
	plt.clabel(contour3, inline=1, fontsize=10, fmt='%1.1f')

	#print the max values right on the plots
	#plt.scatter(max_values[0,2], max_values[0,3], c ='k',marker = '*', s = 1000)
	#plt.annotate(max_values[0,0], xy= (max_values[0,2], max_values[0,3]), xytext = (5, -30), textcoords = 'offset points', ha = 'left', va = 'bottom', fontsize=15)
	#axis limits
	yt_min = 8
	yt_max = 23
	xt_min = 0
	xt_max = 10
	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 
	plt.yticks(arange(yt_min,yt_max+1,1),fontsize=16)
	plt.xticks(arange(xt_min,xt_max+1,1), fontsize = 16)
	plt.ylabel('Log ($ \phi  _{\mathrm{H}}  $)', fontsize=18)
	plt.xlabel('Log($n _{\mathrm{H}}  $)', fontsize=18)
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


#here is where the data for temperature is read in and saved to dataEmissionlines
datatemp1 = [];
datatemp2 = [];
datatemp3 = [];


with open(temp1, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		datatemp1.append(row);		
	datatemp1  = asarray(datatemp1)
with open(temp2, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		datatemp2.append(row);		
	datatemp2  = asarray(datatemp2)
with open(temp3, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		datatemp3.append(row);		
	datatemp3  = asarray(datatemp3)
print "import files complete"
# ---------------------------------------------------

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

datatemp = concatenate((datatemp1,datatemp2,datatemp3))
#for temp values (second column of ovr file)
tempvalues = datatemp[:, 1]

# ---------------------------------------------------
#for grid
datatemp = datatemp[:-1,:]
phi_values = grid[1:len(datatemp)+1,0]
hdens_values = grid[1:len(datatemp)+1,1]

#to find the max values and their grid locations:
max_values = zeros((1,4))
max_values[0,0] = max(tempvalues)
max_values[0,1] = argmax(tempvalues, axis = 0)
max_values[0,2] = hdens_values[max_values[0,1]]
max_values[0,3] = phi_values[max_values[0,1]]

#to round off the maxima 
max_values[:,0] = [ '%.2f' % elem for elem in max_values[:,0] ]

print "data arranged"

# ---------------------------------------------------
#Creating the grid to interpolate with for contours. 
gridarray = zeros((len(datatemp),2))
gridarray[:,0] = hdens_values
gridarray[:,1] = phi_values

x = gridarray[:,0]
x = append(x,0)
y = gridarray[:,1]
y = append(y,0)
z = tempvalues[:]
# ---------------------------------------------------
# Interpolate
print "starting interpolation"
xi, yi = linspace(x.min(), x.max(), 10), linspace(y.min(), y.max(), 10) 
xi, yi = meshgrid(xi, yi)
# ---------------------------------------------------

###
#Ionization Parameter stuff
io_values = zeros(len(phi_values))
for i in range(len(phi_values)):
	io_values[i] = log10(10**(float(phi_values[i]))/(3*10**10.0)/(10**(float(hdens_values[i])+1e-12)))

# ---------------------------------------------------
#Creating the grid to interpolate with for contours. 
gridarrayioparameter = zeros((len(datatemp),2))
gridarrayioparameter[:,0] = hdens_values
gridarrayioparameter[:,1] = phi_values

xio = gridarrayioparameter[:,0]
yio = gridarrayioparameter[:,1]
zio = io_values[:]
# ---------------------------------------------------
# Interpolate
print "starting interpolation"
xion, yion = linspace(xio.min(), xio.max(), (xio.max()-xio.min())*10+10), linspace(yio.min(), yio.max(), (yio.max()-yio.min())*10+10) 
xion, yion = meshgrid(xion, yion)
# ---------------------------------------------------
#plotting time!

print "interpolatation complete; now plotting"
levels = np.array([ (np.arange(.2,.9,.2))+i for i in range(0, 20) ]).flatten()
levels2 = arange(0,20, 1)
#levelsio = [-3.0,0.0,3.0]
levelsio = (-3.0,0.0,3.0)

#plt.suptitle("Temperature Contours- Padova Continuous Age 5 Myr", fontsize=18)

for i in range(1):
	add_sub_plot(i)
ax1 = plt.subplot(1,1,1)
add_patches(ax1)

# ---------------------------------------------------

plt.savefig('tempdiag.pdf')
#plt.savefig('tempdiag.eps', format = 'eps', dpi=1000)
plt.clf()

