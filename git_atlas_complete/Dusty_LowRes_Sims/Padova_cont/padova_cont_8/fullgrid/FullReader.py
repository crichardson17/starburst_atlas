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
# ------------------------------------------------------------------------------------------------------
#input data files loaded in here
print "Starting"
numFiles = 3
gridfile = [None]*numFiles
Elines = [None]*numFiles

for i in range(3):
	for file in os.listdir('.'):
		if file.endswith("padova_cont_{:d}.grd".format(i+1)):
			gridfile[i] = file
			print file
		if file.endswith("padova_cont_{:d}.txt".format(i+1)):
			Elines[i] = file
			print file
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

#the add subplot routine
def add_sub_plot(sub_num, elinesplot):
	numplots = 16
	plt.subplot(numplots/4.,4,sub_num) #define rows and columns by desired amount of subplots
	
	rbf = scipy.interpolate.Rbf(x, y, z[elinesplot][:,sub_num-1], function='linear')
	zi = rbf(xi, yi)
	
	contour = plt.contour(xi,yi,zi, levels, colors='c', linestyles = 'dashed') #teal contours, dashed
	contour2 = plt.contour(xi,yi,zi, levels2, colors='k', linewidths=1.5) #black contours, solid
	
	plt.scatter(max_values[line[elinesplot][sub_num-1],2], max_values[line[elinesplot][sub_num-1],3], c ='k',marker = '*')
	plt.annotate(headers[line[elinesplot][sub_num-1]], xy=(8,11),  xytext=(4.5,8.5), fontsize = 10)
	plt.annotate(max_values[line[elinesplot][sub_num-1],0], xy = (max_values[line[elinesplot][sub_num-1],2], max_values[line[elinesplot][sub_num-1],3]), xytext = (0, -10), textcoords = 'offset points', ha = 'right', va = 'bottom', fontsize=10)
	
	#if sub_num == numplots / 2.:
	print " --- {:d} of the sub-plots of plot{:d} are complete".format(sub_num+1, elinesplot+1)
#axis limits

	yt_min = 8
	yt_max = 23
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
print "import files complete"
# ---------------------------------------------------
headers = ["C III $\lambda$977",
"N III $\lambda$991",
"H I $\lambda$1026",
"O IV $\lambda$1035",
"Incident $\lambda$1215",
"H I $\lambda$1216",
"N V $\lambda$1239", 
"N V $\lambda$1240",
"N V $\lambda$1243",
"Si II $\lambda$1263",
"O I $\lambda$1304",
"Si II $\lambda$1308",
"Si IV $\lambda$1397",
"O IV] $\lambda$1402",
"S IV $\lambda$1406",
"N IV  $\lambda$1485",
"N IV $\lambda$1486",
"Si II $\lambda$1531",	
"C IV $\lambda$1549",
"He II $\lambda$1640",
"O III] $\lambda$1665",
"Al II $\lambda$1671",
"N  4  1719A",
"N III] $\lambda$1750", 
"Al III $\lambda$1860",
"Si III] $\lambda$1888",
"C III] $\lambda$1907",
"TOTL  1909A",
"C III $\lambda$2297",
"[O III] $\lambda$2321",
"[O II] $\lambda$2471",
"C II] $\lambda$2326",
"Si II] $\lambda$2335",
"Al II] $\lambda$2665",
"Mg II $\lambda$2798",
"Mg II $\lambda$2803",	
"[Ne III] $\lambda$3343",
"[Ne V] $\lambda$3426",
"Balmer Cont.",
"Balmer Jump $\lambda$3646",
"[O II] $\lambda$3726",
"[O II] $\lambda$3727",
"[O II] $\lambda$3729",
"[Ne III] $\lambda$3869",
"H I $\lambda$3889",
"Ca II $\lambda$3933",
"He I $\lambda$4026",
"[S II] $\lambda$4070",
"[S II] $\lambda$4074",
"[S II] $\lambda$4078",
"H I $\lambda$4102",
"H I $\lambda$4340",
"[O III] $\lambda$4363",
"He II $\lambda$4686",
"CA B  4686A",
"[Ar IV] $\lambda$4711",
"[Ne IV] $\lambda$4720",
"[Ar IV] $\lambda$4740",
"Incident  $\lambda$4860",
"H $\\beta$ $\lambda$4861",
"[O III] $\lambda$4959",
"[O III] $\lambda$5007",
"[N I] $\lambda$5200",
"FE14  5303A",
"[O I] $\lambda$5577",
"[N II] $\lambda$5755",
"He I $\lambda$5876",
"[O I] $\lambda$6300",
"[S III] $\lambda$6312",
"[O I] $\lambda$6363",
"H $\\alpha$ $\lambda$6563",
"[N II] $\lambda$6584",
"[S II] $\lambda$6716",
"[S II] $\lambda$6720",
"[S II] $\lambda$6731",
"AR 5  7005A",
"[Ar III] $\lambda$7135",
"[O II] $\lambda$7325",
"[Ar IV] $\lambda$7331",
"[Ar III] $\lambda$7751",
"O I $\lambda$8446",
"Ca II $\lambda$8498",
"Ca II $\lambda$8542",
"Ca II $\lambda$8662",
"Ca II $\lambda$8579",
"[S III] $\lambda$9069",
"Pa9 $\lambda$9229",
"[S III] $\lambda$9532",
"Pa $\\epsilon$ $\lambda$9546",
"He I $\lambda$1.083$\mu$m",
"H I $\lambda$1.875$\mu$m",
"H I $\lambda$1.282$\mu$m",
"H I $\lambda$1.094$\mu$m",
"H I $\lambda$1.005$\mu$m",
"H I $\lambda$4.051$\mu$m",
"H I $\lambda$2.625$\mu$m",
"H  1 2.166m",
"H  1 1.945m",
"C II $\lambda$157.6$\mu$m",
"N II $\lambda$121.7$\mu$m",
"N II $\lambda$205.4$\mu$m",
"[N III] $\lambda$57.2$\mu$m",
"[O I] $\lambda$63$\mu$m",
"[O I] $\lambda$145.5$\mu$m",
"O III $\lambda$51.80$\mu$m",
"[O III] $\lambda$88$\mu$m",
"O IV $\lambda$25.88$\mu$m",
"Ne II $\lambda$12.81$\mu$m",
"Ne III $\lambda$15.55$\mu$m",
"Ne III $\lambda$36.01$\mu$m",
"[Ne V] $\lambda$14.3$\mu$m",
"Ne V $\lambda$24.31$\mu$m",
"Ne VI $\lambda$7.652$\mu$m",
"Na III $\lambda$7.320$\mu$m",
"NA 4 9.039m",
"NA 4 21.29m",
"NA 6 14.40m",
"NA 6 8.611m",
"MG 4 4.485m",
"MG 5 5.610m",
"MG 5 13.52m",
"MG 7 5.503m",
"MG 7 9.033m",
"MG 8 3.030m",
"AL 5 2.905m",
"AL 6 3.660m",
"AL 6 9.116m",
"AL 8 5.848m",
"AL 8 3.690m",
"SI 2 34.81m",
"SI 6 1.963m",
"SI 7 2.481m",
"SI 7 6.492m",
"SI 9 3.929m",
"SI 9 2.584m",
"SI10 1.430m",
"S  3 18.67m",
"S  3 33.47m",
"S  4 10.51m",
"S  8  9914A",
"S  9 1.252m",
"S  9 3.754m",
"S 11 1.920m",
"S 11 1.393m",
"AR 2 6.980m",
"AR 3 9.000m",
"AR 3 21.83m",
"AR 5 8.000m",
"AR 5 13.10m",
"AR 6 4.530m",
"AR10  5534A",
"AR11 2.595m",
"CA 4 3.210m",
"CA 5 4.157m",
"CA 5 11.48m",
"CA 8 2.321m",
"SC 5 2.310m",
"TI 6 1.715m",
"V  7 1.304m",
"CR 8 1.011m",
"MN 9  7968A",
"CO11  5168A",
"NI12  4231A",
"O  3  1661A",
"O  3  1666A",
"[O V] $\lambda$1218",
"SI 3  1892A",
"TOTL  2335A"]

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
		[0, #977
		1, #991
		2, #1026
		5, #1216
		91, #1218
		6, #1239
		7, #1240
		8, #1243
		9, #1263
		10, #1304
		11,#1308
		12, #1397
		13, #1402
		14, #1406
		16, #1486
		17], #1531

		#UV2line 
		[18, #1549
		19, #1640
		20, #1665
		21, #1671
		23, #1750
		24, #1860
		25, #1888
		26, #1907
		27, #2297
		28, #2321
		29, #2471
		30, #2326
		31, #2335
		32, #2665
		33, #2798
		34],
		
		#Optical Lines
		[36, #NE 3  3343A
		38, #BA C
		39, #3646
		40, #3726
		41, #3727
		42, #3729
		43, #3869
		44, #3889
		45, #3933
		46, #4026
		47, #4070
		48, #4074
		49, #4078
		50, #4102
		51, #4340
		52], #4363

		#Optical Lines 2
		[56, #AR 4  4740
		58, #4861
		59, #O III 4959
		60, #O  3  5007
		61, #N  1  5200
		63, #O  1  5577
		64, #N  2  5755
		65, #HE 1  5876
		66, #O  1  6300
		67, #S  3  6312
		68, #O  1  6363
		69, #H  1  6563
		70, #N  2  6584
		71, #S II  6716
		72, #S  2  6720
		73], #S II  6731
		
		#IR Lines
		[75, #AR 3  7135
		76, #TOTL  7325
		77,
		78, #AR 3  7751
		79, #6LEV  8446
		80, #CA2X  8498
		81, #CA2Y  8542
		82, #CA2Z  8662
		83, #CA 2  8579A
		84, #S  3  9069
		85, #H  1  9229
		86, #S  3  9532
		87,
		88,
		89,
		90], #H  1  9546

		#Rest Lines
		[3,4,15,22,37,53,54,55,58,63,78,89,90,91,93,94],

		#More Lines
		[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112],

		#More Lines 2
		[113,114,115,116,117,118,119,120,121,122,123,124,125,126,127]
		] 


#create z array for this plot
z = [concatenated_data[:,line[0]],concatenated_data[:,line[1]], concatenated_data[:,line[2]], concatenated_data[:,line[3]], concatenated_data[:,line[4]], concatenated_data[:,line[5]], concatenated_data[:,line[6]], concatenated_data[:,line[7]]]

# ---------------------------------------------------
# Interpolate
print "starting interpolation"
xi, yi = linspace(x.min(), x.max(), (x.max()-x.min())), linspace(y.min(), y.max(), (y.max()-y.min())) 
xi, yi = meshgrid(xi, yi)
# ---------------------------------------------------
#plot
plt.subplots_adjust(wspace=0, hspace=0) #remove space between plots
levels = arange(10**-1,10, .2)
levels2 = arange(10**-2,10**2, 1)
# ---------------------------------------------------

plt.clf()
for j in range (7): 
	for i in range(16):
		add_sub_plot(i,j)
	ax1 = plt.subplot(4,4,1)
	add_patches(ax1)
	print "plot {:d} complete".format(j+1)
	plt.savefig(("Full_lines_%d.pdf")%j)
	plt.clf()
