from numpy import *

#Enter the wanted metallicity
metallicity = .2

heliummass = 4.0026 # will use later

#Solar Abundances From Cloudy

# these are the new Solar abundances (stored as GASS10)

#number abundances
abundHe =	8.51e-2 # * 		4.0026
abundLi = 	1.12e-11# *			6.941 
abundBe = 	2.40e-11# * 		9.0122
abundB = 	5.01e-10# * 		10.811
abundC = 	2.69e-04# * 		12.0107	
abundN = 	6.76e-05# * 		14.0067
abundO = 	4.90e-04# *			15.9994
abundF = 	3.63e-08# * 		18.9984	
abundNe = 	8.51e-05# * 		20.1797
abundNa = 	1.74e-06# * 		22.9897
abundMg = 	3.98e-05# * 	 	24.305
abundAl = 	2.82e-06# * 		26.9815
abundSi = 	3.24e-05# *	 		28.0855
abundP = 	2.57e-07# * 		30.9738
abundS = 	1.32e-05# * 	 	32.065
abundCl = 	3.16e-07# * 		35.453
abundAr = 	2.51e-06# * 	 	39.948
abundK = 	1.07e-07# * 		39.0983
abundCa = 	2.19e-06# * 	 	40.078
abundSc = 	1.41e-09# * 		44.9559
abundTi = 	8.91e-08# * 	 	47.867
abundV = 	8.51e-09# * 		50.9415
abundCr = 	4.37e-07# * 		51.9961
abundMn = 	2.69e-07# * 	 	54.938
abundFe = 	3.16e-05# * 		55.845
abundCo = 	9.77e-08# * 		58.9332
abundNi = 	1.66e-06# * 		58.6934
abundCu = 	1.55e-08# * 		63.546	
abundZi = 	3.63e-08# * 		65.39
#-------------------------------------

#mass abundances
mabundHe =	8.51e-2  * 		4.0026
mabundLi = 	1.12e-11 *		6.941 
mabundBe = 	2.40e-11 * 		9.0122
mabundB = 	5.01e-10 * 		10.811
mabundC = 	2.69e-04 * 		12.0107	
mabundN = 	6.76e-05 * 		14.0067
mabundO = 	4.90e-04 *		15.9994
mabundF = 	3.63e-08 * 		18.9984	
mabundNe = 	8.51e-05 * 		20.1797
mabundNa = 	1.74e-06 * 		22.9897
mabundMg = 	3.98e-05 * 	 	24.305
mabundAl = 	2.82e-06 * 		26.9815
mabundSi = 	3.24e-05 *	 	28.0855
mabundP = 	2.57e-07 * 		30.9738
mabundS = 	1.32e-05 * 	 	32.065
mabundCl = 	3.16e-07 * 		35.453
mabundAr = 	2.51e-06 * 	 	39.948
mabundK = 	1.07e-07 * 		39.0983
mabundCa = 	2.19e-06 * 	 	40.078
mabundSc = 	1.41e-09 * 		44.9559
mabundTi = 	8.91e-08 * 	 	47.867
mabundV = 	8.51e-09 * 		50.9415
mabundCr = 	4.37e-07 * 		51.9961
mabundMn = 	2.69e-07 * 	 	54.938
mabundFe = 	3.16e-05 * 		55.845
mabundCo = 	9.77e-08 * 		58.9332
mabundNi = 	1.66e-06 * 		58.6934
mabundCu = 	1.55e-08 * 		63.546	
mabundZi = 	3.63e-08 * 		65.39

#-------------------------------------

totalz =  abundLi + abundBe + abundB + abundC + abundN + abundO + abundF + abundNe + abundNa + abundMg + abundAl+ abundSi + abundP + abundS + abundCl + abundAr + abundK + abundCa+ abundSc + abundTi + abundV + abundCr + abundMn + abundFe + abundCo + abundNi + abundCu + abundZi
mtotalz =  mabundLi + mabundBe + mabundB + mabundC + mabundN + mabundO + mabundF + mabundNe + mabundNa + mabundMg + mabundAl+ mabundSi + mabundP + mabundS + mabundCl + mabundAr + mabundK + mabundCa+ mabundSc + mabundTi + mabundV + mabundCr + mabundMn + mabundFe + mabundCo + mabundNi + mabundCu + mabundZi

#print "total by number of metals in new version is ", totalz
#print "total weight of metals in new version is ", mtotalz

#-------------------------------------

#old Solar abundances 84
#by number
oldabundHe = 	.100 	 #* 	4.0026
oldabundLi = 	2.04e-9  #*	6.941 
oldabundBe = 	2.63e-11 #* 	9.0122
oldabundB = 	7.59e-10 #* 	10.811
oldabundC = 	3.55e-4  #* 	12.0107	
oldabundN = 	9.33e-5  #*	14.0067
oldabundO = 	7.41e-4  #*	15.9994
oldabundF = 	3.02e-8  #* 	18.9984	
oldabundNe = 	1.17e-4  #* 	20.1797
oldabundNa = 	2.06e-6  #* 	22.9897
oldabundMg = 	3.80e-5  #* 	24.305
oldabundAl = 	2.95e-6  #* 	26.9815
oldabundSi = 	3.55e-5  #* 	28.0855
oldabundP = 	3.73e-7  #* 	30.9738
oldabundS = 	1.62e-5  #* 	32.065
oldabundCl = 	1.88e-7  #* 	35.453
oldabundAr = 	3.98e-6  #* 	39.948
oldabundK = 	1.35e-7  #* 	39.0983
oldabundCa = 	2.29e-6  #* 	40.078
oldabundSc = 	1.58e-9  #* 	44.9559
oldabundTi = 	1.10e-7  #* 	47.867
oldabundV = 	1.05e-8  #* 	50.9415
oldabundCr = 	4.84e-7  #* 	51.9961
oldabundMn = 	3.42e-7  #* 	54.938
oldabundFe = 	3.24e-5  #* 	55.845
oldabundCo = 	8.32e-8  #* 	58.9332
oldabundNi = 	1.76e-6  #* 	58.6934
oldabundCu = 	1.87e-8  #* 	63.546	
oldabundZi = 	4.52e-8  #* 	65.39

#-------------------------------------
#by mass
moldabundHe = 	.100 	 * 	4.0026
moldabundLi = 	2.04e-9  *	6.941 
moldabundBe = 	2.63e-11 * 	9.0122
moldabundB = 	7.59e-10 * 	10.811
moldabundC = 	3.55e-4  * 	12.0107	
moldabundN = 	9.33e-5  *	14.0067
moldabundO = 	7.41e-4  *	15.9994
moldabundF = 	3.02e-8  * 	18.9984	
moldabundNe = 	1.17e-4  * 	20.1797
moldabundNa = 	2.06e-6  * 	22.9897
moldabundMg = 	3.80e-5  * 	24.305
moldabundAl = 	2.95e-6  * 	26.9815
moldabundSi = 	3.55e-5  * 	28.0855
moldabundP = 	3.73e-7  * 	30.9738
moldabundS = 	1.62e-5  * 	32.065
moldabundCl = 	1.88e-7  * 	35.453
moldabundAr = 	3.98e-6  * 	39.948
moldabundK = 	1.35e-7  * 	39.0983
moldabundCa = 	2.29e-6  * 	40.078
moldabundSc = 	1.58e-9  * 	44.9559
moldabundTi = 	1.10e-7  * 	47.867
moldabundV = 	1.05e-8  * 	50.9415
moldabundCr = 	4.84e-7  * 	51.9961
moldabundMn = 	3.42e-7  * 	54.938
moldabundFe = 	3.24e-5  * 	55.845
moldabundCo = 	8.32e-8  * 	58.9332
moldabundNi = 	1.76e-6  * 	58.6934
moldabundCu = 	1.87e-8  * 	63.546	
moldabundZi = 	4.52e-8  * 	65.39


oldtotalz =  oldabundLi + oldabundBe + oldabundB + oldabundC + oldabundN + oldabundO + oldabundF + oldabundNe + oldabundNa + oldabundMg + oldabundAl+ oldabundSi + oldabundP + oldabundS + oldabundCl + oldabundAr + oldabundK + oldabundCa+ oldabundSc + oldabundTi + oldabundV + oldabundCr + oldabundMn + oldabundFe + oldabundCo + oldabundNi + oldabundCu + oldabundZi
moldtotalz =  moldabundLi + moldabundBe + moldabundB + moldabundC + moldabundN + moldabundO + moldabundF + moldabundNe + moldabundNa + moldabundMg + moldabundAl+ moldabundSi + moldabundP + moldabundS + moldabundCl + moldabundAr + moldabundK + moldabundCa+ moldabundSc + moldabundTi + moldabundV + moldabundCr + moldabundMn + moldabundFe + moldabundCo + moldabundNi + moldabundCu + moldabundZi

#print "old total z/H by number is ", oldtotalz
#print "old total z/H by mass is ", moldtotalz

#-------------------------------------

#Begin Calculations

#for new solar abundances
x_ini = 1.0 / (1.0 +  mabundHe + mtotalz)
y_ini = 1.0 - (x_ini) - (mtotalz)*(x_ini)
z_ini = 1.0 - (x_ini) - (mabundHe)*(x_ini)


#for old solar abundances
old_x_ini = 1.0 / (1.0 +  moldabundHe + moldtotalz)
old_y_ini = 1.0 - (old_x_ini) - (moldtotalz)*(old_x_ini)
old_z_ini = 1.0 - (old_x_ini) - (moldabundHe)*(old_x_ini)

#print "The new X_solar value is", x_ini
#print "The new Y_solar value is", y_ini
#print "The new Z_solar value is", z_ini

#print "The old X_solar value is", old_x_ini
#print "The old Y_solar value is", old_y_ini
#print "The old Z_solar value is", old_z_ini

new_z_f = (z_ini * metallicity)/(x_ini + y_ini + ((2.0*metallicity)-1.0)*z_ini)
new_y_f = ((z_ini * metallicity)/(x_ini + y_ini + ((2.0*metallicity)-1.0)*z_ini))-z_ini+y_ini
x_new = 1.0 - new_y_f - new_z_f

newalpha = new_y_f * (1/4.0/x_new) * (1.0/abundHe)

old_z_f = (old_z_ini * metallicity)/(old_x_ini + old_y_ini + ((2.0*metallicity)-1.0)*old_z_ini)
old_y_f = ((old_z_ini * metallicity)/(old_x_ini + old_y_ini + ((2.0*metallicity)-1.0)*old_z_ini))-old_z_ini+old_y_ini
old_x_new = 1.0 - old_y_f - old_z_f

oldalpha = old_y_f * (1/4.0/old_x_new) * (1.0/oldabundHe)


print "The new scale factor is", newalpha
print "The old scale factor was", oldalpha








