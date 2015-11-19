import math as m
import numpy as np
from random import randint, random
import uncertainties.unumpy as unp
from uncertainties import ufloat


#Test-Werte
val1=np.array(5*[randint(0,9)])
val2=np.array(5*[random()])
val3=unp.uarray([1.13,2.212,31,4,5],[0.31,0.000001,3,2,1])


def tableit(tabname,beschreibung,*datenarray): # Kernfunktion
	pass

def rts(x): #Rundet auf eine sign. Stelle
	if x:
		return round(x,-int(m.floor(m.log10(abs(x)))))
	else:
		return 0

def crts(x): #Anzahl der sign. Nachkommastellen
	if -int(m.floor(m.log10(abs(x))))>0:
		return -int(m.floor(m.log10(abs(x))))
	else:
		return 0

def maxcuts(array): # Maximale Nachkommastelle eines Arrays
	m=0
	for i in array:
		if cuts(i)>m:
			m=cuts(i)
	return m

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
