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
import math as m
from random import randint, random
import uncertainties.unumpy as unp
from uncertainties import ufloat


#Test-Werte
val1=np.array(5*[randint(0,9)])
val2=np.array(5*[random()])
val3=unp.uarray([1.13,2.212,31,4,5],[0.31,0.000001,3,2,1])


def tableit(tabname,beschreibung,*datenarray): # Kernfunktion
	pass
>>>>>>> c7efc719d92fc83d6287d1cd04e19975afc09708

#Runden Funktionen
def rts(x):							#Runden
	if x:
		return round(x, -int(m.floor(m.log10(abs(x)))))
	else:
		return 0
<<<<<<< HEAD
def vks(x): 						#Vorkommastellen
	l = np.max(x)
	if l:
		return m.floor(m.log10(m.floor(max(x))))
=======

def crts(x): #Anzahl der sign. Nachkommastellen
	if -int(m.floor(m.log10(abs(x))))>0:
		return -int(m.floor(m.log10(abs(x))))
>>>>>>> c7efc719d92fc83d6287d1cd04e19975afc09708
	else:
		return 0
def cuts(x):						#Nachkommastellen
	if-int(m.floor(m.log10(abs(x))))<1:
		return 0
	else:
		return -int(m.floor(m.log10(abs(x))))
def maxcuts(array):					#Für den Tabellenheader die maximale Anzahl der Nachkommastellen nach dem Runden
	m = 0
	for y in range(array):
		if cuts(array[y])>m:
			m = cuts(array[y])
		return m
			
		
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
	f = np.zeros(len(data))
	for i in range(len(data)):
		if(type(data[i][0]) == type(dummy) or type(data[i][0]) == type(dummyarray[1]) or type(data) == type(udummyarray)):
			f[i] = True
		else:
			f[i] = False
	print(f)
	#Runden
	for i in range(len(data)):
		if(f[i]):
			for j in range(data[0]):
				sdevs(data[i][j]) = rts(sdevs(data[i][j]))
				noms(data[i][j]) = round((noms(data[i][j]), -int(m.floor(m.log10(abs(x))))))
							
			
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
	

def makedata(*datenarray): # Bildet eine Matrix aus den gerundeten Arrays
	stm=np.array([])
	for array in datenarray:
		stm=np.append(stm,len(array))
	if min(stm)==max(stm):
		stm=np.array([])
		data=np.array(datenarray)
		return data
	else:
		data=np.array([])
		print("\nDie Daten-Arrays passen nicht zusammen!\n\n")
		raise TypeError

def gettype(*datenarray): # Ermittelt den Datentyp der Arrays und rundet entsprechend
	global stm # schweizer taschenmesser
	stm=np.array([])
	global rundarray
	rundarray=dict()
	for ID,array in enumerate(datenarray):
		rundarray[ID]=np.array([])
		if np.any(unp.std_devs(array)):
			stm=np.append(stm,"fehlerbehaftet")
			for element in array:
				rundarray[ID]=np.append(rundarray[ID],ufloat(round(element.n,crts(element.s)),rts(element.s)))
		if not np.any(unp.std_devs(array)):
			stm=np.append(stm,"normal")
			for element in array:
				rundarray[ID]=np.append(rundarray[ID],round(element,2))
	pass


gettype(val1,val2,val3)
print(stm)
print(rundarray)
