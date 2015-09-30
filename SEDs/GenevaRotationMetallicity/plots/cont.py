#Begin by importing everything necessary
import csv
import matplotlib.pyplot as plt
from numpy import *

# The user must set this to the directory and file that needs to be read in.
inputfile1 = 'Rotation_cont_002_1.con'
inputfile2 = 'Rotation_cont_002_2.con'
inputfile3 = 'Rotation_cont_002_3.con'
inputfile4 = 'Rotation_cont_002_4.con'
inputfile5 = 'Rotation_cont_002_5.con'
inputfile6 = 'Rotation_cont_002_6.con'
inputfile29 = 'Rotation_cont_002_7.con'
inputfile30 = 'Rotation_cont_002_8.con'

inputfile7 =  'Rotation_cont_008_1.con'
inputfile8 =  'Rotation_cont_008_2.con'
inputfile9 =  'Rotation_cont_008_3.con'
inputfile10 = 'Rotation_cont_008_4.con'
inputfile11 = 'Rotation_cont_008_5.con'
inputfile12 = 'Rotation_cont_008_6.con'
inputfile25 = 'Rotation_cont_008_7.con'
inputfile26 = 'Rotation_cont_008_8.con'
#inputfile29 = 'Rotation_cont_008_10.con'
#it does reach steady state after 8 Myr

inputfile13 = 'Rotation_inst_002_1.con'
inputfile14 = 'Rotation_inst_002_2.con'
inputfile15 = 'Rotation_inst_002_3.con'
inputfile16 = 'Rotation_inst_002_4.con'
inputfile17 = 'Rotation_inst_002_5.con'
inputfile18 = 'Rotation_inst_002_6.con'
inputfile31 = 'Rotation_inst_002_7.con'
inputfile32 = 'Rotation_inst_002_8.con'

inputfile19 = 'Rotation_inst_008_1.con'
inputfile20 = 'Rotation_inst_008_2.con'
inputfile21 = 'Rotation_inst_008_3.con'
inputfile22 = 'Rotation_inst_008_4.con'
inputfile23 = 'Rotation_inst_008_5.con'
inputfile24 = 'Rotation_inst_008_6.con'
inputfile27 = 'Rotation_inst_008_7.con'
inputfile28 = 'Rotation_inst_008_8.con'


inputfile33 = 'padova_inst_1.con'
inputfile34 = 'padova_inst_2.con'
inputfile35 = 'padova_inst_3.con'
inputfile36 = 'padova_inst_4.con'
inputfile37 = 'padova_inst_5.con'
inputfile38 = 'padova_inst_6.con'
inputfile39 = 'padova_inst_7.con'
inputfile40 = 'padova_inst_8.con'

inputfile41 = 'padova_cont_1.con'
inputfile42 = 'padova_cont_2.con'
inputfile43 = 'padova_cont_3.con'
inputfile44 = 'padova_cont_4.con'
inputfile45 = 'padova_cont_5.con'
inputfile46 = 'padova_cont_6.con'
inputfile47 = 'padova_cont_7.con'
inputfile48 = 'padova_cont_8.con'

#-------------------------------------------------------------

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
#---

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

#----

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
'''

datastarburst29 = [];
with open(inputfile29, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst29.append(row);
    datastarburst29 = asarray(datastarburst29)

'''

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

datastarburst37 = [];
with open(inputfile37, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst37.append(row);
    datastarburst37 = asarray(datastarburst37)

datastarburst38 = [];
with open(inputfile38, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst38.append(row);
    datastarburst38 = asarray(datastarburst38)

datastarburst39 = [];
with open(inputfile39, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst39.append(row);
    datastarburst39 = asarray(datastarburst39)


datastarburst40 = [];
with open(inputfile40, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst40.append(row);
    datastarburst40 = asarray(datastarburst40)

datastarburst41 = [];
with open(inputfile41, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst41.append(row);
    datastarburst41 = asarray(datastarburst41)

datastarburst42 = [];
with open(inputfile42, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst42.append(row);
    datastarburst42 = asarray(datastarburst42)

datastarburst43 = [];
with open(inputfile43, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst43.append(row);
    datastarburst43 = asarray(datastarburst43)


datastarburst44 = [];
with open(inputfile44, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst44.append(row);
    datastarburst44 = asarray(datastarburst44)

datastarburst45 = [];
with open(inputfile45, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst45.append(row);
    datastarburst45 = asarray(datastarburst45)

datastarburst46 = [];
with open(inputfile46, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst46.append(row);
    datastarburst46 = asarray(datastarburst46)

datastarburst47 = [];
with open(inputfile47, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst47.append(row);
    datastarburst47 = asarray(datastarburst47)


datastarburst48 = [];
with open(inputfile48, 'rb') as f:
    csvReader = csv.reader(f,delimiter='\t')
    headers = csvReader.next()
    for row in csvReader:
        datastarburst48.append(row);
    datastarburst48 = asarray(datastarburst48)
#-------------------------------------------------------------
    
# Extract x and y from the first two columns of the array.
x  = double(datastarburst1[:4022,0])
#if eV is desired, uncomment the following:
for i in range(len(x)):
    x[i] = 1.240/x[i]

y1  = double(datastarburst1[:4022,1])
y2  = double(datastarburst2[:4022,1])
y3  = double(datastarburst3[:4022,1])
y4  = double(datastarburst4[:4022,1])
y5  = double(datastarburst5[:4022,1])
y6  = double(datastarburst6[:4022,1])

y7  = double(datastarburst7[:4049,1])
y8  = double(datastarburst8[:4049,1])
y9  = double(datastarburst9[:4049,1])
y10  = double(datastarburst10[:4049,1])
y11  = double(datastarburst11[:4049,1])
y12  = double(datastarburst12[:4049,1])

y13  = double(datastarburst13[:4022,1])
y14  = double(datastarburst14[:4022,1])
y15  = double(datastarburst15[:4022,1])
y16  = double(datastarburst16[:4022,1])
y17  = double(datastarburst17[:4022,1])
y18  = double(datastarburst18[:4022,1])

y19  = double(datastarburst19[:3963,1])
y20  = double(datastarburst20[:3963,1])
y21  = double(datastarburst21[:3963,1])
y22  = double(datastarburst22[:3963,1])
y23  = double(datastarburst23[:3963,1])
y24  = double(datastarburst24[:3963,1])

y25  = double(datastarburst25[:4049,1])
y26  = double(datastarburst26[:4049,1])
y27  = double(datastarburst27[:3963,1])
y28  = double(datastarburst28[:3963,1])


y29  = double(datastarburst29[:4022,1])
y30  = double(datastarburst30[:4022,1])

y31  = double(datastarburst31[:4022,1])
y32  = double(datastarburst32[:4022,1])

y33  = double(datastarburst31[:4049,1])
y34  = double(datastarburst32[:4049,1])
y35  = double(datastarburst33[:4049,1])
y36  = double(datastarburst34[:4049,1])
y37  = double(datastarburst35[:4049,1])
y38  = double(datastarburst36[:4049,1])
y39  = double(datastarburst31[:4049,1])
y40  = double(datastarburst32[:4049,1])

y41  = double(datastarburst33[:4049,1])
y42  = double(datastarburst34[:4049,1])
y43  = double(datastarburst35[:4049,1])
y44  = double(datastarburst36[:4049,1])
y45  = double(datastarburst31[:4049,1])
y46  = double(datastarburst32[:4049,1])
y47  = double(datastarburst33[:4049,1])
y48  = double(datastarburst34[:4049,1])


#y29  = double(datastarburst29[:4049,1])
'''
y25  = double(datastarburst25[:3950,1])
y26  = double(datastarburst26[:3950,1])
y27  = double(datastarburst27[:3950,1])
y28  = double(datastarburst28[:3950,1])
y29  = double(datastarburst29[:3950,1])
y30  = double(datastarburst30[:3950,1])

y31  = double(datastarburst31[:4049,1])
y32  = double(datastarburst32[:4049,1])
y33  = double(datastarburst33[:4049,1])
y34  = double(datastarburst34[:4049,1])
y35  = double(datastarburst35[:4049,1])
y36  = double(datastarburst36[:4049,1])

#there are specific values here because for some reason some of the outputs were shorter (perhaps the end temp was reached faster in some) they only differed by about 100 so I've cut them off

#-------------------------------------------------------------
# Plot x vs. y in 4 subplots

fig = plt.figure(1)
#sp1 = plt.subplot(321) #rows columns location of this parcticular plot
p1 = plt.plot(x,y1, 'k', linewidth=1.5, label="1 Myr")
p2 = plt.plot(x,y2, 'c', linewidth=1.5, label="2 Myr")
p3 = plt.plot(x,y3, 'y', linewidth=1.5, label="3 Myr")
p4 = plt.plot(x,y4, 'r', linewidth=1.5, label="4 Myr")
p5 = plt.plot(x,y5, 'g', linewidth=1.5, label="5 Myr")
p6 = plt.plot(x,y6, 'b', linewidth=1.5, label="6 Myr")
p29 = plt.plot(x,y29, 'm', linewidth=1.5, label="7 Myr")
p30 = plt.plot(x,y30, '.75', linewidth=1.5, label="8 Myr")

plt.xlim(10**1, 10**2)
plt.ylim(10**1, 10**6)


plt.title('Starburst Geneva Track Continuous with Rotation- 0.002 Metallicity', fontsize=30)
#plt.ylabel(r'$4 \pi \nu J_\nu$ (erg $s^{-1} cm ^ {-2})$', fontsize=10)
#plt.tick_params(axis='x', bottom='off',labelbottom='off')
#plt.xscale('log', fontsize=10)
#plt.yscale('log', fontsize= 10)

#plt.legend(prop={'size':7})

#--------------------------------------------------------


fig = plt.figure(1)
#sp2 = plt.subplot(322)
p7 = plt.plot(x,y7, 'k', linewidth=1.5, label="1 Myr")
p8 = plt.plot(x,y8, 'c', linewidth=1.5, label="2 Myr")
p9 = plt.plot(x,y9, 'y', linewidth=1.5, label="3 Myr")
p10 = plt.plot(x,y10, 'r', linewidth=1.5, label="4 Myr")
p11 = plt.plot(x,y11, 'g', linewidth=1.5, label="5 Myr")
p12 = plt.plot(x,y12, 'b', linewidth=1.5, label="6 Myr")
p25 = plt.plot(x,y25, 'm', linewidth=1.5, label="7 Myr")
p26 = plt.plot(x,y26, '.75', linewidth=1.5, label="8 Myr")
#p29 = plt.plot(x,y29, '.5', linewidth=1.5, label="10 Myr")


plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)

#plt.tick_params(axis='x', bottom='off',labelbottom='off')


plt.title('Starburst Geneva Track Continuous with Rotation- 0.008 Metallicity', fontsize=30)
#plt.xscale('log')
#plt.yscale('log')

#plt.legend(prop={'size':7})


#--------------------------------------------------------
#sp3 = plt.subplot(323)
fig = plt.figure(1)
p13 = plt.plot(x,y13, 'k', linewidth=1.5, label="1 mil yrs")
p14 = plt.plot(x,y14, 'c', linewidth=1.5, label="2 mil yrs")
p15 = plt.plot(x,y15, 'y', linewidth=1.5, label="3 mil yrs")
p16 = plt.plot(x,y16, 'r', linewidth=1.5, label="4 mil yrs")
p17 = plt.plot(x,y17, 'g', linewidth=1.5, label="5 mil yrs")
p18 = plt.plot(x,y18, 'b', linewidth=1.5, label="6 mil yrs")

p30 = plt.plot(x,y30, 'm', linewidth=1.5, label="7 Myr")
p31 = plt.plot(x,y31, '0.75', linewidth=1.5, label="8 Myr")

plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)

plt.title('Starburst Geneva Track Instantaneous with Rotation- 0.002 Metallicity', fontsize=30)
#plt.xlabel(r'$\mu m$', fontsize=10)
#plt.ylabel(r'$4 \pi \nu J_\nu$ (erg $s^{-1} cm ^ {-2})$', fontsize=10)
#plt.xscale('log')
#plt.yscale('log')

#plt.legend(prop={'size':7})

#--------------------------------------------------------

#sp4 = plt.subplot(324)
fig = plt.figure(1)

p19 = plt.plot(x,y19, 'k', linewidth=1.5, label="1 Myr")
p20 = plt.plot(x,y20, 'c', linewidth=1.5, label="2 Myr")
p21 = plt.plot(x,y21, 'y', linewidth=1.5, label="3 Myr")
p22 = plt.plot(x,y22, 'r', linewidth=1.5, label="4 Myr")
p23 = plt.plot(x,y23, 'g', linewidth=1.5, label="5 Myr")
p24 = plt.plot(x,y24, 'b', linewidth=1.5, label="6 Myr")
p27 = plt.plot(x,y27, 'm', linewidth=1.5, label="7 Myr")
p28 = plt.plot(x,y28, '.75', linewidth=1.5, label="8 Myr")


plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)


plt.title('Starburst Geneva Track Instantaneous with Rotation- 0.008 Metallicity', fontsize=30)
#plt.xlabel(r'$\mu m$', fontsize=10)
#plt.tick_params(axis='x', bottom='off',labelbottom='off')

#plt.xscale('log')
#plt.yscale('log')

#plt.legend(prop={'size':7})

#-------------------------------------------------------------
# Plot x vs. y in 4 subplots
'''
fig = plt.figure(1)

#sp1 = plt.subplot(325) #rows columns location of this parcticular plot
p33 = plt.plot(x,y33, 'k', linewidth=.75, label="1 Myr")
p34 = plt.plot(x,y34, 'c', linewidth=.75, label="2 Myr")
p35 = plt.plot(x,y35, 'y', linewidth=.75, label="3 Myr")
p36 = plt.plot(x,y36, 'r', linewidth=.75, label="4 Myr")
p37 = plt.plot(x,y37, 'g', linewidth=.75, label="5 Myr")
p38 = plt.plot(x,y38, 'b', linewidth=.75, label="6 Myr")
p39 = plt.plot(x,y49, 'm', linewidth=.75, label="7 Myr")
p40 = plt.plot(x,y40, '0.75', linewidth=.75, label="8 Myr")


#plt.xlim(10**1, 10**2)
#plt.ylim(10**0, 10**6)


plt.title('Starburst Padova Track Instantaneous', fontsize=10)
#plt.ylabel(r'$4 \pi \nu J_\nu$ (erg $s^{-1} cm ^ {-2})$', fontsize=10)
#plt.xlabel('eV')

#plt.xscale('log')
#plt.yscale('log')

#plt.legend(prop={'size':7})
'''
#-------------------------------------------------------------
# Plot x vs. y in 4 subplots

fig = plt.figure(1)

#sp1 = plt.subplot(326) #rows columns location of this parcticular plot
p1 = plt.plot(x,y31, 'k', linewidth=2, label="1 Myr")
p2 = plt.plot(x,y32, 'c', linewidth=2, label="2 Myr")
p3 = plt.plot(x,y33, 'y', linewidth=2, label="3 Myr")
p4 = plt.plot(x,y34, 'r', linewidth=2, label="4 Myr")
p5 = plt.plot(x,y35, 'g', linewidth=2, label="5 Myr")
p6 = plt.plot(x,y36, 'b', linewidth=2, label="6 Myr")


'''
plt.xlim(10**1, 10**2)
plt.ylim(10**0, 10**6)
plt.yticks(fontsize=25)
plt.xticks(fontsize=25)


#ax = plt.gca()
#ax.tick_params(which='both', direction='out', length=10, width=1)

#plt.title('Padova Track Instantaneous SFH', fontsize=40)
plt.xlabel('Energy (eV)', fontsize = 25)
plt.ylabel(r'$4 \pi \nu J_\nu$ (erg $\mathrm{s}^{-1} \mathrm{cm} ^ {-2})$', fontsize=25)

plt.xscale('log')
plt.yscale('log')

plt.legend(prop={'size':30})

#-------------------------------------------------------------

#plt.savefig('continuum_padovacont.eps', figsize=(30,10))
#plt.clf()

plt.show()

