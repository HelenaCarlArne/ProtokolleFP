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
	
def quad(x,a,b,c):
	return a*x**2+b*x+c

#Modenparameter
mod1=np.array([200,220,230,0,2*3.15,0])
mod2=np.array([120,140,150,0,2*3.15,0])
mod3=np.array([70,80,90,0,2*2.65,0])

#Quadratische Regression der Moden
params1,comat = curve_fit(quad,mod1[0:3],mod1[3:6])
params2,comat = curve_fit(quad,mod2[0:3],mod2[3:6])
params3,comat = curve_fit(quad,mod3[0:3],mod3[3:6])

x = np.linspace(50,250,10000)

print(params1)
print(params2)
print(params3)
print(max(quad(x,*params1)))
print(max(quad(x,*params2)))
print(max(quad(x,*params3)))

# Modenplot
plt.xlim(50,250)
plt.ylim(0,8)
plt.plot(mod1[0:3],mod1[3:6],'kx', label='Messdaten')
plt.plot(mod2[0:3],mod2[3:6],'kx')
plt.plot(mod3[0:3],mod3[3:6],'kx')
plt.plot(x, quad(x,*params1),'r-', label='Kurve 1')
plt.plot(x, quad(x,*params2),'g-', label='Kurve 2')
plt.plot(x, quad(x,*params3),'b-', label='Kurve 3')
plt.xlabel(r'Reflektorspannung $U \:/\: \si{\volt}$')
plt.ylabel(r'Ma\ss\,\,f\"ur Leistung, Amplitude $A$')
plt.legend(loc=0,numpoints=1)
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/plot.pdf')
plt.clf()

#Mittelwerte der Breitseite
breiteseite_mean=np.mean([22.45,22.7,22.7,22.7,22.55])
print(breiteseite_mean)

with open("pc/resultat.txt", 'a') as data:
	data.write("#Breitseite in mm\n"+"%s\n"%breiteseite_mean)

#Plot und Fit der Theorie-Dämpfung
dat=np.array([1.345,1.698,2.115,2.341,2.609])
mm=np.array([0,1,2,3,4,5])
dB=np.array([0,2,8,17,29,46])
plt.plot(mm,dB,"bx",label=r"Theorie-D\"ampfung")
params,coeff=curve_fit(quad,mm,dB)
plt.plot(dat,np.array([2,4,6,8,10]),"rx",label="Messwerte")
plt.plot(np.linspace(0,5),quad(np.linspace(0,5),*params),"b-",label=r"Fit der Theorie-D\"ampfung")
plt.legend(loc="best",numpoints=1)
plt.grid()
plt.xlabel(r'D\"ampfungseinstellung $\:/\: \si{\milli\meter}$')
plt.ylabel(r'D\"ampfung $\:/\: \si{\decibel}$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/daempfung.pdf')
plt.clf()

with open("pc/resultat.txt", 'a') as data:
	data.write("#Fit der Theorie-Dämpfung\n"+"%s\n"%params)

#Berechnung der Frequenz
lambda_g=48.2
a=22.62
freq=con.value("speed of light in vacuum")*np.sqrt(1/lambda_g**2 + 1/(4*a**2))
print(freq)
with open("pc/resultat.txt", 'a') as data:
	data.write("#Berechnete Frequenz\n"+"%s\n"%freq)

dat=np.array([1.345,1.698,2.115,2.341,2.609])
print(quad(dat,*params))
print(np.array([2,4,6,8,10])-quad(dat,*params)/quad(dat,*params)*100)
with open("pc/resultat.txt", 'a') as data:
	data.write("#Theoriewerte\n"+"%s\n"%quad(dat,*params))

