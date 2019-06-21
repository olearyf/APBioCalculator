'''
	Below is my final project from the first semester
	of my first computer science course. We spent about
	half of the semester learning Scratch, and spent the 
	latter half learnin Python. 
	At the time, I was in AP Bio, and had to do a
	Chi-Square test for a lab. I was inspired to create
	this program after doing that lab, since the math
	was so tedious.
	This version has not been edited since I wrote it,
	in the winter of 2016, hence its length, redundancy,
	incorrectness, and possible spelling errors.
'''

import math
import os
import turtle
#read through each function
#all temperature conversions work
#test each function
#unify wording
#make functions to solve the genetics problems you do in class
#add in functions so if an equation requires anopther function it takes the user there
#add in explainations 
def finalFinder():
	os.system('cls')
	print("Final Grade Calculator")
	print()
	print("Please note that all of these values should be entered in proper decimal form.")
	print("EX: If you have an 85%, you type .85.")
	currentGrade = float(input("What is your current grade %?"))
	examWorth = float(input("What % of your grade is the exam worth?"))
	idealGrade = float(input("What grade % would you like in the class?"))
	finalGrade = ((idealGrade-((1-examWorth)*currentGrade))/examWorth)*100
	print()
	print("You need a", finalGrade, "% to earn a", idealGrade, "in the class.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			finalFinder()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def meanCalculator():
	os.system('cls')
	print("Mean Calculator")
	print()
	numbers = []
	samplesize = int(input("How many numbers do you have?"))
	maxLengthList = samplesize
	while len(numbers)<maxLengthList:
		item = float(input("Enter your value: "))
		numbers.append(item)
	y = samplesize
	y = y-1
	mean = numbers[y]
	for i in range(y):
		y = y-1
		mean = mean+numbers[y]
	mean = mean/samplesize
	print()
	print("Your mean is", mean, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			meanCalculator()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def standardErrorCalc():
	os.system('cls')
	print("Standard Error Calculator")
	print()
	standardDev = float(input("What is your standard deviation?"))
	sampleSize = float(input("What is your sample size?"))
	standardError = standardDev/math.sqrt(sampleSize)
	print()
	print("Your standard error is", standardError, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			standardErrorCalc()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def standardDeviation():
	os.system('cls')
	print("Standard Deviation Calculator")
	print()
	mean  = float(input("What is the mean of your data?"))
	data = []
	samplesize = int(input("How many numbers do you have?"))
	y = samplesize
	maxLengthList = samplesize
	while len(data)<maxLengthList:
		item = float(input("Enter your value:"))
		data.append(item)
	samplesize = samplesize-1
	sd = (data[samplesize] - mean)**2
	for i in range(samplesize):
		samplesize = samplesize-1
		sd = (data[samplesize] - mean)**2 + sd
	sd = math.sqrt(sd/y)
	print()
	print("Your standard deviation is", sd, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			standardDeviation()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def chiSquare():
	os.system('cls')
	print("Chi-Square Calculator")
	print()
	print("Please note that this calculator only works")
	print("if the expected value is the same for each piece of data.")
	e = float(input("What is your expected value?(The mean of your data.)"))
	values = []
	samplesize = int(input("How many numbers do you have?"))
	maxLengthList = samplesize
	while len(values)<maxLengthList:
		item = float(input("Enter your value:"))
		values.append(item)
	samplesize = samplesize-1
	chi = ((values[samplesize]-e)**2)/e
	for i in range(samplesize):
		samplesize = samplesize-1
		chi = ((values[samplesize]-e)**2)/e + chi
	print()
	print("Your chi-square statistic is", chi, ".")
	print("Use a chi-square table to determine if your can accept or reject your null hypothesis.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			chiSquare()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def allFrequenciesWithQ():
	os.system('cls')
	print("All Frequencies Given Dominant Allele Frequency")
	print()
	q = float(input("What is your dominant allele frequency?"))
	p = 1-q
	pp = p**2
	qq = q**2
	pq = 2*p*q
	print()
	print("Your recessive allele frequency is", p, ".")
	print("Your homozygous recessive genotype frequency is", pp, ".")
	print("Your homozygous dominant genotype is", qq, ".")
	print("Your heterozygous genotype frequency is", pq, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to go back to the Hardy-Weinberg index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			allFrequenciesWithQ()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			hardyWeinberg()
		else:
			print("That was not an option! Please try again!")
def allFrequenciesWithR():
	os.system('cls')
	print("All Frequencies Given Recessive Allele Frequency")
	print()
	p = float(input("What is your recessive allele frequency?"))
	q = 1-p
	pp = p**2
	qq = q**2
	pq = 2*p*q
	print()
	print("Your dominant allele frequency is", q, ".")
	print("Your homozygous recessive genotype frequency is", pp, ".")
	print("Your homozygous dominant genotype is", qq, ".")
	print("Your heterozygous genotype frequency is", pq, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to go back to the Hardy-Weinberg index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			allFrequenciesWithRR()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			hardyWeinberg()
		else:
			print("That was not an option! Please try again!")
def allFrequenciesWithQQ():
	os.system('cls')
	print("All Frequencies Given Homozygous Dominant Frequency")
	print()
	qq = float(input("What is your homozygous dominant genotype frequency?"))
	q = math.sqrt(qq)
	p = 1-q
	pp = p**2
	pq = 2*p*q
	print()
	print("Your recessive allele frequency is", p, ".")
	print("Your dominant allele frequency is", q, ".")
	print("Your homozygous recessive genotype frequency is", pp, ".")
	print("Your heterozygous genotype frequency is", pq, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to go back to the Hardy-Weinberg index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			allFrequenciesWithQQ()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			hardyWeinberg()
		else:
			print("That was not an option! Please try again!")
def allFrequenciesWithRR():
	os.system('cls')
	print("All Frequencies Given Homozygous Recessive Frequency")
	print()
	pp = float(input("What is your homozygous dominant genotype frequency?"))
	p = math.sqrt(pp)
	q = 1-p
	qq = q**2
	pq = 2*p*q
	print()
	print("Your recessive allele frequency is", p, ".")
	print("Your dominant allele frequency is", q, ".")
	print("Your homozygous dominant genotype is", qq, ".")
	print("Your heterozygous genotype frequency is", pq, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to return to the Hardy-Weinberg index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			allFrequenciesWithRR()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			hardyWeinberg()
		else:
			print("That was not an option! Please try again!")
def hardyWeinberg():
	os.system('cls')
	print("Hardy-Weinberg Functions")
	print()
	#here combine all your hardy weinberg functions in a visual index that can then be navigated through
	#write functions to solve the problems you are doing in that packet
	print("Below are the functions related to Hardy Weinberg equations.")
	print("Enter the corresponding function number to run it.")
	print("If you would like to go to the main menu, type'back'.")
	functNames = ["All Frequencies Given Dominant Allele Frequency", "All Frequencies Given Recessive Allele Frequency", "All Frequencies Given Homozygous Dominant Frequency", "All Frequencies Given Homozygous Recessive Frequency"]
	x = 1
	y = 0
	print()
	for i in range(4):
		print(x, "\t", functNames[y])
		x = x+1
		y = y+1
	print()
	while 3==3:
		answer = input("What function would you like to use?")
		if answer=="1":
			allFrequenciesWithQ()
		elif answer=="2":
			allFrequenciesWithR()
		elif answer=="3":
			allFrequenciesWithQQ()
		elif answer=="4":
			allFrequenciesWithRR()
		elif answer=="back":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def solutePotential():
	os.system('cls')
	print("Solute Potential Calculator")
	print()
	pressPotential = float(input("What is your pressure potential?"))
	waterPoten = float(input("What is your water potential?"))
	sp = waterPoten-pressPotential
	print()
	print("Your solute potential is", sp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			solutePotential()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def waterPotential():
	os.system('cls')
	print("Water Otential Calculator")
	print()
	pressPotential = float(input("What is your pressure potential?"))
	solutePoten = float(input("What is your solute potential?"))
	wp = solutePoten+pressPotential
	print()
	print("Your water potential is", wp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			waterPotential()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def pressurePotential():
	os.system('cls')
	print("Pressure Potential Calculator")
	print()
	solPotential = float(input("What is your solute potential?"))
	waterPoten = float(input("What is your water potential?"))
	pp = waterPoten-solPotential
	print()
	print("Your solute potential is", pp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			pressurePotential()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def solutePotentialofSolution():
	os.system('cls')
	ionConstant = float(input("What is your ionization constant?"))
	molarCon = float(input("What is your molar concentration?"))
	temp = float(input("What is the temperature in Kelvin?"))
	sps = -1*ionConstant*molarCon*temp*0.0831
	print("The solute potential of your solution is", sps, ".")
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			solutePotentialofSolution()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def initialSoluteConcentration():
	os.system('cls')
	print("Initial Solute Concentration Calculator")
	print()
	iv = float(input("What was the initial volume of your solution?"))
	fc = float(input("What is the final concentration of your solution?"))
	fv = float(input("What is the final volume of your solution?"))
	isc = (fc*fv)/iv
	print()
	print("Your initial solute concentration was", isc, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	print("If you would like to return to the dilution index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			initialSoluteConcentration()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			dilutionCalc()
		else:
			print("That was not an option! Please try again!")
def initialSoluteVolume():
	os.system('cls')
	print("Initial Solute Volume Calculator")
	print()
	ic = float(input("What was the initial concentration of your solute?"))
	fc = float(input("What is the final concentration of your solution?"))
	fv = float(input("What is the final volume of your solution?"))
	isv = (fc*fv)/ic
	print()
	print("Your initial solute volume was", isv, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	print("If you would like to return to the dilution index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			initialSoluteVolume()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			dilutionCalc()
		else:
			print("That was not an option! Please try again!")
def finalSoluteConcentration():
	os.system('cls')
	print("Final Solute Concentration Calculator")
	print()
	ic = float(input("What was the initial concentration of your solute?"))
	iv = float(input("What was the initial volume of your solution?"))
	fv = float(input("What is the final volume of your solution?"))
	fsc = (ic*iv)/fv
	print()
	print("Your final solute concentration is", fsc, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	print("If you would like to return to the dilution index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			finalSoluteConcentration()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			dilutionCalc()
		else:
			print("That was not an option! Please try again!")
def finalSoluteVolume():
	os.system('cls')
	print("Final Solute Volume Calculator")
	print()
	ic = float(input("What was the initial concentration of your solute?"))
	iv = float(input("What was the initial volume of your solution?"))
	fc = float(input("What is the final concentration of your solution?"))
	fsv = (ic*iv)/fc
	print()
	print("Your final solute volume is", fsv, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	print("If you would like to return to the dilution index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			finalSoluteVolume()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			dilutionCalc()
		else:
			print("That was not an option! Please try again!")
def dilutionCalc():
	os.system('cls')
	print("Dilution Functions")
	print()
	print("Below are the functions related to dilution.")
	print("Enter the corresponding function number to run it.")
	print("If you would like to go to the main menu, type'back'.")
	print()
	functNames = ["Initial Solute Concentration Calculator", "Initial Solute Volume Calculator", "Final Solute Concentration Calculator", "Final Solute Volume Calculator"]
	x = 1
	y = 0
	for i in range(4):
		print(x, "\t", functNames[y])
		x = x+1
		y = y+1
	print()
	while 3==3:
		answer = input("What function would you like to use?")
		if answer=="1":
			initialSoluteConcentration()
		elif answer=="2":
			initialSoluteVolume()
		elif answer=="3":
			finalSoluteConcentration()
		elif answer=="4":
			finalSoluteVolume()
		elif answer=="back":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def celsius2fahrenheit():
	os.system('cls')
	print("Celsius to Fahrenheit")
	print()
	temp = float(input("What is your temperature in degrees Celsius?"))
	convertTemp = temp*(9/5) + 32
	print()
	print("Your temperature in degrees Fahrenheit is", convertTemp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to return to the temperature conversion index, type '3'.")#next time consolidate the intro and outro code in another function to shorten it
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			celsius2fahrenheit()
		elif answer=="2":
			APBioCalculator()
		elif answer=='3':
			temperatureConversions()
		else:
			print("That was not an option! Please try again!")
def fahrenheit2celsius():
	os.system('cls')
	print("Fahrenheit to Celsius")
	print()
	temp = float(input("What is your temperature in degrees Fahrenheit?"))
	convertTemp = (temp-32)*5/9
	print()
	print("Your temperature in degrees Celsius is", convertTemp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to return to the temperature conversion index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			fahrenheit2celsius()
		elif answer=="2":
			APBioCalculator()
		elif answer=='3':
			temperatureConversions()
		else:
			print("That was not an option! Please try again!")
def celsius2kelvin():
	os.system('cls')
	print("Celsius to Kelvin")
	print()
	temp = float(input("What is your temperature in degrees Celsius?"))
	convertTemp = temp + 273.15
	print()
	print("Your temperature in degrees Kelvin is", convertTemp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to return to the temperature conversion index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			celsius2kelvin()
		elif answer=="2":
			APBioCalculator()
		elif answer=='3':
			temperatureConversions()
		else:
			print("That was not an option! Please try again!")
def fahrenheit2kelvin():
	os.system('cls')
	print("Fahrenheit to Kelvin")
	print()
	temp = float(input("What is your temperature in degrees Fahrenheit?"))
	convertTemp = ((temp-32)*5/9)+273.15
	print()
	print("Your temperature in degrees Kelvin is", convertTemp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to return to the temperature conversion index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			fahrenheit2kelvin()
		elif answer=="2":
			APBioCalculator()
		elif answer=='3':
			temperatureConversions()
		else:
			print("That was not an option! Please try again!")
def kelvin2celsius():
	os.system('cls')
	print("Kelvin to Celsius")
	print()
	temp = float(input("What is your temperature in degrees Kelvin?"))
	convertTemp = temp - 273.15
	print()
	print("Your temperature in degrees Celsius is", convertTemp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to return to the temperature conversion index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			kelvin2celsius()
		elif answer=="2":
			APBioCalculator()
		elif answer=='3':
			temperatureConversions()
		else:
			print("That was not an option! Please try again!")
def kelvin2fahrenheit():
	os.system('cls')
	print("Kelvin to Fahrenheit")
	print()
	temp = float(input("What is your temperature in degrees Kelvin?"))
	convertTemp = (temp - 273.15)*(9/5) + 32
	print()
	print("Your temperature in degrees Celsius is", convertTemp, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If you would like to return to the temperature conversion index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			kelvin2fahrenheit()
		elif answer=="2":
			APBioCalculator()
		elif answer=='3':
			temperatureConversions()
		else:
			print("That was not an option! Please try again!")
def temperatureConversions():
	os.system('cls')
	print("Temerature Conversions")
	print()
	print("Below are the functions related to temperature conversions.")
	print("Enter the corresponding function number to run it.")
	print("If you would like to go to the main menu, type 'back'.")
	print()
	functNames = ["Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius", "Fahrenheit to Kelvin", "Kelvin to Celsius", "Kelvin to Fahrenheit"]
	x = 1
	y = 0
	for i in range(6):
		print(x, "\t", functNames[y])
		x = x+1
		y = y+1
	print()
	while 3==3:
		answer = input("What function would you like to use?")
		if answer=="1":
			celsius2fahrenheit()
		elif answer=="2":
			celsius2kelvin()
		elif answer=="3":
			fahrenheit2celsius()
		elif answer=="4":
			fahrenheit2kelvin()
		elif answer=="5":
			kelvin2celsius()
		elif answer=="6":
			kelvin2fahrenheit()
		elif answer=="back":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def gibbsFreeEnergy():
	os.system('cls')
	print("Gibbs Free Energy Calculator")
	print()
	deltaH = float(input("What is your change in enthalpy in kJ?"))
	deltaS = float(input("What is your entropy change in kJ/K?"))
	sysTemp = float(input("What is the temperature of your system in K?"))
	freeEnergyChange = deltaH-(sysTemp*deltaS)
	print()
	print("Your Free Energy Change is", freeEnergyChange, "kJ.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If your would like to return to the Gibbs free energy index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			gibbsFreeEnergy()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			gfecalculator()
		else:
			print("That was not an option! Please try again!")
def changeinEntropy():
	os.system('cls')
	print("Change in Entropy Calculator")
	print()
	deltaH = float(input("What is your change in enthalpy in kJ?"))
	freeEnergyChange = float(input("What is your free energy change in kJ?"))
	sysTemp = float(input("What is the temperature of your system in K?"))
	deltaS = (freeEnergyChange-deltaH)/(-1*sysTemp)
	print()
	print("Your Change in Entropy is", deltaS, "kJ/K.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") 
	print("If your would like to return to the Gibbs free energy index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			changeinEntropy()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			gfecalculator()
		else:
			print("That was not an option! Please try again!")
def changeinEnthalpy():
	os.system('cls')
	print("Change in Enthalpy Calculator")
	print()
	freeEnergyChange = float(input("What is your free energy change in kJ?"))
	deltaS = float(input("What is your entropy change in kJ/K?"))
	sysTemp = float(input("What is the temperature of your system in K?"))
	deltaH = freeEnergyChange+sysTemp*deltaS
	print()
	print("Your change in enthalpy is", deltaH, "kJ.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	print("If your would like to return to the Gibbs free energy index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			changeinEnthalpy()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			gfecalculator()
		else:
			print("That was not an option! Please try again!")
def temperatureGFE():
	os.system('cls')
	print("System Temperature Calculator")
	print()
	deltaH = float(input("What is your change in enthalpy in kJ?"))
	deltaS = float(input("What is your entropy change in kJ/K?"))
	freeEnergyChange = float(input("What is your free energy change in kJ?"))
	sysTemp = ((freeEnergyChange-deltaH)/deltaS)/-1
	print()
	print("Your system temperature is", sysTemp5, "K.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	print("If your would like to return to the Gibbs free energy index, type '3'.")
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			temperatureGFE()
		elif answer=="2":
			APBioCalculator()
		elif answer=="3":
			gfecalculator()
		else:
			print("That was not an option! Please try again!")
def gfecalculator():
	os.system('cls')
	print("Gibbs Free Energy Functions")
	print()
	print("Below are the functions related to Gibbs Free Energy.")
	print("Enter the corresponding function number to run it.")
	print("If you would like to go to the main menu, type'back'.")
	print()
	functNames = ["Gibbs Free Energy Calculator", "Change in Entropy Calculator", "Change in Enthalpy Calculator", "System Temperature Calculator"]
	x = 1
	y = 0
	for i in range(4):
		print(x, "\t", functNames[y])
		x = x+1
		y = y+1
	print()
	while 3==3:
		answer = input("What function would you like to use?")
		if answer=="1":
			gibbsFreeEnergy()
		elif answer=="2":
			changeinEntropy()
		elif answer=="3":
			changeinEnthalpy()
		elif answer=="4":
			temperatureGFE()
		elif answer=="back":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def pHcalc():
	os.system('cls')
	print("pH Calculator")
	print()
	hconcentration = float(input("What is your hydrogen ion concentration? No scientific notation."))
	pH = -1*(math.log(hconcentration, 10))
	print()
	print("Your pH is", pH, ".")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			pHcalc()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def sphereVolume():
	os.system('cls')
	print("Sphere Volume Calculator")
	print()
	radius = float(input("What is the radius of your sphere?"))
	volume = (4/3)*math.pi*radius**3
	print()
	print("The volume of your sphere is", volume, "units cubed.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			sphereVolume()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def rectangularPrismVolume():
	os.system('cls')
	print("Rectangular Prism Volume Calculator")
	print()
	length = float(input("What is the length of your rectangular prism?"))
	height = float(input("What is the height of your rectangular prism?"))
	width = float(input("What is the width of your rectangular prism?"))
	volume = length*width*height
	print()
	print("The volume of your rectangular prism is", volume, "units cubed.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			rectangularPrismVolume()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def columnVolume():
	os.system('cls')
	print("Cylinder Volume Calculator")
	print()
	height = float(input("What is the height of your column?"))
	radius = float(input("What is the radius of your column?"))
	colVol = math.pi*(radius**2)*height
	print()
	print("The volume of your column is", colVol, "units cubed.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			columnVolume()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def sphereSurfaceArea():
	os.system('cls')
	print("Sphere Surface Area Calculator")
	print()
	radius = float(input("What is the radius of your sphere?"))
	sphereSA = 4*math.pi*radius**2
	print()
	print("The surface area of your sphere is", sphereSA, "units squared.")
	print()
	print("If you would like to use this function again, type '1'.")
	print("If you would like to return to the main menu, type '2'.") #for functions within another index add another option to go back there
	while 1==1:
		answer = input("What would you like to do?")
		if answer=="1":
			sphereSurfaceArea()
		elif answer=="2":
			APBioCalculator()
		else:
			print("That was not an option! Please try again!")
def APBioCalculator():
	while 1==1:
		#add in spaces to differentiate between places or clear the screen
		os.system('cls') #put this method withinin every function and create a way so you can navigate back to the main menu after a function is used
		print("Below are the AP Biology Fomulas and Equations that") 
		print("are listed online by the College Board.")
		print("Enter the corresponding number to run your desired function.")
		#make sure all functions are in alphabetical order
		allFunctList = ["Chi-Square Calculator", "Cylinder Volume Calculator",  "Dilution Functions", "Final Grade Calculator", "Gibbs Free Energy Functions", "Hardy-Weinberg Functions",  "Mean Calculator", "pH Calculator", "Pressure Potential Calculator", "Rectangular Prism Volume Calculator", "Solute Potential Calculator", "Solute Potential of Solution Calculator", "Sphere Surface Area Calculator", "Sphere Volume Calculator", "Standard Deviation Calculator", "Standard Error Calculator", "Temperature Conversions", "Water Potential Calculator"]
		print("If at anytime you are stuck in a function you did")
		print("not want, please work through it and follow")
		print("the directions back to your desired destination afterwards.")
		print("Also note that when you navigate to a new function")
		print("or page, the screen will be cleared.")
		print("Finally, please remember to keep your units consistent.")
		print()
		x = 1
		y = 0
		for i in range(18):
			print(x, "\t", allFunctList[y])
			x = x+1
			y = y+1
		print()
		while 3==3:
			answer = input("What function would you like to use?")
			if answer=="1":
				chiSquare()
			elif answer=="2":
				columnVolume()
			elif answer=="3":
				dilutionCalc()
			elif answer=="4":
				finalFinder()
			elif answer=="5":
				gfecalculator()
			elif answer=="6":
				hardyWeinberg()
			elif answer=="7":
				meanCalculator()
			elif answer=="8":
				pHcalc()
			elif answer=="9":
				pressurePotential()
			elif answer=="10":
				rectangularPrismVolume()
			elif answer=="11":
				solutePotential()
			elif answer=="12":
				solutePotentialofSolution()
			elif answer=="13":
				sphereSurfaceArea()
			elif answer=="14":
				sphereVolume()
			elif answer=="15":
				standardDeviation()
			elif answer=="16":
				standardErrorCalc()
			elif answer=="17":
				temperatureConversions()
			elif answer=="18":
				waterPotential()
			elif answer=="Mr. Tucker":
				print("#FreeBubbaTheFrog")
				print("You have found my easter egg.")
				print("You are now trapped here.")
				print("Please restart the program to actually use it.")
				#put a picture of a frog here that will pop up
				#image not recognized as something to be imported so draw one
				wn = turtle.Screen()
				t = turtle.Turtle
				wn.bgcolor("black")
				turtle.color("white")
				turtle.speed(0)
				turtle.ht()
				colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
				while 1==1:
					x = int(input("What is your size?"))
					i = int(input("How many times"))
					o = input("White or rainbow?")
					if o=="white":
						for n in range(i):
							turtle.pencolor("white")
							turtle.circle(x)
							turtle.left(360/i)
					if o=="rainbow":
						for n in range(i):
							turtle.pencolor(colors[n%6])
							turtle.circle(x)
							turtle.left(360/i)
					wn.exitonclick()
			else:
				print("That was not an option! Please try again!")
APBioCalculator()
