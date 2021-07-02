"""
META            :   Determinar la proporción de cpromedios de por alerta y dar los mejores y peores

ANÁLISIS    
    Entradas    :   [n], entrada la cantidad de ciudades (n) a analizar==> Se lee una vez
                    [m], cantidad total de lecturas de los distintos sensores (m) ==> Se lee una vez
                    [ica], Resultado de la prueba de habilidad técnica, float, >= 0   ==> Se leen n veces

    Salidas     :   1)número de la ciudad con el mejor promedio del ICA, seguido de su valor y la alerta.
                    2)número de la ciudad con el peor promedio del ICA, seguido de su valor y la alerta.
                    3) se debe mostrar cada números que presentó la alerta por ciudad, es decir,
                    Verde  amarillo naranja  rojo morado marron
                    0        0        0        0    0      2
                    4) cantidades de alerta por encima del debajo, igual a él, o por encima
                    Por debajo  |  igual al promedio | por encima
                     0          |       0            |   1 

    Proceso     :   1) Leer la cantidad de cIUDADES a examinar (Deberá ser >0)
                    2) Para cada ciuDAD leer [c], (Deberá validarse que sean >= 0)
                    3) Contar la ciudad con el mayor ica promedio
                    4) contar la ciudad con el menor ica promedio
                    5) Generar el porcentaje de icas promedio por alerta

     0        1       2       3         4         5        6        7       8      9         10
| CIUDAD  | MAYOR | MENOR | SUMA   |  CUENTA |  VERDE  |AMARILLO| NARANJA| ROJO | MORADO | MARRON |
+---------+-------+-------+--------+---------+---------+--------+--------+------+--------+--------+
|    1    |  0    |  0    |   0    |    0    |     0   |   0    |    0   |  0   |    0   |   0    |
+---------+-------+-------+--------+---------+---------+--------+--------+------+--------+--------+
|    1    |  0    |  0    |   0    |    0    |     0   |   0    |   0    |  0   |    0   |   0    |
+---------+-------+-------+--------+---------+---------+--------+--------+------+--------+--------+
|    1    |  0    |  0    |   0    |    0    |     0   |   0    |   0    |  0   |    0   |   0    |
+---------+-------+-------+--------+---------+---------+--------+--------+------+--------+--------+
1  63000   24C  ==>  = 63000
"""


conteoverde=0
conteoamarillo=0
conteonaranja=0
conteorojo=0
conteomorado=0
conteomarron=0
cicapro=0
cicamen=0
cicamay=0

while True:
    #lea como texto
    tmp=input()
    #2) divida lo que se leyó 
        
    dat=tmp.split()
    #3) convierta (en la posición
    if dat[0].isdigit() :
        n=int(dat[0])
        m=int(dat[1])
        break
#leer los datos de la ciudad (cantidad de mediciones)

datos= []
for i in range (m):
    #se procede a leer los datos de las mediciones
    while True:
        #lea como un texto
        tmp=input()
        # 2) divide lo que se leyó 
        dat= tmp.split()
        #3) convierte (en la posición 0 está el número de la ciudad y en la posición 1 el valor de la lectura)
        if dat[0].isdigit() :
            ciu=int(dat[0])
            lec=float(dat[1])
            print(ciu,lec)
            if 0<=lec<500.5:
                break
    datos.append([ciu, lec])
#procesar los datos
# creo la matriz de resultados (tantas filas como ciudades-)
resultados=[]
for i in range (n):
    fil = [0]*14
    fil[0] = i+1  # se coloca el numero de la ciudad
    fil[1] = -2000  # para el mayor se coloca un valor pequeño
    fil[2] = 2000 # para el menor se coloca un valor grande
    fil[3] = 0
    fil[4] = 0
       
    resultados.append(fil)

for ele in datos:
    #calcular el ica
    ciu = ele [0]
    lec = ele [1]
    if 0<=lec<15.5:
        Il=0
        Ih=50
        Bpl=0
        Bph=15.4
    elif 15.5<=lec<40.5:
        Il=51
        Ih=100
        Bpl=15.5
        Bph=40.4
    elif 40.5<=lec<65.5:
        Il=101
        Ih=150
        Bpl=40.5
        Bph=65.4 
    elif 65.5<=lec<150.5:
        Il=151
        Ih=200
        Bpl=65.5
        Bph= 150.4  
    elif 150.5<=lec<250.5:
        Il=201
        Ih=300
        Bpl=150.5
        Bph=250.4
    elif 250.5<=lec<350.5:
        Il=301
        Ih=400
        Bpl=250.5
        Bph=350.4 
    elif 350.5<=lec<500.5:
        Il=401
        Ih=500
        Bpl=350.5
        Bph=500.4  
    else: 
        Il=Ih=Bpl=bph=0
        
    if Il>=0:
        ica=((Ih-Il)/(Bph-Bpl))*(lec-Bpl)+Il
        #se determina el color de la alerta
        if ((ica>=0) and (ica<=50)):
            conteoverde=1
        elif ((ica>50) and (ica<=100)):
            conteoamarillo=1
        elif ((ica>100) and (ica<=150)):
            conteonaranja=1
        elif ((ica>150) and (ica<=200)):
            conteorojo=1
        elif ((ica>200) and (ica<=300)):
            conteomorado=1
        elif (ica>300):
            conteomarron=1
        idx=ciu -1
        if resultados[idx][1]<ica:
            resultados[idx][1]=ica
        if resultados[idx][2]>ica:
            resultados[idx][2]=ica
        resultados[idx][3]+=ica
        resultados[idx][4]+= 1
        if resultados[idx][4]>0:
            resultados[idx][5]+=conteoverde
        else:
            resultados[idx][5]=0
        if resultados[idx][4]>0:
            resultados[idx][6]+=conteoamarillo
        else:
            resultados[idx][6]=0
        if resultados[idx][4]>0:
            resultados[idx][7]+=conteonaranja
        else:
            resultados[idx][7]=0
        if resultados[idx][4]>0:
            resultados[idx][8]+=conteorojo
        else:
            resultados[idx][8]=0
        if resultados[idx][4]>0:
            resultados[idx][9]+=conteomorado
        else:
            resultados[idx][9]=0
        if resultados[idx][4]>0:
            resultados[idx][10]+=conteomarron
        else:
            resultados[idx][10]=0
        resultados[idx][11]+=cicamen
        resultados[idx][12]+=cicapro
        resultados[idx][13]+=cicamay
    resultados2=[]
    filas = [0]*2
    filas[0] = ciu
    filas[1] = ica # se coloca el numero de la ciudad
    resultados2.append(filas)
    print(resultados2)

    #print(f"{ciu} {ica:.2f}") 
       
# se imprimen los resultados

for fil in resultados: 
    print(fil[0])
    if fil[4]>0:
        pro=fil[3]/fil[4]
    else:
        pro = 0
    if ica==pro:
        cicapro=1
    else:
        cicapro=0
    if ica<pro:
        cicamen=1
    else:
        cicamen=0
    if ica>pro:
        cicamay=1
    else:
        cicamay=0
    if fil[2]==2000:
        fil[2]=0
    if fil[1]==-2000:
        fil[1]=0
    print(f"{fil[2]:.2f} {pro:.2f} {fil[1]:.2f} ")
    print(f"{fil[5]} {fil[6]} {fil[7]} {fil[8]} {fil[9]} {fil[10]}")
    #print(f"{fil[0]} {fil[2]:.2f} {pro:.2f} {fil[1]:.2f} {fil[3]:.2f}")
    #se determina el color de la alerta
"""
#        0        1      2       3       4        5
#|  VERDE  |AMARILLO| NARANJA| ROJO | MORADO | MARRON |
#+---------+-------+-------+--------+---------+-------+    


for i in range (len(resultados)):
    if resultados[i][11]>0:
        ica==pro:
            resultados[idx][12]+=cicapro
        if ica<pro:
            resultados[idx][12]+=cicamen
        if ica>pro:
            resultados[idx][12]+=cicamay



#    print(f"{fil[11]} {fil[12]} {fil[13]} ")

#print(resultados)
#     0        1       2       3         4         5        6         7      8      9        10
#| CIUDAD  | MAYOR | MENOR | SUMA   |  CUENTA |  VERDE  |AMARILLO| NARANJA| ROJO | MORADO | MARRON |
#+---------+-------+-------+--------+---------+---------+--------+--------+------+--------+--------+
#    11         12       13
#| cicamay | cicapro | cicamen|
"""