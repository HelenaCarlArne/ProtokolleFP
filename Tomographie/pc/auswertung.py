import numpy as np
import uncertainties
import uncertainties.unumpy as unp

array=np.array([182333,63058,63098,62991, 6361,10509,
10692,10940,6447,11279,10401,10737,10720,13163,12112,
11262,1105,1729, 2314, 2539, 1037, 4671, 2223, 2528,
3610,5777, 2662, 3454,12503,62255, 3108,61660,11767,
19961,19552,19589,17596,15917,15361,16543])

print(np.mean([6361,10509,
10692,10940,6447,11279,10401,10737,10720,13163,12112,
11262]))

print(np.mean([1105,1729, 2314, 2539, 1037, 4671, 2223, 2528,
3610,5777, 2662, 3454]))

print(np.mean([12503,62255, 3108,61660,11767,
19961,19552,19589,17596,15917,15361,16543]))

print("Würfel 1,2,4")
print("Projektionen in der Reihe")
print("")
print(unp.log(unp.uarray(array[2],np.sqrt(array[2]))/unp.uarray(array[4],np.sqrt(array[4]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[5],np.sqrt(array[5]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[6],np.sqrt(array[6]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[7],np.sqrt(array[7]))))
print(unp.log(unp.uarray(array[2],np.sqrt(array[2]))/unp.uarray(array[8],np.sqrt(array[8]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[9],np.sqrt(array[9]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[10],np.sqrt(array[10]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[11],np.sqrt(array[11]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[12],np.sqrt(array[12]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[13],np.sqrt(array[13]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[14],np.sqrt(array[14]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[15],np.sqrt(array[15]))))
print("")
print(unp.log(unp.uarray(array[2],np.sqrt(array[2]))/unp.uarray(array[16],np.sqrt(array[16]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[17],np.sqrt(array[17]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[18],np.sqrt(array[18]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[19],np.sqrt(array[19]))))
print(unp.log(unp.uarray(array[2],np.sqrt(array[2]))/unp.uarray(array[20],np.sqrt(array[20]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[21],np.sqrt(array[21]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[22],np.sqrt(array[22]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[23],np.sqrt(array[23]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[24],np.sqrt(array[24]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[25],np.sqrt(array[25]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[26],np.sqrt(array[26]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[27],np.sqrt(array[27]))))
print("")
print(unp.log(unp.uarray(array[2],np.sqrt(array[2]))/unp.uarray(array[28],np.sqrt(array[28]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[29],np.sqrt(array[29]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[30],np.sqrt(array[30]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[31],np.sqrt(array[31]))))
print(unp.log(unp.uarray(array[2],np.sqrt(array[2]))/unp.uarray(array[32],np.sqrt(array[32]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[33],np.sqrt(array[33]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[34],np.sqrt(array[34]))))
print(unp.log(unp.uarray(array[1],np.sqrt(array[1]))/unp.uarray(array[35],np.sqrt(array[35]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[36],np.sqrt(array[36]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[37],np.sqrt(array[37]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[38],np.sqrt(array[38]))))
print(unp.log(unp.uarray(array[3],np.sqrt(array[3]))/unp.uarray(array[39],np.sqrt(array[39]))))
print("")
"""
    00    rawdata/Daten_von_Robert/Initial.dat
    01    rawdata/Daten_von_Robert/Leerwuerfel_gerade.dat
    02    rawdata/Daten_von_Robert/Leerwuerfel_diagonal.dat
    03    rawdata/Daten_von_Robert/Leerwuerfel_halbdiagonal.dat
    04    rawdata/Daten_von_Robert/Wuerfel_1_Proj_01.dat
    05    rawdata/Daten_von_Robert/Wuerfel_1_Proj_02.dat
    06    rawdata/Daten_von_Robert/Wuerfel_1_Proj_03.dat
    07    rawdata/Daten_von_Robert/Wuerfel_1_Proj_04.dat
    08    rawdata/Daten_von_Robert/Wuerfel_1_Proj_05.dat
    09    rawdata/Daten_von_Robert/Wuerfel_1_Proj_06.dat
    10    rawdata/Daten_von_Robert/Wuerfel_1_Proj_07.dat
    11    rawdata/Daten_von_Robert/Wuerfel_1_Proj_08.dat
    12    rawdata/Daten_von_Robert/Wuerfel_1_Proj_09.dat
    13    rawdata/Daten_von_Robert/Wuerfel_1_Proj_10.dat
    14    rawdata/Daten_von_Robert/Wuerfel_1_Proj_11.dat
    15    rawdata/Daten_von_Robert/Wuerfel_1_Proj_12.dat
    16    rawdata/Daten_von_Robert/Wuerfel_2_Proj_01.dat
    17    rawdata/Daten_von_Robert/Wuerfel_2_Proj_02.dat
    18    rawdata/Daten_von_Robert/Wuerfel_2_Proj_03.dat
    19    rawdata/Daten_von_Robert/Wuerfel_2_Proj_04.dat
    20    rawdata/Daten_von_Robert/Wuerfel_2_Proj_05.dat
    21    rawdata/Daten_von_Robert/Wuerfel_2_Proj_06.dat
    22    rawdata/Daten_von_Robert/Wuerfel_2_Proj_07.dat
    23    rawdata/Daten_von_Robert/Wuerfel_2_Proj_08.dat
    24    rawdata/Daten_von_Robert/Wuerfel_2_Proj_09.dat
    25    rawdata/Daten_von_Robert/Wuerfel_2_Proj_10.dat
    26    rawdata/Daten_von_Robert/Wuerfel_2_Proj_11.dat
    27    rawdata/Daten_von_Robert/Wuerfel_2_Proj_12.dat
    28    rawdata/Daten_von_Robert/Wuerfel_4_Proj_01.dat
    29    rawdata/Daten_von_Robert/Wuerfel_4_Proj_02.dat
    30    rawdata/Daten_von_Robert/Wuerfel_4_Proj_03.dat
    31    rawdata/Daten_von_Robert/Wuerfel_4_Proj_04.dat
    32    rawdata/Daten_von_Robert/Wuerfel_4_Proj_05.dat
    33    rawdata/Daten_von_Robert/Wuerfel_4_Proj_06.dat
    34    rawdata/Daten_von_Robert/Wuerfel_4_Proj_07.dat
    35    rawdata/Daten_von_Robert/Wuerfel_4_Proj_08.dat
    36    rawdata/Daten_von_Robert/Wuerfel_4_Proj_09.dat
    37    rawdata/Daten_von_Robert/Wuerfel_4_Proj_10.dat
    38    rawdata/Daten_von_Robert/Wuerfel_4_Proj_11.dat
    39    rawdata/Daten_von_Robert/Wuerfel_4_Proj_12.dat
"""

# print("WUERFEL: 1,2,4")
# print("Intensität: Projektion 1")
# print(np.log(array[2]/array[4]),np.log(array[2]/array[16]),np.log(array[2]/array[28]))
# print("")
# print("Intensität: Projektion 2")
# print(np.log(array[1]/array[5]),np.log(array[1]/array[17]),np.log(array[1]/array[29]))
# print("")
# print("Intensität: Projektion 3")
# print(np.log(array[1]/array[6]),np.log(array[1]/array[18]),np.log(array[1]/array[30]))
# print("")
# print("Intensität: Projektion 4")
# print(np.log(array[1]/array[7]),np.log(array[1]/array[19]),np.log(array[1]/array[31]))
# print("")
# print("Intensität: Projektion 5")
# print(np.log(array[2]/array[8]),np.log(array[2]/array[20]),np.log(array[2]/array[32]))
# print("")
# print("Intensität: Projektion 6")
# print(np.log(array[1]/array[9]),np.log(array[1]/array[21]),np.log(array[1]/array[33]))
# print("")
# print("Intensität: Projektion 7")
# print(np.log(array[1]/array[10]),np.log(array[1]/array[22]),np.log(array[1]/array[34]))
# print("")
# print("Intensität: Projektion 8")
# print(np.log(array[1]/array[11]),np.log(array[1]/array[23]),np.log(array[1]/array[35]))
# print("")
# print("Intensität: Projektion 9")
# print(np.log(array[3]/array[12]),np.log(array[3]/array[24]),np.log(array[3]/array[36]))
# print("")
# print("Intensität: Projektion 10")
# print(np.log(array[3]/array[13]),np.log(array[3]/array[25]),np.log(array[3]/array[37]))
# print("")
# print("Intensität: Projektion 11")
# print(np.log(array[3]/array[14]),np.log(array[3]/array[26]),np.log(array[3]/array[38]))
# print("")
# print("Intensität: Projektion 12")
# print(np.log(array[3]/array[15]),np.log(array[3]/array[27]),np.log(array[3]/array[39]))
# print("")

print("Mittelwert: Würfel 1")
print(np.sum([0.6189,0.5893,0.5499,0.5472,0.5217,0.6440,0.5802,0.6361,0.5016])/9)

print("Mittelwert: Würfel 2")
print(np.sum([1.3419,1.0039,0.9754,0.9178,1.0033,0.9919,0.9982,1.26,0.67])/9)

#
#  Lösen der Matrix-Gleichung durch TI- Voyage 200
#
