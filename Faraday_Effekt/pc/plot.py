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
	


#Methwerte einlesen
sk, Bp, Bn = np.genfromtxt('pc/mag.txt', unpack = True)
d1 = 1.36
d2 = 1.296
d3 = 5.11

N1 = 1.2*10**24
N2 = 2.8*10**24
n  = 3.4

l, thp1, thp2, thp3 = np.genfromtxt('pc/bp.txt', unpack = True)
l, thn1, thn2, thn3 = np.genfromtxt('pc/bn.txt', unpack = True)

th1 = abs(1/2 * (thp1-thn1)/d1)
th2 = abs(1/2 * (thp2-thn2)/d2)
th3 = abs(1/2 * (thp3-thn3)/d3)

sk = sk - 69

e0 = 1.602 * 10 **(-19)
eps0 = 8.854 * 10 **(-12)
c = 3*10**8
B = 447.5 * 10 ** (-3)
m0 = 9.109*10**(-31)



#B-Feld

plt.plot(sk, Bp,'rx', label='B positiv gepolt')
plt.plot(sk, Bn,'bx', label='B negativ gepolt')

plt.xlabel(r'Abstand von der Probe in $\si{\milli\meter}$')
plt.ylabel(r'$B \:/\: \si{\milli\tesla}$')
plt.legend(loc='best', fancybox=True, shadow=True)
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/plot.pdf')
plt.clf()

#Rotation

plt.plot(l, th1,'r.', label=r'$N = 1{,}2 \cdot 10^{18} \si{\per\cubic\centi\meter}$')
plt.plot(l, th2,'bx', label=r'$N = 2{,}8 \cdot 10^{18} \si{\per\cubic\centi\meter}$')
plt.plot(l, th3,'kx', label='rein')

plt.xlabel(r'$\lambda\:/\: \si{\micro\meter}$')
plt.ylabel(r'$\frac{\theta}{d} \:/\: \si{\degree\per\milli\meter}$')
plt.ylim([0,9])
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/rot.pdf')
plt.clf()

th11 = th1/180*np.pi
th22 = th2/180*np.pi
th33 = th3/180*np.pi

th1 = (th11-th33)
th2 = (th22-th33)

def reg(x, a):
	return a*x

t = np.linspace(0,7, 1000)

#Probe 1

param1, cov1 = curve_fit(reg, l**2, th1)

plt.plot(l**2, th1, 'bx', label=r'$N_1 = 1{,}2 \cdot 10^{18} \si{\per\cubic\centi\meter}$, Messwerte')
plt.plot(t, reg(t, *param1), 'b-', label='fit')

#Probe 2

param2, cov2 = curve_fit(reg, l**2, th2)

plt.plot(l**2, th2, 'rx', label=r'$N_2 = 2{,}8 \cdot 10^{18} \si{\per\cubic\centi\meter}$, Messwerte')
plt.plot(t, reg(t, *param2), 'r-', label='fit')

plt.xlabel(r'$\lambda²\:/\: \si{\square\micro\meter}$')
plt.ylabel(r'$\frac{\theta_i}{d_i} - \frac{\theta_\text{rein}}{d_\text{rein}} \:/\: \si{\radian\per\milli\metre}$')
plt.xlim(1,8)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/p.pdf')
plt.clf()







#Effektive Masse Probe 1
param1 = correlated_values(param1, cov1)

a1 = param1[0]*10**15

m1 = unp.sqrt(e0**3*N1*B/(n*8*np.pi**2*eps0*c**3*a1))

print(m1)
print(param1)

#Effektive Masse Probe 2

param2 = correlated_values(param2, cov2)

a2 = param2[0]*10**15

m2 = unp.sqrt(e0**3*N2*B/(n*8*np.pi**2*eps0*c**3*a2))

print(m2)
print(param2)

m1e = m1/m0
m2e = m2/m0

print(m1e)
print(m2e)



#Tabellen
#data1 = [a,b,c,d,e]
#p1 = {'name':'tabelle1.tex','data':data1}
#table(**p1)

dataB = [sk, Bp, Bn]
pB = {'name':'B.tex','data':dataB}
#table(**pB)

datath1 = [l, thp1, thn1, th11]
pth1 = {'name':'th1.tex', 'data':datath1}
#table(**pth1)

datath2 = [l, thp2, thn2, th22]
pth2 = {'name':'th2.tex', 'data':datath2}
#table(**pth2)

datath3 = [l, thp3, thn3, th33]
pth3 = {'name':'th3.tex', 'data':datath3}
#table(**pth3)

datathr = [l**2, th1, th2]
pthr = {'name':'thr.tex', 'data':datathr}
#table(**pthr)





