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
def add_sub_plot(sub_num, desiredline):

	plt.subplot(2,2,sub_num)
	
	plt.scatter(xvals, peaks[desiredline], c ='b', s = 30)
	plt.xlim(min(xvals),max(xvals))
	plt.ylim(0,4) 
	#	plt.ylim(0,max(peaks[desiredline])+1)  #took this out because creates different scales which is confusing
	plt.title(headers[desiredline], fontsize = 12)

	if sub_num in [1,3]:
		plt.ylabel('Peak Equivalent Width')
	if sub_num in [1,2]:
		plt.tick_params(labelbottom = 'off')
	else:
		plt.xlabel('Age (millions of years)')

# ---------------------------------------------------

#input files
for file in os.listdir('.'):
    if file.endswith(".0"):
    	inputfile0 = file


for file in os.listdir('.'):
    if file.endswith(".2"):
    	inputfile2 = file

for file in os.listdir('.'):
    if file.endswith(".4"):
    	inputfile4 = file

for file in os.listdir('.'):
    if file.endswith(".5"):
    	inputfile5 = file

for file in os.listdir('.'):
    if file.endswith(".6"):
    	inputfile6 = file

for file in os.listdir('.'):
    if file.endswith(".txt"):
    	headers = file
# ---------------------------------------------------
lines0 = [];
with open(inputfile0, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines0.append(row);
	lines0  = asarray(lines0)

lines2 = [];
with open(inputfile2, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	for row in csvReader:
		lines2.append(row);
	lines2  = asarray(lines2)

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

dataEmissionlines = [];
with open(headers, 'rb') as f:
	csvReader = csv.reader(f,delimiter='\t')
	headers = csvReader.next()
	for row in csvReader:
		dataEmissionlines.append(row);		
	dataEmissionlines  = asarray(dataEmissionlines)
print "import files complete"


#create an array full of the peak values. the columns represent the times (0,2,4,5,6)
peaks = zeros((len(lines6),5))

peaks[:,0] = lines0[:,0]
peaks[:,1] = lines2[:,0]
peaks[:,2] = lines4[:,0]
peaks[:,3] = lines5[:,0]
peaks[:,4] = lines6[:,0]


headers = headers[1:] #the first is #linelist so let's make sure this will work

xvals = [0,2,4,5,6]

print "data arraged"

desired = [60,69,70,76] #this is where you should specify which lines you'd like to plot

for i in range(4):
	add_sub_plot(i,desired[i-1]) #add our subplots with desired lines (calls routine add subplot)

plt.suptitle("Peak Equivalent Widths", fontsize = 15)
plt.show()
plt.savefig('Peak_Eqwidths.pdf')



