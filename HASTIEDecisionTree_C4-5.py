StartTest=9600
EndTest = 12000

NodoRaiz=8
Nodo1=8
Nodo2=9
Nodo3=9
Nodo4=10
Nodo5=10
Nodo6=5
Nodo7=5
Nodo8=2
Nodo9=2
Nodo10=3
Nodo11=3
Nodo12=4
Nodo13=4
Nodo14=7
Nodo15=7
Nodo16=6
Nodo17=6
Nodo18=1
Nodo19=1

ValorDecision=150
ValorDecision1=151
ValorDecision2=164
ValorDecision3=163
ValorDecision4=154
ValorDecision5=155
ValorDecision6=153
ValorDecision7=154
ValorDecision8=147
ValorDecision9=146
ValorDecision10=151
ValorDecision11=150
ValorDecision12=137
ValorDecision13=138
ValorDecision14=153
ValorDecision15=152
ValorDecision16=151
ValorDecision17=152
ValorDecision18=238
ValorDecision19=74


NumCampos=11

StartTraining = 0
EndTraining = 9600

import time

Inicio=time.time()

Max=[float(-9.9999E+16)]
Min=[float(9.9999E+16)]
for i in range(NumCampos):
    Max.append(-9.9999E+16)
    Min.append(9.9999E+16)
f=open("C:\Hastie10_2Corrected.txt","r")
Conta=0

    
for linea in f:
    
    lineadelTrain =linea.split(";")
    Conta = Conta + 1
    if Conta < StartTraining:
        continue
    if Conta > EndTraining:
        break
    linea_x =[""]
    z=-1
    for x in lineadelTrain:
   
        z=z+1
        if z==0: continue
        if z==NumCampos: break
        
        if float(lineadelTrain[z]) > Max[z]:
                 Max[z]=float(lineadelTrain[z])
        if float(lineadelTrain[z]) < Min[z]:
                 Min[z]=float(lineadelTrain[z])
       
f.close() 
def CalcIndex(Max, Min, Nodo, ValorNodo, TopeMemoria):
    ValorNodo =ValorNodo - Min[Nodo]
    Maximo = Max[Nodo]
    Maximo = Maximo - Min[Nodo]
    indice =(int) (((TopeMemoria - 2.0) * ValorNodo)/ Maximo)
    if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
            print("index overflowed=" + str( indice) + " in  the field ="+ str(Nodo) )
            indice=TopeMemoria
    return indice            
NumClases=2
NumCampos =11
   
TopeMemoria = 304



Maximo=0.0
Conta=0.0
Cont=-1

TotAciertos=0.0
TotFallos=0.0


f=open("C:\Hastie10_2Corrected.txt","r")

for linea in f:
    
    lineadelTrain =linea.split(";")
    Conta = Conta + 1
    if Conta < StartTest:
        continue
    if Conta > EndTest:
        break
    pp=0
    ClasePredecida=-1.0
    while pp==0:
        pp=1
        ValorTrain =float(lineadelTrain[NodoRaiz])            
        indice=CalcIndex(Max, Min, NodoRaiz, ValorTrain, TopeMemoria)
        if indice < ValorDecision:
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo1])           
        indice=CalcIndex(Max, Min, Nodo1, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision1):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo2])           
        indice=CalcIndex(Max, Min, Nodo2, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision2):
            ClasePredecida=1.0
            break
       
        ValorTrain =float(lineadelTrain[Nodo3])
        indice=CalcIndex(Max, Min, Nodo3, ValorTrain, TopeMemoria)
        if (indice < ValorDecision3):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo4])
        indice=CalcIndex(Max, Min, Nodo4, ValorTrain, TopeMemoria)
        if (indice < ValorDecision4):
            ClasePredecida=1.0
            break
                  
        ValorTrain =float(lineadelTrain[Nodo5])
        indice=CalcIndex(Max, Min, Nodo5, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision5):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo6])
        indice=CalcIndex(Max, Min, Nodo6, ValorTrain, TopeMemoria)
        if (indice < ValorDecision6):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo7])
        indice=CalcIndex(Max, Min, Nodo7, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision7):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo8])
        indice=CalcIndex(Max, Min, Nodo8, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision8):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo9])
        indice=CalcIndex(Max, Min, Nodo9, ValorTrain, TopeMemoria)
        if (indice < ValorDecision9):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo10])
        indice=CalcIndex(Max, Min, Nodo10, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision10):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo11])
        indice=CalcIndex(Max, Min, Nodo11, ValorTrain, TopeMemoria)
        if (indice < ValorDecision11):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo12])
        indice=CalcIndex(Max, Min, Nodo12, ValorTrain, TopeMemoria)
        if (indice < ValorDecision12):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo13])
        indice=CalcIndex(Max, Min, Nodo13, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision13):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo14])
        indice=CalcIndex(Max, Min, Nodo14, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision14):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo15])
        indice=CalcIndex(Max, Min, Nodo15, ValorTrain, TopeMemoria)
        if (indice < ValorDecision15):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo16])
        indice=CalcIndex(Max, Min, Nodo16, ValorTrain, TopeMemoria)
        if (indice < ValorDecision16):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo17])
        indice=CalcIndex(Max, Min, Nodo17, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision17):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo18])
        indice=CalcIndex(Max, Min, Nodo18, ValorTrain, TopeMemoria)
        if (indice >= ValorDecision18):
            ClasePredecida=1.0
            break
        
        ValorTrain =float(lineadelTrain[Nodo19])
        indice=CalcIndex(Max, Min, Nodo19, ValorTrain, TopeMemoria)
        if (indice < ValorDecision19):
            ClasePredecida=1.0
            break
    
   
        
    ClaseLeida=float(lineadelTrain[0])
    if ClaseLeida==ClasePredecida:
        TotAciertos=TotAciertos+1
    else:
       TotFallos=TotFallos+1 
   
f.close()    
print("") 
print("Total Hits = " + str(TotAciertos)) 
print("Total Failures = " + str(TotFallos))                                                                                      

Fin =time.time()  
print ( "")
print( " Time = " + str(Fin - Inicio) )
    