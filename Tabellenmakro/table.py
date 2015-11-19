import math as m
import numpy as np

def rts(x): #Rundet auf eine sign. Stelle
	if x:
		return round(x,-int(m.floor(m.log10(abs(x)))))
	else:
		return 0

def cuts(x): #Anzahl der sign. Nachkommastellen
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

test =np.array(
	[1.12,
	2.2,
	3.1,
	0.000000000001,
	123,
	312432.1,
	12.332,
	16.21,
	0.003,
	0.1,
	0.01,
	0.000021])

for x in test:
	print("%s\n%s, \nNachkommastellen: %s\n"%(x,rts(x),cuts(x))) 

print(maxcuts(test))