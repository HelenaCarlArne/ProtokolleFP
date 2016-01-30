import numpy as np

array=np.array([182333,63058,63098,62991, 6361,10509,
10692,10940,6447,11279,10401,10737,10720,13163,12112,
11262,1105,1729, 2314, 2539, 1037, 4671, 2223, 2528,
3610,5777, 2662, 3454,12503,62255, 3108,61660,11767,
19961,19552,19589,17596,15917,15361,16543])

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

print("WUERFEL: 1,2,4")
print("Intensität: Projektion 1")
print(np.log(array[2]/array[4]),np.log(array[2]/array[16]),np.log(array[2]/array[28]))
print("")
print("Intensität: Projektion 2")
print(np.log(array[1]/array[5]),np.log(array[1]/array[17]),np.log(array[1]/array[29]))
print("")
print("Intensität: Projektion 3")
print(np.log(array[1]/array[6]),np.log(array[1]/array[18]),np.log(array[1]/array[30]))
print("")
print("Intensität: Projektion 4")
print(np.log(array[1]/array[7]),np.log(array[1]/array[19]),np.log(array[1]/array[31]))
print("")
print("Intensität: Projektion 5")
print(np.log(array[2]/array[8]),np.log(array[2]/array[20]),np.log(array[2]/array[32]))
print("")
print("Intensität: Projektion 6")
print(np.log(array[1]/array[9]),np.log(array[1]/array[21]),np.log(array[1]/array[33]))
print("")
print("Intensität: Projektion 7")
print(np.log(array[1]/array[10]),np.log(array[1]/array[22]),np.log(array[1]/array[34]))
print("")
print("Intensität: Projektion 8")
print(np.log(array[1]/array[11]),np.log(array[1]/array[23]),np.log(array[1]/array[35]))
print("")
print("Intensität: Projektion 9")
print(np.log(array[3]/array[12]),np.log(array[3]/array[24]),np.log(array[3]/array[36]))
print("")
print("Intensität: Projektion 10")
print(np.log(array[3]/array[13]),np.log(array[3]/array[25]),np.log(array[3]/array[37]))
print("")
print("Intensität: Projektion 11")
print(np.log(array[3]/array[14]),np.log(array[3]/array[26]),np.log(array[3]/array[38]))
print("")
print("Intensität: Projektion 12")
print(np.log(array[3]/array[15]),np.log(array[3]/array[27]),np.log(array[3]/array[39]))
print("")

print("Mittelwert: Würfel 1")
print(np.sum([0.6189,0.5893,0.5499,0.5472,0.5217,0.6440,0.5802,0.6361,0.5016])/9)

print("Mittelwert: Würfel 2")
print(np.sum([1.3419,1.0039,0.9754,0.9178,1.0033,0.9919,0.9982,1.26,0.67])/9)

#
#  Lösen der Matrix-Gleichung durch TI- Voyage 200
#
