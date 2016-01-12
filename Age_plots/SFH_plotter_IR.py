############################################################
########## Plotting File for SFH comparison Plots ##########
################## Data read from Cloudy ###################
################ Helen Meskhidze, Fall 2015 ################
#################### Elon University #######################
#------------------------------------------------------------------------------------------------------
'''
The inputs this code takes are the peaks files exported by my peaksreader.py
This code outputs IR SFH comparison plots, saved to the working directory
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
# ---------------------------------------------------
#red for Padova; black for Geneva
color1 = "#e50000" #red
color2 = "#000000" #black

plt.subplots_adjust(wspace=0, hspace=1) #remove space between plots

#subplot routine
def add_sub_plot(sub_num, desiredline):
	
	plt.subplot(4,4,sub_num)
	plt.scatter(xvals, peakspadcont[desiredline], c =color1, s = 8)
	plt.plot(xvals, peakspadcont[desiredline], c =color1, label="Padova Continuous")

	plt.scatter(xvals, peakspadinst[desiredline], c =color1, s = 8)
	plt.plot(xvals, peakspadinst[desiredline], c =color1, linestyle='dotted',  label="Padova Instantaneous")

	plt.scatter(xvals, peaksgencont[desiredline], c =color2, s = 8)
	plt.plot(xvals, peaksgencont[desiredline], c =color2, label="Geneva Continuous")

	plt.scatter(xvals, peaksgeninst[desiredline], c =color2, s = 8)
	plt.plot(xvals, peaksgeninst[desiredline], c =color2, linestyle='dotted', label = "Geneva Instantaneous")

	#plt.legend(prop={'size':4}, loc=3)

	plt.xlim(min(xvals),max(xvals))
	plt.ylim(0,3.5) 
	plt.xticks(arange(0,8,1),fontsize=6)
	plt.yticks(arange(0,3.5,.5),fontsize=6)


	if sub_num in [1, 2,3,4]:
		plt.tick_params(labelleft = 'off')
		plt.tick_params(labelbottom = 'on')
		plt.xlabel('Age (Myr)', fontsize=6)
		plt.annotate(headers[desiredline], xy=(0.1,0.05),  xytext=(0.1,0.05), fontsize = 6)


	if sub_num in [5,6,7,8]:
		plt.tick_params(labelleft = 'off')
		plt.xlabel('Age (Myr)', fontsize=6)
		plt.annotate(headers[desiredline], xy=(0.1,0.05),  xytext=(0.1,0.05), fontsize = 6)
	
	if sub_num in [9,10,11,12]:
		plt.tick_params(labelleft = 'off')
		plt.xlabel('Age (Myr)', fontsize=6)
		plt.annotate(headers[desiredline], xy=(0.1,0.05),  xytext=(0.1,0.05), fontsize = 6)


	if sub_num == 1:
		plt.ylabel('log($W _{\lambda}$)', fontsize=6)
		plt.tick_params(labelleft = 'on')

	if sub_num == 5:
		plt.xlabel('Age (Myr)', fontsize=6)
		plt.ylabel('log($W _{\lambda}$)', fontsize=6)
		plt.tick_params(labelleft = 'on')

	if sub_num == 9:
		plt.xlabel('Age (Myr)', fontsize=6)
		plt.ylabel('log($W _{\lambda}$)', fontsize=6)
		plt.tick_params(labelleft = 'on')

	if sub_num in [4,8,12]:
		plt.xticks(arange(0,9,1),fontsize=6)
	

	if sub_num == 6:
		figtext(.5,.95,'Strong IR Emission Lines', fontsize=8, ha='center')
	if sub_num == 10:
		figtext(.5,.485,'Fine Structure Lines', fontsize=8, ha='center')
	
	if sub_num == 1:
		plt.legend(bbox_to_anchor=(0., 1.2, 4., 0), loc=1, ncol=4, mode="expand", prop={'size':6}, borderaxespad=0.)

	if sub_num == 5:
		plt.legend(bbox_to_anchor=(0., 1.2, 4., 0), loc=1, ncol=4, mode="expand", prop={'size':6}, borderaxespad=0.)
	if sub_num == 9:
		plt.legend(bbox_to_anchor=(0., 1.2, 4., 0), loc=1, ncol=4, mode="expand", prop={'size':6}, borderaxespad=0.)


# ---------------------------------------------------
numFiles = 5

gridFiles = [None]*numFiles
emissionFiles = [None]*numFiles


#input files
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevacont0"):
    	inputfile0 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevacont2"):
    	inputfile1 = file  
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevacont4"):
    	inputfile2 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevacont5"):
    	inputfile3 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevacont6"):
    	inputfile4 = file

for file in os.listdir('./data'):
    if file.endswith("peaks_Genevacont8"):
    	inputfile20 = file

for file in os.listdir('./data'):
    if file.endswith("peaks_Genevainst0"):
    	inputfile5 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevainst2"):
    	inputfile6 = file  
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevainst4"):
    	inputfile7 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevainst5"):
    	inputfile8 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevainst6"):
    	inputfile9 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Genevainst8"):
    	inputfile21 = file

for file in os.listdir('./data'):
    if file.endswith("peaks_Padovainst0"):
    	inputfile10 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovainst2"):
    	inputfile11 = file  
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovainst4"):
    	inputfile12 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovainst5"):
    	inputfile13 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovainst6"):
    	inputfile14 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovainst8"):
    	inputfile22 = file

for file in os.listdir('./data'):
    if file.endswith("peaks_Padovacont0"):
        inputfile15 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovacont2"):
        inputfile16 = file  
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovacont4"):
        inputfile17 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovacont5"):
        inputfile18 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovacont6"):
        inputfile19 = file
for file in os.listdir('./data'):
    if file.endswith("peaks_Padovacont8"):
        inputfile23 = file
# importing headers file

for file in os.listdir('./'):
    if file.endswith(".txt"):
    	headers = file

# ---------------------------------------------------

os.chdir("./data")

lines0 = [];
with open(inputfile0, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines0.append(row);
	lines0  = asarray(lines0)

lines1 = [];
with open(inputfile1, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines1.append(row);
	lines1  = asarray(lines1)

lines2 = [];
with open(inputfile2, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines2.append(row);
	lines2  = asarray(lines2)

lines3 = [];
with open(inputfile3, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines3.append(row);
	lines3  = asarray(lines3)

lines4 = [];
with open(inputfile4, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines4.append(row);
	lines4  = asarray(lines4)

lines5 = [];
with open(inputfile5, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines5.append(row);
	lines5  = asarray(lines5)

lines6 = [];
with open(inputfile6, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines6.append(row);
	lines6  = asarray(lines6)

lines7 = [];
with open(inputfile7, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines7.append(row);
	lines7  = asarray(lines7)

lines8 = [];
with open(inputfile8, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines8.append(row);
	lines8  = asarray(lines8)

lines9 = [];
with open(inputfile9, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines9.append(row);
	lines9  = asarray(lines9)


lines10 = [];
with open(inputfile10, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines10.append(row);
	lines10 = asarray(lines10)

lines11 = [];
with open(inputfile11, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines11.append(row);
	lines11 = asarray(lines11)

lines12 = [];
with open(inputfile12, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines12.append(row);
	lines12 = asarray(lines12)

lines13 = [];
with open(inputfile13, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines13.append(row);
	lines13 = asarray(lines13)

lines14 = [];
with open(inputfile14, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines14.append(row);
	lines14 = asarray(lines14)

lines15 = [];
with open(inputfile15, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines15.append(row);
	lines15 = asarray(lines15)

lines16 = [];
with open(inputfile16, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines16.append(row);
	lines16 = asarray(lines16)

lines17 = [];
with open(inputfile17, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines17.append(row);
	lines17 = asarray(lines17)

lines18 = [];
with open(inputfile18, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines18.append(row);
	lines18 = asarray(lines18)

lines19 = [];
with open(inputfile19, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines19.append(row);
	lines19 = asarray(lines19)

lines20 = [];
with open(inputfile20, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines20.append(row);
	lines20 = asarray(lines20)

lines21 = [];
with open(inputfile21, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines21.append(row);
	lines21 = asarray(lines21)
lines22 = [];
with open(inputfile22, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines22.append(row);
	lines22 = asarray(lines22)
lines23 = [];
with open(inputfile23, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines23.append(row);
	lines23 = asarray(lines23)

dataEmissionlines = [];

os.chdir("../")
with open(headers, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		dataEmissionlines.append(row);		
	dataEmissionlines  = asarray(dataEmissionlines)
print "import files complete"


# ---------------------------------------------------

#create an array full of the peak values. the columns represent the times (0,2,4,5,6)
peakspadcont = zeros((len(lines6),6))
peakspadinst = zeros((len(lines6),6))
peaksgencont = zeros((len(lines6),6))
peaksgeninst = zeros((len(lines6),6))

peaksgencont[:,0] = lines0[:,0]
peaksgencont[:,1] = lines1[:,0]
peaksgencont[:,2] = lines2[:,0]
peaksgencont[:,3] = lines3[:,0]
peaksgencont[:,4] = lines4[:,0]
peaksgencont[:,5] = lines20[:,0]

peaksgeninst[:,0] = lines5[:,0]
peaksgeninst[:,1] = lines6[:,0]
peaksgeninst[:,2] = lines7[:,0]
peaksgeninst[:,3] = lines8[:,0]
peaksgeninst[:,4] = lines9[:,0]
peaksgeninst[:,5] = lines21[:,0]

peakspadinst[:,0] = lines10[:,0]
peakspadinst[:,1] = lines11[:,0]
peakspadinst[:,2] = lines12[:,0]
peakspadinst[:,3] = lines13[:,0]
peakspadinst[:,4] = lines14[:,0]
peakspadinst[:,5] = lines22[:,0]

peakspadcont[:,0] = lines15[:,0]
peakspadcont[:,1] = lines16[:,0]
peakspadcont[:,2] = lines17[:,0]
peakspadcont[:,3] = lines18[:,0]
peakspadcont[:,4] = lines19[:,0]
peakspadcont[:,5] = lines23[:,0]


headers = headers[1:] #the first is #linelist so let's make sure this will work

xvals = [0,2,4,5,6,8]

print "data arraged"
# ---------------------------------------------------

#below is where you should specify which lines you'd like to plot
desired = [76,77,79,80,
			85,87,88,89, 
			104, 102, 105, 98] 

plt.clf()
for i in range(12):
	add_sub_plot(i+1,desired[i])

plt.savefig('SFH_Comp_IR.pdf')
print "plot saved and complete"
