
############################################################
################## Plotting File for SEDs  #################
################## Data read from Cloudy ###################
################ Helen Meskhidze, Fall 2015 ################
#################### Elon University #######################
#------------------------------------------------------------------------------------------------------
'''
The inputs this code takes are .con files from Cloudy. 
This code outputs SED plots to the working dir.
'''
#------------------------------------------------------------------------------------------------------
#Begin with packages
import csv
import matplotlib.pyplot as plt
from numpy import *
import math 
#------------------------------------------------------------------------------------------------------

#set figure size 
plt.figure(figsize=(20,12))
plt.subplots_adjust(wspace=.08, hspace=.08)

# The user must set this to the directory and file that needs to be read in.

inputfile1 = 'Rotation_inst_1.con'
inputfile2 = 'Rotation_inst_2.con'
inputfile3 = 'Rotation_inst_3.con'
inputfile4 = 'Rotation_inst_4.con'
inputfile5 = 'Rotation_inst_5.con'
inputfile6 = 'Rotation_inst_6.con'


inputfile7 = 'Rotation_cont_1.con'
inputfile8 = 'Rotation_cont_2.con'
inputfile9 = 'Rotation_cont_3.con'
inputfile10 = 'Rotation_cont_4.con'
inputfile11 = 'Rotation_cont_5.con'
inputfile12 = 'Rotation_cont_6.con'

inputfile13 = 'NoRotation_inst_1.con'
inputfile14 = 'NoRotation_inst_2.con'
inputfile15 = 'NoRotation_inst_3.con'
inputfile16 = 'NoRotation_inst_4.con'
inputfile17 = 'NoRotation_inst_5.con'
inputfile18 = 'NoRotation_inst_6.con'

inputfile19 = 'NoRotation_cont_1.con'
inputfile20 = 'NoRotation_cont_2.con'
inputfile21 = 'NoRotation_cont_3.con'
inputfile22 = 'NoRotation_cont_4.con'
inputfile23 = 'NoRotation_cont_5.con'
inputfile24 = 'NoRotation_cont_6.con'


inputfile25 = 'padova_inst_1.con'
inputfile26 = 'padova_inst_2.con'
inputfile27 = 'padova_inst_3.con'
inputfile28 = 'padova_inst_4.con'
inputfile29 = 'padova_inst_5.con'
inputfile30 = 'padova_inst_6.con'


inputfile31 = 'padova_cont_1.con'
inputfile32 = 'padova_cont_2.con'
inputfile33 = 'padova_cont_3.con'
inputfile34 = 'padova_cont_4.con'
inputfile35 = 'padova_cont_5.con'
inputfile36 = 'padova_cont_6.con'

#-------------------------------------------------------------
#reading in the files
datastarburst1 = [];
with open(inputfile1, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst1.append(row);
    datastarburst1 = asarray(datastarburst1)


datastarburst2 = [];
with open(inputfile2, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst2.append(row);
    datastarburst2 = asarray(datastarburst2)

datastarburst3 = [];
with open(inputfile3, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst3.append(row);
    datastarburst3 = asarray(datastarburst3)

datastarburst4 = [];
with open(inputfile4, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst4.append(row);
    datastarburst4 = asarray(datastarburst4)

datastarburst5 = [];
with open(inputfile5, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst5.append(row);
    datastarburst5 = asarray(datastarburst5)

datastarburst6 = [];
with open(inputfile6, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst6.append(row);
    datastarburst6 = asarray(datastarburst6)


#-------------------------------------------------------------
datastarburst7 = [];
with open(inputfile7, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst7.append(row);
    datastarburst7 = asarray(datastarburst7)


datastarburst8 = [];
with open(inputfile8, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst8.append(row);
    datastarburst8 = asarray(datastarburst8)

datastarburst9 = [];
with open(inputfile9, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst9.append(row);
    datastarburst9 = asarray(datastarburst9)

datastarburst10 = [];
with open(inputfile10, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst10.append(row);
    datastarburst10 = asarray(datastarburst10)

datastarburst11 = [];
with open(inputfile11, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst11.append(row);
    datastarburst11= asarray(datastarburst11)

datastarburst12 = [];
with open(inputfile12, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst12.append(row);
    datastarburst12 = asarray(datastarburst12)

#-------------------------------------------------------------
datastarburst13 = [];
with open(inputfile13, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst13.append(row);
    datastarburst13 = asarray(datastarburst13)


datastarburst14 = [];
with open(inputfile14, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst14.append(row);
    datastarburst14 = asarray(datastarburst14)

datastarburst15 = [];
with open(inputfile15, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst15.append(row);
    datastarburst15 = asarray(datastarburst15)

datastarburst16 = [];
with open(inputfile16, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst16.append(row);
    datastarburst16 = asarray(datastarburst16)

datastarburst17 = [];
with open(inputfile17, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst17.append(row);
    datastarburst17 = asarray(datastarburst17)

datastarburst18 = [];
with open(inputfile18, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst18.append(row);
    datastarburst18 = asarray(datastarburst18)


#-------------------------------------------------------------
datastarburst19 = [];
with open(inputfile19, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst19.append(row);
    datastarburst19 = asarray(datastarburst19)


datastarburst20 = [];
with open(inputfile20, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst20.append(row);
    datastarburst20 = asarray(datastarburst20)

datastarburst21 = [];
with open(inputfile21, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst21.append(row);
    datastarburst21 = asarray(datastarburst21)

datastarburst22 = [];
with open(inputfile22, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst22.append(row);
    datastarburst22 = asarray(datastarburst22)


datastarburst23 = [];
with open(inputfile23, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst23.append(row);
    datastarburst23 = asarray(datastarburst23)

datastarburst24 = [];
with open(inputfile23, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst24.append(row);
    datastarburst24 = asarray(datastarburst24)


#-------------------------------------------------------------

datastarburst25 = [];
with open(inputfile25, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst25.append(row);
    datastarburst25 = asarray(datastarburst25)


datastarburst26 = [];
with open(inputfile26, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst26.append(row);
    datastarburst26 = asarray(datastarburst26)

datastarburst27 = [];
with open(inputfile27, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst27.append(row);
    datastarburst27 = asarray(datastarburst27)

datastarburst28 = [];
with open(inputfile28, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst28.append(row);
    datastarburst28 = asarray(datastarburst28)

datastarburst29 = [];
with open(inputfile29, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst29.append(row);
    datastarburst29 = asarray(datastarburst29)

datastarburst30 = [];
with open(inputfile30, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst30.append(row);
    datastarburst30 = asarray(datastarburst30)
#-------------------------------------------------------------

datastarburst31 = [];
with open(inputfile31, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst31.append(row);
    datastarburst31 = asarray(datastarburst31)


datastarburst32 = [];
with open(inputfile32, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst32.append(row);
    datastarburst32 = asarray(datastarburst32)

datastarburst33 = [];
with open(inputfile33, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst33.append(row);
    datastarburst33 = asarray(datastarburst33)

datastarburst34 = [];
with open(inputfile34, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst34.append(row);
    datastarburst34 = asarray(datastarburst34)

datastarburst35 = [];
with open(inputfile35, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst35.append(row);
    datastarburst35 = asarray(datastarburst35)

datastarburst36 = [];
with open(inputfile36, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst36.append(row);
    datastarburst36 = asarray(datastarburst36)

#-------------------------------------------------------------
    
# Extract x and y from the first two columns of the array.

x  = double(datastarburst1[:3950,0])
#if eV is desired, uncomment the following:
for i in range(len(x)):
    x[i] = 1.240/x[i]

x1  = double(datastarburst1[:4030,0])
#if eV is desired, uncomment the following:
for i in range(len(x1)):
    x1[i] = 1.240/x1[i]

x2  = double(datastarburst1[:3970,0])
#if eV is desired, uncomment the following:
for i in range(len(x2)):
    x2[i] = 1.240/x2[i]

x3  = double(datastarburst1[:4108,0])
#if eV is desired, uncomment the following:
for i in range(len(x3)):
    x3[i] = 1.240/x3[i]

x4  = double(datastarburst1[:4069,0])
#if eV is desired, uncomment the following:
for i in range(len(x4)):
    x4[i] = 1.240/x4[i]
x5  = double(datastarburst1[:3960,0])
#if eV is desired, uncomment the following:
for i in range(len(x5)):
    x5[i] = 1.240/x5[i]

x6  = double(datastarburst28[:4147,0])
#if eV is desired, uncomment the following:
for i in range(len(x6)):
    x6[i] = 1.240/x6[i]

y1  = double(datastarburst1[:4108,1])
y2  = double(datastarburst2[:4108,1])
y3  = double(datastarburst3[:4030,1])
y4  = double(datastarburst4[:4030,1])
y5  = double(datastarburst5[:4030,1])
y6  = double(datastarburst6[:3970,1])

y7  = double(datastarburst7[:4108,1])
y8  = double(datastarburst8[:4108,1])
y9  = double(datastarburst9[:4108,1])
y10  = double(datastarburst10[:4108,1])
y11  = double(datastarburst11[:4108,1])
y12  = double(datastarburst12[:4108,1])

y13  = double(datastarburst13[:4069,1])
y14  = double(datastarburst14[:4069,1])
y15  = double(datastarburst15[:4030,1])
y16  = double(datastarburst16[:3960,1])
y17  = double(datastarburst17[:3960,1])
y18  = double(datastarburst18[:3960,1])

y19  = double(datastarburst19[:4108,1])
y20  = double(datastarburst20[:4108,1])
y21  = double(datastarburst21[:4108,1])
y22  = double(datastarburst22[:4108,1])
y23  = double(datastarburst23[:4108,1])
y24  = double(datastarburst24[:4108,1])

y25  = double(datastarburst25[:4069,1])
y26  = double(datastarburst26[:4030,1])
y27  = double(datastarburst27[:4108,1])
y28  = double(datastarburst28[:4147,1])
y29  = double(datastarburst29[:4147,1])
y30  = double(datastarburst30[:4147,1])

y31  = double(datastarburst31[:4030,1])
y32  = double(datastarburst32[:4030,1])
y33  = double(datastarburst33[:4147,1])
y34  = double(datastarburst34[:4147,1])
y35  = double(datastarburst35[:4147,1])
y36  = double(datastarburst36[:4147,1])

#there are specific values here because for some reason some of the outputs were shorter (perhaps the end temp was reached faster in some) they only differed by about 100 so I've cut them off

#-------------------------------------------------------------
# Plot x vs. y in 4 subplots

fig = plt.figure(1)
sp5 = plt.subplot(325) #rows columns location of this parcticular plot
p1 = plt.plot(x3,y1, 'k', linewidth=.75, label="1 Myr")
p2 = plt.plot(x3,y2, 'c', linewidth=.75, label="2 Myr")
p3 = plt.plot(x1,y3, 'y', linewidth=.75, label="3 Myr")
p4 = plt.plot(x1,y4, 'r', linewidth=.75, label="4 Myr")
p5 = plt.plot(x1,y5, 'g', linewidth=.75, label="5 Myr")
p6 = plt.plot(x2,y6, 'b', linewidth=.75, label="6 Myr")

plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$h$$\nu$ [$\rm{eV}$]', fontsize = 18)



sp5.text(.5,.9,"Geneva Track Instantaneous with Rotation", horizontalalignment="center", transform = sp5.transAxes, fontsize = 16)


plt.ylabel(r'$4 \pi \nu J_\nu$ [$\rm{erg}$ $\mathrm{s}^{-1} \mathrm{cm} ^ {-2}$]', fontsize=18)

plt.legend(prop={'size':11})

#--------------------------------------------------------

sp6 = plt.subplot(326)
p7 = plt.plot(x3,y7, 'k', linewidth=.75, label="1 Myr")
p8 = plt.plot(x3,y8, 'c', linewidth=.75, label="2 Myr")
p9 = plt.plot(x3,y9, 'y', linewidth=.75, label="3 Myr")
p10 = plt.plot(x3,y10, 'r', linewidth=.75, label="4 Myr")
p11 = plt.plot(x3,y11, 'g', linewidth=.75, label="5 Myr")
p12 = plt.plot(x3,y12, 'b', linewidth=.75, label="6 Myr")

plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xscale('log')
plt.yscale('log')

sp6.set_yticklabels([])
plt.xlabel(r'$h$$\nu$ [$\rm{eV}$]', fontsize = 18)

sp6.text(.5,.9,"Geneva Track Continuous with Rotation", horizontalalignment="center", transform = sp6.transAxes, fontsize = 16)



plt.legend(prop={'size':11})


#--------------------------------------------------------
sp3 = plt.subplot(323)
p13 = plt.plot(x4,y13, 'k', linewidth=.75, label="1 Myr")
p14 = plt.plot(x4,y14, 'c', linewidth=.75, label="2 Myr")
p15 = plt.plot(x1,y15, 'y', linewidth=.75, label="3 Myr")
p16 = plt.plot(x5,y16, 'r', linewidth=.75, label="4 Myr")
p17 = plt.plot(x5,y17, 'g', linewidth=.75, label="5 Myr")
p18 = plt.plot(x5,y18, 'b', linewidth=.75, label="6 Myr")


plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)
plt.yticks(fontsize=16)
yt_min = 10**0
yt_max = 10**5
#plt.xticks(fontsize=15)
plt.legend(prop={'size':10})
plt.xscale('log')
plt.yscale('log')
sp3.set_xticklabels([])

plt.ylabel(r'$4 \pi \nu J_\nu$ [$\rm{erg}$ $\mathrm{s}^{-1} \mathrm{cm} ^ {-2}$]', fontsize=18)

sp3.text(.5,.9,"Geneva Track Instantaneous without Rotation", horizontalalignment="center", transform = sp3.transAxes, fontsize = 16)



plt.legend(prop={'size':11})

#--------------------------------------------------------

sp4 = plt.subplot(324)
p19 = plt.plot(x3,y19, 'k', linewidth=.75, label="1 Myr")
p20 = plt.plot(x3,y20, 'c', linewidth=.75, label="2 Myr")
p21 = plt.plot(x3,y21, 'y', linewidth=.75, label="3 Myr")
p22 = plt.plot(x3,y22, 'r', linewidth=.75, label="4 Myr")
p23 = plt.plot(x3,y23, 'g', linewidth=.75, label="5 Myr")
p24 = plt.plot(x3,y24, 'b', linewidth=.75, label="6 Myr")

plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)
#plt.yticks(fontsize=15)
#plt.xticks(fontsize=15)
plt.legend(prop={'size':10})
plt.xscale('log')
plt.yscale('log')
yt_min = 10**0
yt_max = 10**5

sp4.set_xticklabels([])
sp4.set_yticklabels([])

sp4.text(.5,.9,"Geneva Track Continuous without Rotation", horizontalalignment="center", transform = sp4.transAxes, fontsize = 16)


plt.legend(prop={'size':11})

#-------------------------------------------------------------
# Plot x vs. y in 4 subplots

fig = plt.figure(1)

sp1 = plt.subplot(321) #rows columns location of this parcticular plot
p1 = plt.plot(x4,y25, 'k', linewidth=.75, label="1 Myr")
p2 = plt.plot(x1,y26, 'c', linewidth=.75, label="2 Myr")
p3 = plt.plot(x3,y27, 'y', linewidth=.75, label="3 Myr")
p4 = plt.plot(x6,y28, 'r', linewidth=.75, label="4 Myr")
p5 = plt.plot(x6,y29, 'g', linewidth=.75, label="5 Myr")
p6 = plt.plot(x6,y30, 'b', linewidth=.75, label="6 Myr")

plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xscale('log')
plt.yscale('log')
sp1.set_xticklabels([])

sp1.text(.5,.9,"Padova Track Instantaneous",horizontalalignment="center", transform = sp1.transAxes, fontsize = 16)
plt.ylabel(r'$4 \pi \nu J_\nu$ [$\rm{erg}$ $\mathrm{s}^{-1} \mathrm{cm} ^ {-2}$]', fontsize=18)


plt.legend(prop={'size':11})


#-------------------------------------------------------------
# Plot x vs. y in 4 subplots

fig = plt.figure(1)

sp2 = plt.subplot(322) #rows columns location of this parcticular plot
p1 = plt.plot(x1,y31, 'k', linewidth=.75, label="1 Myr")
p2 = plt.plot(x1,y32, 'c', linewidth=.75, label="2 Myr")
p3 = plt.plot(x6,y33, 'y', linewidth=.75, label="3 Myr")
p4 = plt.plot(x6,y34, 'r', linewidth=.75, label="4 Myr")
p5 = plt.plot(x6,y35, 'g', linewidth=.75, label="5 Myr")
p6 = plt.plot(x6,y36, 'b', linewidth=.75, label="6 Myr")

plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)
plt.xticks(fontsize=16)
plt.xscale('log')
plt.yscale('log')
sp2.set_xticklabels([])
sp2.set_yticklabels([])


sp2.text(.5,.9,"Padova Track Continuous", horizontalalignment="center", transform = sp2.transAxes, fontsize = 16)

plt.legend(prop={'size':11})

#-------------------------------------------------------------
#plt.savefig('continuum.png')
#plt.savefig('continuum.ps')
plt.savefig('SED_comparison.pdf')


#plt.clf()

#plt.show()
