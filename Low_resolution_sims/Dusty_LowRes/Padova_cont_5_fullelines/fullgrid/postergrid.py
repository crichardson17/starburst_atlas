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
'''
#the routine to add patches for others peoples' data onto our plots. 
def add_patches(ax):
	patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
	patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
	patch = patches.PathPatch(path, facecolor='red', lw=0)
	ax1.add_patch(patch3)
	ax1.add_patch(patch2)
	ax1.add_patch(patch)

	ax2.add_patch(patch3)
	ax2.add_patch(patch2)
	ax2.add_patch(patch)
'''
# ------------------------------------------------------------------------------------------------------
#the subplot routine; will be called later
numplots = 21

fig = plt.figure()

def add_sub_plot(sub_num):

	plt.subplot(3,7,sub_num)
	
	rbf = scipy.interpolate.Rbf(x, y, z[:,sub_num-1], function='linear')
	zi = rbf(xi, yi)

	contour = plt.contour(xi,yi,zi, levels, colors='c', linestyles = 'dashed')
	contour2 = plt.contour(xi,yi,zi, levels2, colors='k', linewidths=1.5)
	
	plt.scatter(max_values[line[sub_num-1],2], max_values[line[sub_num-1],3], c ='k',marker = '*')

	if sub_num <= 16 and sub_num != 13 :
		plt.annotate(max_values[line[sub_num-1],0], xy= (max_values[line[sub_num-1],2], max_values[line[sub_num-1],3]), xytext = (0, -15), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=11)

	if sub_num == 13:
		plt.annotate(max_values[line[sub_num-1],0], xy= (max_values[line[sub_num-1],2], max_values[line[sub_num-1],3]), xytext = (0, 15), textcoords = 'offset points', ha = 'right', va = 'top', fontsize=11)

	if sub_num > 16:
		plt.annotate(max_values[line[sub_num-1],0], xy= (max_values[line[sub_num-1],2], max_values[line[sub_num-1],3]), xytext = (0, 15), textcoords = 'offset points', ha = 'left', va = 'top', fontsize=11)

	#	plt.annotate(max_values[line[sub_num-1],0], xy= (max_values[line[sub_num-1],2], max_values[line[sub_num-1],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=11)
	
	#if sub_num > 14 and sub_num < 18:

	#	plt.annotate(max_values[line[sub_num-1],0], xy= (max_values[line[sub_num-1],2], max_values[line[sub_num-1],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=11)
	
	#if sub_num >= 18:
	#	plt.annotate(max_values[line[sub_num-1],0], xy= (max_values[line[sub_num-1],2], max_values[line[sub_num-1],3]), xytext = (0, 15), textcoords = 'offset points', ha = 'left', va = 'top', fontsize=11)
	
	plt.annotate(plotstitles[sub_num-1], xy=(8,11),  xytext=(6,8.25), fontsize = 11)		

	if sub_num == numplots / 2.:
		print "half the plots are complete"
#axis limits

	yt_min = 8
	yt_max = 23
	xt_min = 0
	xt_max = 10

	plt.ylim(yt_min,yt_max)
	plt.xlim(xt_min,xt_max) 


	plt.yticks(arange(yt_min+1,yt_max,2),fontsize=12)
	plt.xticks(arange(xt_min+1,xt_max,1), fontsize = 12)

	if sub_num in [2,3,4,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21]:
		plt.tick_params(labelleft = 'off')
	else:
		plt.tick_params(labelleft = 'on')

	if sub_num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
		plt.tick_params(labelbottom = 'off')
	else: 		
		plt.tick_params(labelbottom = 'on')

	if sub_num == 1:
		plt.yticks(arange(yt_min+1,yt_max+1,2),fontsize=12)
 
	if sub_num == 8:
		plt.yticks(arange(yt_min+1,yt_max,2),fontsize=12)
		#plt.xticks(arange(xt_min,xt_max,1), fontsize = 12)
	if sub_num == 15:
		plt.yticks(arange(yt_min+1,yt_max,2),fontsize=12)
		plt.xticks(arange(0,10,1), fontsize = 12)
	#if sub_num == 20:
	#	plt.xticks(arange(1,11,1), fontsize = 12)



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

#Emissionlines = Emissionlines[np.where(hdens_values<=10.)]

#for lines
headers = headers[1:]

concatenated_data = zeros((len(Emissionlines),len(Emissionlines[0])))
#concatenated_data = concatenated_data_tmp[np.where(hdens_values <= 10.)]
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

	concatenated_data_cut = concatenated_data[np.where(hdens_values <= 10.)]
	max_values[j,0] = max(concatenated_data_cut[:,j])
	max_values[j,1] = argmax(concatenated_data_cut[:,j], axis = 0)
	hdens_values_cut = hdens_values[np.where(hdens_values<=10.)]
	phi_values_cut = phi_values[np.where(hdens_values<=10.)]

	max_values[j,2] = hdens_values_cut[max_values[j,1]]
	max_values[j,3] = phi_values_cut[max_values[j,1]]

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


line = [3, #1034
		7,	#1240		
		18, #1549
		28, #2297
		34, #2798
		37, #Ne V 3426
		41, #3727
		43, #3869
		52, #4363
		53, #4686
		58, #4861
		60, #O  3  5007
		66, #O  1  6300
		69, #H  1  6563
		70, #N  2  6584
		75, #AR 3  7135
		109, #Ne V 14.32
		100, #N 3 57.21m
		101, #O I 63
		105, # O III 88
		97 #C II 158
		] 

plotstitles = [
		
		"O IV $\lambda$1034",
		"N V $\lambda$1240", 	
		"C IV $\lambda$1549",
		"C III $\lambda$2297",
		"Mg II $\lambda$2798",
		"[Ne V] $\lambda$3426",
		"[O II] $\lambda$3727",
		"[Ne III] $\lambda$3869",
		"[O III] $\lambda$4363",
		"He II $\lambda$4686",
		"H $\\beta$ $\lambda$4861",
		"[O III] $\lambda$5007",
		"[O I] $\lambda$6300",
		"H $\\alpha$ $\lambda$6563", 
		"[N II] $\lambda$6584",
		"[Ar III] $\lambda$7135",
		"[Ne V] $\lambda$14.3$\mu$m",

		"[N III] $\lambda$57.2$\mu$m",
		"[O I] $\lambda$63$\mu$m",
		"[O III] $\lambda$88$\mu$m",
		"[C II] $\lambda$158$\mu$m"

		]

#create z array for this plot with given lines
z = concatenated_data[:,line[:]]

# ---------------------------------------------------
# Interpolate
print "starting interpolation"
xi, yi = linspace(x.min(), x.max(), 11), linspace(y.min(), y.max(), 16) 
xi, yi = meshgrid(xi, yi)
# ---------------------------------------------------
print "interpolatation complete; now plotting"
#plot
plt.subplots_adjust(wspace=0, hspace=0) #remove space between plots
levels = arange(10**-1,10, .2)
levels2 = arange(10**-2,10**2, 1)
plt.suptitle("Baseline Model", fontsize=30)
# ---------------------------------------------------

for i in range(22):
	add_sub_plot(i)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,1).add_patch(patch3)
plt.subplot(3,7,1).add_patch(patch2)
plt.subplot(3,7,1).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,4).add_patch(patch3)
plt.subplot(3,7,4).add_patch(patch2)
plt.subplot(3,7,4).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,7).add_patch(patch3)
plt.subplot(3,7,7).add_patch(patch2)
plt.subplot(3,7,7).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,8).add_patch(patch3)
plt.subplot(3,7,8).add_patch(patch2)
plt.subplot(3,7,8).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,11).add_patch(patch3)
plt.subplot(3,7,11).add_patch(patch2)
plt.subplot(3,7,11).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,14).add_patch(patch3)
plt.subplot(3,7,14).add_patch(patch2)
plt.subplot(3,7,14).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,15).add_patch(patch3)
plt.subplot(3,7,15).add_patch(patch2)
plt.subplot(3,7,15).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,18).add_patch(patch3)
plt.subplot(3,7,18).add_patch(patch2)
plt.subplot(3,7,18).add_patch(patch)

patch3 = patches.PathPatch(path3, facecolor='yellow', lw=0)
patch2 = patches.PathPatch(path2, facecolor='green', lw=0)
patch = patches.PathPatch(path, facecolor='red', lw=0)

plt.subplot(3,7,21).add_patch(patch3)
plt.subplot(3,7,21).add_patch(patch2)
plt.subplot(3,7,21).add_patch(patch)

#ax.set_xlabel('Log($n _{\mathrm{H}}  $)')
#ax.set_ylabel('Log ($ \phi  _{\mathrm{H}}  $)')



print "figure complete"

plt.savefig('Poster_fig.pdf')


plt.show()
plt.clf()
print "figure saved"


