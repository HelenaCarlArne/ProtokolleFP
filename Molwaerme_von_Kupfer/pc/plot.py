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
ak = ak * 10**(-6)
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
sR = 0.1
R = unp.uarray(R, sR) #in ohm
m = 0.342 #in kg
M = 0.063546 #in kg/mol
rho = 8920 #in kg/m³
V0 = M/rho # in m³/mol
K = 1.278 * 10**11 #in N/m²
vl = 4700 # in m/s
vtr = 2260 #in m/s
#print(V0)

#Einheiten anpassen:
I = I/1000 #in A

#Temperatur umrechnen:
def TR(R):
	return 0.00134*R**2 + 2.296*R - 243.02
Tt = TR(R)
T = unp.uarray(np.zeros(len(Tt)+1), 0)
T[0] = TR(ufloat(23.7,0.1))
for i in range(len(Tt)):
	T[i+1] = Tt[i]
T = T + 273.15
#print(T)

#Temperaturdifferenzen
dT = unp.uarray(np.zeros(len(T)-1),0)
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
Cp = M/m * E/dT


#Cv bestimmen
Cv = Cp - 9 *(alpha[1:])**2*V0*T[1:]*K


#Plot
plt.errorbar(noms(T[1:]), noms(Cp),xerr=sdevs(T[1:]), yerr=sdevs(Cp), fmt='bx', label=r'$C_P$')
plt.errorbar(noms(T[1:]), noms(Cv),xerr = sdevs(T[1:]), yerr = sdevs(Cv),fmt='mx', label =r'$C_V$')
plt.grid()
plt.xlabel(r'$T/K$')
plt.ylabel(r'$C_\text{V / P}$')
plt.legend(loc='best')
#plt.show()
plt.savefig('pc/C.pdf')
plt.clf()	

TT = (T[1:])
Cvv = (Cv)
Td = unp.uarray(np.zeros(8),0)
Cvd = unp.uarray(np.zeros(8),0)
for i in range(len(TT)):
	if TT[i]<170:
		Td[i] = TT[i]
		Cvd[i] = Cvv[i]		
#Td und Cvd sind die in Frage kommenden Werte, deb die dazugehörigen Debye Funktionswerte die ich per Hand rausgesucht habe. con.R ist die allgemeine Gaskonstante

deb = np.array([3.7, 2.9, 2.7, 2.8, 2.9, 2.7, 2.5, 2.2])

#theta_D ist thD

thD = (deb*Td**3*9*con.R/Cvd)**(1/3)


MthD = ufloat(np.mean(noms(thD)),np.std(noms(thD))/np.sqrt(len(noms(thD))))
print(MthD)

wd = (1/vl**3 + 2/vtr**3)**(-1/3)*(18*con.N_A*con.pi**2*rho/M)**(1/3) #N_A ist die Loschmidtsche Zahl, pi=3, hbar =1 :D und k die Boltzmannkonstante
#print(wd)
theta_D = con.hbar*wd/con.k
#print(theta_D)


#Tabellen und anderer krasser Shit

#Erstmal Uarray->Array, ist übrigens keine Symmetrietransformation da die Mantissen gekürzt werden
#bei manchen Arrays muss für die Tabelle eine 0 in der ersten Zeile ergänzt werden.
dTt = unp.uarray(np.zeros(len(dT)+1), 0)
dTt[0] = ufloat(69,42)
Cpt = unp.uarray(np.zeros(len(Cp)+1), 0)
Cpt[0] = ufloat(69,42)
Cvt = unp.uarray(np.zeros(len(Cv)+1), 0)
Cvt[0] = ufloat(69,42)
for i in range(len(dT)):
	dTt[i+1] = dT[i]
	Cvt[i+1] = Cv[i]
	Cpt[i+1] = Cp[i]


# Rt=np.zeros(len(R))
# Tt=np.zeros(len(R)) 
# dTtt=np.zeros(len(R)) 
# Cptt=np.zeros(len(R)) 
# Cvtt = np.zeros(len(R))
# Ra = noms(R)
# Rb = sdevs(R)
# for i in range (len(R)):
	# Rt[i] = ufloat(Ra[i], Rb[i])
	# Tt[i] = ufloat(noms(T[i]), sdevs(T[i]))
	# dTtt[i] = ufloat(noms(dTt[i]), sdevs(dTt[i]))
	# Cvtt[i] = ufloat(noms(Cvt[i]), sdevs(Cvt[i]))
	# Cptt[i] = ufloat(noms(Cpt[i]), sdevs(Cpt[i]))
# print(Rt)	


#Tabellen	
data1 = [noms(R), T, dTt, Cvt, Cpt]
p1 = {'name':'pc/tab1.tex', 'data':data1}
table(**p1)

data2 = [U, I, t, E]
p2 = {'name':'pc/En.tex', 'data':data2}
table(**p2)

data3 = [Td, Cvd, deb, thD]
p3 = {'name':'pc/deb.tex', 'data':data3}
table(**p3)

