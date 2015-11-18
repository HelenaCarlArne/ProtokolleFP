import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties import ufloat
import sympy
from uncertainties import correlated_values, correlation_matrix
#Table Funktion
dummy = ufloat(69,42)
dummyarray = np.array([dummy,dummy*6.626])

#data1 = [a,b,c,d,e]
#p1 = {'name':'tabelle1.tex','data':data1}
#table(**p1)
def table(name, data):
	j=0
	i=0
	f = [0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(len(data)):
		if(type(data[i][0]) == type(dummy) or type(data[i][0]) == type(dummyarray[1])):
			f[i] = True
		else:
			f[i] = False
	print(f)
	output = open(name, 'w')
	output.write(r'\begin{table}[h]' + '\n' + r'\centering' + '\n' + r'\caption{CAPTION}' + '\n' +r'\sisetup{round-mode=places,'+'\n'+r'round-precision=3}'+'\n'+ r'\begin{tabular}{ ')
	for i in range(len(data)):
		if(f[i]):
			output.write(r'S @{${}\pm{}$} ' + r' S ')
		else:
			output.write(r' S[table-format= .3] ')
	output.write(r'}' + '\n' + r'\toprule' + '\n')
	
	for i in range(len(data)):
		if(i < (len(data)-1)): 
			if(f[i]):
				output.write(r'\multicolumn{2}{c}{TITLE} &')
			else:
				output.write(r'{$\text{Title}$} & ')
		else:
			if(f[i]):
				output.write(r'\multicolumn{2}{c}{TITLE} \\')
			else:
				output.write(r'{$\text{Title}$} \\')
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
	


#Alpha Faktor
Tak, ak = np.genfromtxt('rawdata/a.txt', unpack = True)

#def f(x, a, b, c, m):
#	return m*np.log(a*(x-b))+c
def f(x, a, b, m):
	return m*np.log(a*x+ b)
params, covs = curve_fit(f, Tak, ak)
	
plt.plot(Tak, ak,'bx', label='Messwerte')
t = np.linspace(50, 300, 500)
plt.plot(t, f(t, *params), 'r-', label='fit log')
plt.grid()
plt.xlabel(r'$T/K$')
plt.ylabel(r'$\alpha$')
plt.legend(loc='best')
#plt.show()
plt.savefig('pc/a.pdf')
plt.clf()	
 
#Messwerte einlesen
t, U, I, R = np.genfromtxt('rawdata/m.txt', unpack = True)
#Einheiten anpassen:
I = I/1000
#Temperatur umrechnen:
def TR(R):
	return 0.00134*R**2 + 2.296*R - 243.02
Tt = TR(R)
T = np.zeros(len(Tt)+1)
T[0] = TR(23.7)
for i in range(len(Tt)):
	T[i+1] = Tt[i]
T = T + 273.15
#print(T)
#Temperaturdifferenzen
dT = np.zeros(len(T)-1)
for i in range(len(T)-1):
	dT[i] = T[i+1] - T[i]
#print(dT)	
#Energie bestimmen/ bzw. die zugeführte Wärmemenge
E = U * I * t
#print(t)
#Conclusio: Verwende die Funktion für alpha
perr = np.sqrt(np.diag(covs))
param = unp.uarray(params, perr)
#print(param)
alpha = param[2]*unp.log(param[0]*T+param[1])
#print(alpha)
#Cp bestimmen

