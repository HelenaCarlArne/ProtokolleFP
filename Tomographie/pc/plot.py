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
import os, os.path

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


# Dies plottet alle von Robert ausgegebenen Daten graphisch:
#
# ACHTUNG: ES DÜRFEN KEINERLEI FALSCHE DATEIEN IM ORDNER LIEGEN, etwa .DS_Store
# oder ähnlich
#
# Dauer: etwa eine Minute

plt.plot([0,1],[0,1],"kx") # Für die Zeitmarke der Makefile
plt.savefig("pc/plt.pdf")
plt.close()

print("Plotte alle von Robert ausgegebenen Daten graphisch")
intensity = np.array([])
print("")
for root, _, files in os.walk("rawdata/Daten_von_Robert/"):
    for f in files:
        fullpath = os.path.join(root, f)
        print(fullpath)
        x,y = np.genfromtxt("{}".format(fullpath), unpack=True)
        plt.plot(x,y,"k-",label="{}".format(f))
        plt.legend(loc='best')
        plt.xlim(0,len(x))
        plt.ylim(0,max(y)+100)
        plt.axvline(250,color='k', linestyle='dotted')
        plt.axvline(285,color='k', linestyle='dotted')
        plt.title("I={}".format(np.sum(y[250:285])))
        intensity=np.append(intensity,np.sum(y[250:285]))
        plt.xlabel("Kanäle")
        plt.ylabel("Zerfälle")
        plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
        plt.savefig('pc/{}.pdf'.format(f))
        plt.close()
print("")
print("Alle auftretenden integrierten Intensitäten")
print(intensity, sep=",")
# Dies plottet Leerwuerfel_gerade einzeln, da es ein eigenes Format hat:
# Dauer: etwa eine Minute


y = np.genfromtxt("rawdata/Leerwuerfel_gerade.dat", unpack=True)
x = np.arange(0,1024)
plt.plot(x,y,"k-",label="Leerwuerfel_gerade")
plt.legend(loc='best')
plt.xlim(0,len(x))
plt.ylim(0,max(y)+100)
plt.title("I={}".format(np.sum(y[250:285])))
plt.axvline(250,color='k', linestyle='dotted')
plt.axvline(285,color='k', linestyle='dotted')
plt.xlabel("Kanäle")
plt.ylabel("Zerfälle")
plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/Leerwuerfel_gerade.pdf')
plt.close()

print("")
print("Plotte die Literaturwerte für Abs.koeff.")

x1,x2,x3,x4 = np.genfromtxt("rawdata/aluminum.txt").T
plt.plot(x1,x2,'g-',label="Compton-Streuung")
plt.plot(x1,x3,'b-',label="Photoeffekt")
plt.plot(x1,x4,'k-',label="kombiniert")
plt.legend(loc='best')
plt.title("Aluminium")
plt.xlim(0.5,1)
plt.axvline(0.662,color='k', linestyle='dotted',label="Energie des Strahlers")
plt.xlabel(r"Energie in \si{\mega\electronvolt}")
plt.ylabel("Absorptionskoeffizient in \si{\centi\meter\squared\per\gram}")
plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/aluminum.pdf')
plt.close()
x1,x2,x3,x4 = np.genfromtxt("rawdata/brass.txt").T
plt.plot(x1,x2,"g-",label="Compton-Streuung")
plt.plot(x1,x3,"b-",label="Photoeffekt")
plt.plot(x1,x4,"k-",label="kombiniert")
plt.legend(loc='best')
plt.title("Brass")
plt.xlim(0.5,1)
plt.axvline(0.662,color='k', linestyle='dotted',label="Energie des Strahlers")
plt.xlabel(r"Energie in \si{\mega\electronvolt}")
plt.ylabel("Absorptionskoeffizient in \si{\centi\meter\squared\per\gram}")
plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/brass.pdf')
plt.close()
x1,x2,x3,x4 = np.genfromtxt("rawdata/iron.txt").T
plt.plot(x1,x2,"g-",label="Compton-Streuung")
plt.plot(x1,x3,"b-",label="Photoeffekt")
plt.plot(x1,x4,"k-",label="kombiniert")
plt.legend(loc='best')
plt.title("Iron")
plt.xlim(0.5,1)
plt.axvline(0.662,color='k', linestyle='dotted',label="Energie des Strahlers")
plt.xlabel(r"Energie in \si{\mega\electronvolt}")
plt.ylabel("Absorptionskoeffizient in \si{\centi\meter\squared\per\gram}")
plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/iron.pdf')
plt.close()
x1,x2,x3,x4 = np.genfromtxt("rawdata/lead.txt").T
plt.plot(x1,x2,"g-",label="Compton-Streuung")
plt.plot(x1,x3,"b-",label="Photoeffekt")
plt.plot(x1,x4,"k-",label="kombiniert")
plt.legend(loc='best')
plt.title("Lead")
plt.xlim(0.5,1)
plt.axvline(0.662,color='k', linestyle='dotted',label="Energie des Strahlers")
plt.xlabel(r"Energie in \si{\mega\electronvolt}")
plt.ylabel("Absorptionskoeffizient in \si{\centi\meter\squared\per\gram}")
plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/lead.pdf')
plt.close()
x1,x2,x3,x4 = np.genfromtxt("rawdata/pom.txt").T
plt.plot(x1,x2,"g-",label="Compton-Streuung")
plt.plot(x1,x3,"b-",label="Photoeffekt")
plt.plot(x1,x4,"k-",label="kombiniert")
plt.legend(loc='best')
plt.title("Delrin")
plt.xlim(0.5,1)
plt.axvline(0.662,color='k', linestyle='dotted',label="Energie des Strahlers")
plt.xlabel(r"Energie in \si{\mega\electronvolt}")
plt.ylabel("Absorptionskoeffizient in \si{\centi\meter\squared\per\gram}")
plt.tight_layout(pad=0.2, h_pad=1.08, w_pad=1.08)
plt.savefig('pc/pom.pdf')
plt.close()
