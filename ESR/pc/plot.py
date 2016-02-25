# coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
import sympy
from uncertainties import correlated_values, correlation_matrix
import scipy.integrate as int
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as sdevs
import scipy.constants as con
from scipy.constants import physical_constants as pcon
#Table Funktion
dummy = ufloat(69,42)
dummyarray = np.array([dummy,dummy*6.626])
udummyarray = unp.uarray([4], [5*con.pi])

#data1 = [a,b,c,d,e]
#p1 = {'name':'tabelle1.tex','data':data1}
#table(**p1)
def table(name, data):
	j=0
	i=0
	f = [0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(len(data)):
		if(type(data[i][0]) == type(dummy) or type(data[i][0]) == type(dummyarray[1]) or type(data) == type(udummyarray)):
			f[i] = True
		else:
			f[i] = False
	print(f)
	output = open(name, 'w')
	output.write(r'\begin{table}[h]' + '\n' + r'\centering' + '\n' + r'\caption{CAPTION}' + '\n' +r'\sisetup{%uncertainty-seperator = {\,},'+'\n'+r'table-number-alignment = center,'+'\n'+'table-unit-alignment = center,'+'\n'+'%table-figures-integer = 1,'+'\n'+'%table-figures-decimal = 1,'+'\n'+'table-auto-round = true'+'\n'+'}'+'\n'+ r'\begin{tabular}{ ')
	for i in range(len(data)):
		if(f[i]):
			output.write(r'S[table-format= 3.1]'+'\n'+' @{\,$\pm{}$\,} '+'\n' + r' S[table-format= 3.1] ')
		else:
			output.write(r' S[table-format= 3.1] '+'\n')
	output.write(r'}' + '\n' + r'\toprule' + '\n')

	for i in range(len(data)):
		if(i < (len(data)-1)):
			if(f[i]):
				output.write(r'\multicolumn{2}{c}{TITLE}'+'\n'+'&')
			else:
				output.write(r'{$\text{Title}$}'+'\n'+'&')
		else:
			if(f[i]):
				output.write(r'\multicolumn{2}{c}{TITLE} \\'+'\n')
			else:
				output.write(r'{$\text{Title}$} \\'+'\n')
	output.write(r' \midrule' + '\n')

	#Tabelle
	for j in range(len(data[0])):
		i = 0
		while i <= len(data)-1:
				if(f[i]):
					if(i == len(data)-1):
						output.write(str(data[i][j].n) + '&' + str(data[i][j].s) + r'\\' + '\n')
					else:
						output.write(str(data[i][j].n)+ '&' + str(data[i][j].s) + '&')
					i = i+1
				else:
					if(i == len(data)-1):
						output.write(str(data[i][j]) + r'\\' + '\n')
					else:
						output.write(str(data[i][j]) + '&')
					i = i+1
	#Tabelle Ende
	output.write(r'\bottomrule' + '\n' + r'\end{tabular}' + '\n' + r'\label{tab:LABEL}' + '\n' + r'\end{table}')
	output.close()


#x = [1,2,3]
#y = [4,5,6]
#plt.plot(x,y,"rx",label="Test") 
#plt.legend(loc='best')#

#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('pc/plot.pdf')


#Konstanten
n = 156
r = 0.1
mu0 = 4*np.pi*10**(-7)
h = 6.626*10**(-34)
muB = 9.274 * 10**(-24)
#Berechnung der Feldstärke
def B(x):
	return 8/(np.sqrt(125))*mu0*n/r*x
#f = 10.572
mm1, Im1 = np.genfromtxt('data/f1.txt', unpack = True)	#Werte der Skala
mf1 = ufloat(np.mean(Im1/mm1), np.std(Im1/mm1)/np.sqrt(len(Im1))) #Massstabsfaktor in mA / mm
nm1 = 120 - 9*mf1	#Nullpunkt des Massstabes
I1p = nm1 + 63*mf1	#Wert des Minimums in mA
B1p = B(I1p)		#Feldstärke in mT
I1a = nm1 + 112*mf1	#Wert des Minimums in mA
B1a = B(I1a)		#Feldstärke in mT
I1p = I1p/1000
B1p= B1p/1000
I1a = I1a/1000
B1a= B1a/1000
print(mf1)


#f = 15.901
mm2, Im2 = np.genfromtxt('data/f2.txt', unpack = True)	#Werte der Skala
mf2 = ufloat(np.mean(Im2/mm2), np.std(Im2/mm2)/np.sqrt(len(Im2))) #Massstabsfaktor in mA / mm
nm2 = 237 - 9*mf2	#Nullpunkt des Massstabes
I2p = nm2 + 70*mf2	#Wert des Minimums in mA
B2p = B(I2p)		#Feldstärke in mT
I2a = nm2 + 105*mf2	#Wert des Minimums in mA
B2a = B(I2a)		#Feldstärke in mT
I2p = I2p/1000
B2p= B2p/1000
I2a = I2a/1000
B2a= B2a/1000
print(mf2)

#f = 20.577
mm3, Im3 = np.genfromtxt('data/f3.txt', unpack = True)	#Werte der Skala
mf3 = ufloat(np.mean(Im3/mm3), np.std(Im3/mm3)/np.sqrt(len(Im3))) #Massstabsfaktor in mA / mm
nm3 = 280 - 8*mf3	#Nullpunkt des Massstabes
I3p = nm3 + 115*mf3	#Wert des Minimums in mA
B3p = B(I3p)		#Feldstärke in mT
I3a = nm3 + 152*mf3	#Wert des Minimums in mA
B3a = B(I3a)		#Feldstärke in mT
I3p = I3p/1000
B3p= B3p/1000
I3a = I3a/1000
B3a= B3a/1000
print(mf3)


#f = 25.000
mm4, Im4 = np.genfromtxt('data/f4.txt', unpack = True)	#Werte der Skala
mf4 = ufloat(np.mean(Im4/mm4), np.std(Im4/mm4)/np.sqrt(len(Im4))) #Massstabsfaktor in mA / mm
nm4 = 524 - 10*mf4	#Nullpunkt des Massstabes
I4p = nm4 + 50*mf4	#Wert des Minimums in mA
B4p = B(I4p)		#Feldstärke in mT
I4a = nm4 + 87*mf4	#Wert des Minimums in mA
B4a = B(I4a)		#Feldstärke in mT
I4p = I4p/1000
B4p= B4p/1000
I4a = I4a/1000
B4a= B4a/1000
print(mf4)


#f = 29.448
mm5, Im5 = np.genfromtxt('data/f5.txt', unpack = True)	#Werte der Skala
mf5 = ufloat(np.mean(Im5/mm5), np.std(Im5/mm5)/np.sqrt(len(Im5))) #Massstabsfaktor in mA / mm
nm5 = 547 - 6*mf5	#Nullpunkt des Massstabes
I5p = nm5 + 94*mf5	#Wert des Minimums in mA
B5p = B(I5p)		#Feldstärke in mT
I5a = nm5 + 130*mf5	#Wert des Minimums in mA
B5a = B(I5a)		#Feldstärke in mT
I5p = I5p/1000
B5p= B5p/1000
I5a = I5a/1000
B5a= B5a/1000
print(mf5)


Bae = np.array([B1a, B2a, B3a, B4a, B5a])
Bpe = np.array([B1p, B2p, B3p, B4p, B5p])
Ba = np.array([ufloat(0,0), B1a, B2a, B3a, B4a, B5a])
Bp = np.array([ufloat(0,0), B1p, B2p, B3p, B4p, B5p])
Bts = (Ba + Bp)/2
Be = (Bae - Bpe)/2
Bem = Be.mean()
print(Bts)
print(Be)
print(Bem)
Bt = np.array([Bts])

#Frequenzen
fm = np.array([0, 10.572, 15.901, 20.557, 25.00, 29.448])*10**6
fe = np.array([0, 10.00, 15.35, 20.00, 24.44, 30.00])*10**6 

def Bf(x, m, b):
	return m*x + b
params, cov = curve_fit(Bf, abs(fm), noms(Bts))
print(params)
params = correlated_values(params, cov)
m = params[0]
g = h/(muB*m)
print(g)


plt.errorbar(fm, noms(Bts), yerr=sdevs(Bts), fmt='rx', label="Messwerte")
plt.legend(loc='best')

plt.xlabel(r'$\nu \:/\: \si{\hertz}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/plot.pdf')

