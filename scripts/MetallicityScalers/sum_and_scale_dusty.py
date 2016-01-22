from numpy import *

#Enter the wanted metallicity
metallicity = 5


heliummass = 4.0026 # will use later

# these are the  Dusty abundances from Cloudy (Baldwin 1991)

#abundances by number
abundHe =	0.095 	# * 		4.0026
abundLi = 	5.40e-11# *			6.941 
abundBe = 	1e-20	# * 		9.0122
abundB = 	8.9e-11	# * 		10.811
abundC = 	3.e-4	# * 		12.0107	
abundN = 	7.0e-5	# * 		14.0067
abundO = 	4.0e-04# *			15.9994
abundF = 	1e-20	# * 		18.9984	
abundNe = 	6e-5	# * 		20.1797
abundNa = 	3e-7 	# * 		22.9897
abundMg = 	3.e-6	# * 	 	24.305
abundAl = 	2.e-7	# * 		26.9815
abundSi = 	4.e-6	# *	 		28.0855
abundP = 	1.6e-7  # * 		30.9738
abundS = 	1.0e-5	# * 	 	32.065
abundCl = 	1.e-7	# * 		35.453
abundAr = 	3.0e-6	# * 	 	39.948
abundK = 	1.1e-08	# * 		39.0983
abundCa = 	2.0e-8  # * 	 	40.078
abundSc = 	1.e-20	# * 		44.9559
abundTi = 	5.8e-10	# * 	 	47.867
abundV = 	1.0e-10 # * 		50.9415
abundCr = 	1.0e-8  # * 		51.9961
abundMn = 	2.3e-8  # * 	 	54.938
abundFe = 	3.0e-6  # * 		55.845
abundCo = 	1e-20   # * 		58.9332
abundNi = 	1e-7    # * 		58.6934
abundCu = 	1.5e-9  # * 		63.546	
abundZi = 	2.0e-8  # * 		65.39
#-------------------------------------
#mass abundances
mabundHe =	0.095 	 * 		4.0026
mabundLi = 	5.40e-11 *			6.941 
mabundBe = 	1e-20	 * 		9.0122
mabundB = 	8.9e-11	 * 		10.811
mabundC = 	3.e-4	 * 		12.0107	
mabundN = 	7.0e-5	 * 		14.0067
mabundO = 	4.0e-04  *			15.9994
mabundF = 	1e-20	 * 		18.9984	
mabundNe = 	6e-5	 * 		20.1797
mabundNa = 	3e-7 	 * 		22.9897
mabundMg = 	3.e-6	 * 	 	24.305
mabundAl = 	2.e-7	 * 		26.9815
mabundSi = 	4.e-6	 *	 		28.0855
mabundP = 	1.6e-7   * 		30.9738
mabundS = 	1.0e-5	 * 	 	32.065
mabundCl = 	1.e-7	 * 		35.453
mabundAr = 	3.0e-6	 * 	 	39.948
mabundK = 	1.1e-08	 * 		39.0983
mabundCa = 	2.0e-8   * 	 	40.078
mabundSc = 	1.e-20	 * 		44.9559
mabundTi = 	5.8e-10	 * 	 	47.867
mabundV = 	1.0e-10  * 		50.9415
mabundCr = 	1.0e-8   * 		51.9961
mabundMn = 	2.3e-8   * 	 	54.938
mabundFe = 	3.0e-6   * 		55.845
mabundCo = 	1e-20    * 		58.9332
mabundNi = 	1e-7     * 		58.6934
mabundCu = 	1.5e-9   * 		63.546	
mabundZi = 	2.0e-8   * 		65.39

#-------------------------------------
#computing the total metals abundance by mass and by number 
totalz =  abundLi + abundBe + abundB + abundC + abundN + abundO + abundF + abundNe + abundNa + abundMg + abundAl+ abundSi + abundP + abundS + abundCl + abundAr + abundK + abundCa+ abundSc + abundTi + abundV + abundCr + abundMn + abundFe + abundCo + abundNi + abundCu + abundZi
mtotalz =  mabundLi + mabundBe + mabundB + mabundC + mabundN + mabundO + mabundF + mabundNe + mabundNa + mabundMg + mabundAl+ mabundSi + mabundP + mabundS + mabundCl + mabundAr + mabundK + mabundCa+ mabundSc + mabundTi + mabundV + mabundCr + mabundMn + mabundFe + mabundCo + mabundNi + mabundCu + mabundZi
#-------------------------------------

#for new solar abundances
x_ini = 1.0 / (1.0 +  mabundHe + mtotalz) #X_solar
y_ini = 1.0 - (x_ini) - (mtotalz)*(x_ini) #Y_solar
z_ini = 1.0 - (x_ini) - (mabundHe)*(x_ini) #Z_solar


new_z_f = (z_ini * metallicity)/(x_ini + y_ini + ((2.0*metallicity)-1.0)*z_ini)
new_y_f = ((z_ini * metallicity)/(x_ini + y_ini + ((2.0*metallicity)-1.0)*z_ini))-z_ini+y_ini
x_new = 1.0 - new_y_f - new_z_f

newalpha = new_y_f * (1/4.0/x_new) * (1.0/abundHe) #new scale factor
##print here so it doesn't mess the rest up 
print "The dusty He scale factor for metallicity", metallicity, "is", newalpha


#now calculate for the solar abundaces (for the non-dusty part)
#Solar Abundances From Cloudy

# these are the new Solar abundances (stored as GASS10)

#abundances by number
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
#computing the total metals abundance by mass and by number 
totalz =  abundLi + abundBe + abundB + abundC + abundN + abundO + abundF + abundNe + abundNa + abundMg + abundAl+ abundSi + abundP + abundS + abundCl + abundAr + abundK + abundCa+ abundSc + abundTi + abundV + abundCr + abundMn + abundFe + abundCo + abundNi + abundCu + abundZi
mtotalz =  mabundLi + mabundBe + mabundB + mabundC + mabundN + mabundO + mabundF + mabundNe + mabundNa + mabundMg + mabundAl+ mabundSi + mabundP + mabundS + mabundCl + mabundAr + mabundK + mabundCa+ mabundSc + mabundTi + mabundV + mabundCr + mabundMn + mabundFe + mabundCo + mabundNi + mabundCu + mabundZi
#-------------------------------------

#for new solar abundances
x_ini = 1.0 / (1.0 +  mabundHe + mtotalz) #X_solar
y_ini = 1.0 - (x_ini) - (mtotalz)*(x_ini) #Y_solar
z_ini = 1.0 - (x_ini) - (mabundHe)*(x_ini) #Z_solar


new_z_f = (z_ini * metallicity)/(x_ini + y_ini + ((2.0*metallicity)-1.0)*z_ini)
new_y_f = ((z_ini * metallicity)/(x_ini + y_ini + ((2.0*metallicity)-1.0)*z_ini))-z_ini+y_ini
x_new = 1.0 - new_y_f - new_z_f

newalpha = new_y_f * (1/4.0/x_new) * (1.0/abundHe) #new scale factor

print "The solar He scale factor for metallicity", metallicity, "is", newalpha

