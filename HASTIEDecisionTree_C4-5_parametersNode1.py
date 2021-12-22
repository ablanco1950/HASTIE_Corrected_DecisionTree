Campo=8
NodoRaiz=8


ValorDecision=150


import numpy as np
import math

NumCampos=11
Start = 0
End = 9600
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
    if Conta < Start:
        continue
    if Conta > End:
        break
    linea_x =[""]
    z=-1
    for x in lineadelTrain:
   
        z=z+1
        if z==0: continue
        if z==NumCampos: break
        #if z==1: linea_x[0]=float(lineadelTrain[z])
        #else:  linea_x.append(float(lineadelTrain[z]))
        if float(lineadelTrain[z]) > Max[z]:
                 Max[z]=float(lineadelTrain[z])
        if float(lineadelTrain[z]) < Min[z]:
                 Min[z]=float(lineadelTrain[z])
       
#for i in range(NumCampos):
#    print(" i ="+ str(i) + " MAX="+ str(Max[i]) + " MIN=" + str(Min[i])) 


""" CLASIFIER FUNCTION ==========================================================="""

def Hastie_C4_5( W):
    
        
        NumClases=2
        NumCampos =11
       
        TopeMemoria = 304
        
        # Got frm https://stackoverflow.com/questions/15448594/how-to-add-elements-to-3-dimensional-array-in-python
        TabVotos = np.zeros((NumCampos,TopeMemoria+1,NumClases))
        
        Maximo=0.0
        Conta=0.0
        Cont=-1
        
        ContClase=[float(0.0)]
        for j in range(NumClases):
             ContClase.append(float(0.0))
       
        Start=0
        End = 9600
       
    
       
        f=open("C:\Hastie10_2Corrected.txt","r")
        
        
        for linea in f:
            
            lineadelTrain =linea.split(";")
            Conta = Conta + 1
            if Conta < Start:
                continue
            if Conta > End:
                break
            #  la primera vez se computan todos los campos
            # La segunda los que estan a la derecha del nodo raiz y a la izquierda
            
            ValorTrain =float(lineadelTrain[NodoRaiz])
            ValorTrain =ValorTrain - Min[NodoRaiz]
            Maximo = Max[NodoRaiz]
            Maximo = Maximo - Min[NodoRaiz]
            indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
            if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                    print("index overflowed=" + str( indice) + " in  the field ="+ str(ValorDecision) )
                    indice=TopeMemoria
            # if indice <= 150 is class 1.0
            if indice < ValorDecision: continue
           
            Cont = Cont +1
            if len(W) == 1:
              FactorPri=1.0
            else:
                FactorPri=W[Cont]
                
            ClaseLeida=float(lineadelTrain[0])
            if ClaseLeida==-1.0:
                Clase=0
            else:
                Clase=int(ClaseLeida)
                               
            ContClase[Clase]=ContClase[Clase] + 1
                       
            
            # Acumulacion valores
            z=-1
            for x  in lineadelTrain:
                
                z=z+1
                if z==NumCampos:
                    break
              
                if z==0: continue
                   
                ValorTrain =float(lineadelTrain[z])
                ValorTrain =ValorTrain - Min[z]
                Maximo = Max[z]
                Maximo = Maximo - Min[z]
                indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
                if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                    print("index overflowed=" + str( indice) + " in  the field ="+ str(z-1) )
                
                Wvalor=0.0
             
                Wvalor= TabVotos[z,TopeMemoria-1,Clase]
                Wvalor= Wvalor + 1
                TabVotos[z,TopeMemoria-1,Clase]=Wvalor 
               
                Wvalor= TabVotos[z,indice,Clase]
                Wvalor=Wvalor+FactorPri
                TabVotos[z,indice,Clase]=Wvalor 
                # print("Acumula en el indice = " + str(indice) + " Clase =" + str(Clase) + " Wvalor =" + str(Wvalor))
       
        f.close()
        
        #print("Total Clase 0 = " + str(ContClase[0]) +" Total Clase 1 = " +str(ContClase[1]))
        
       # for Campo in range(NumCampos):
           
       
        ContaPanta=0
        HClase_PreguntaMin=999999999.0
        indiceMin=999999
        i=0
        for i in range (TopeMemoria-2):
            # ClaseMenos y ClaseMas computan computan las clases
            # que existen con valores del campo menos o mas del 
            # campo considerado
            
            ClasesMenos = np.zeros(NumClases)
            ClasesMas = np.zeros(NumClases)
            TotClaseMenos=0
            TotClaseMas=0
            EntroCampoMenos=0
            EntroCampoMas=0
            for y in range(i):
               
                for w in range (NumClases):
                    # print("Recupera indice = "+str(i) + "Clase= " + str(w) + "Valor = " +str(TabVotos[Campo,i,w]))
                    TotClaseMenos= TotClaseMenos + TabVotos[Campo,y,w]
                    ClasesMenos[w]=ClasesMenos[w]+ TabVotos[Campo,y,w]
            
            for j in range (NumClases):
                    if (ClasesMenos[j] != 0.0) :
                        P=ClasesMenos[j]/TotClaseMenos
                        # print("Indice =" + str(i) + " Clase= " + str(j) +  " Probabilidad Campo  "+  str(P) + "Total Clases = "+ str(TotClases))
                        EntroCampoMenos= EntroCampoMenos +  P*math.log(1.0/P,2)
            #print("Entropy < indiex =" +str(i) + " field "+  str(Campo)+ " = " + str(EntroCampoMenos) )
            for y in range(i,TopeMemoria-2):
               
                for w in range (NumClases):
                    # print("Recupera indice = "+str(i) + "Clase= " + str(w) + "Valor = " +str(TabVotos[Campo,i,w]))
                    TotClaseMas= TotClaseMas + TabVotos[Campo,y,w]
                    ClasesMas[w]=ClasesMas[w]+ TabVotos[Campo,y,w]
            
            for j in range (NumClases):
                    if (ClasesMas[j] != 0.0) :
                        P=ClasesMas[j]/TotClaseMas
                        # print("Indice =" + str(i) + " Clase= " + str(j) +  " Probabilidad Campo  "+  str(P) + "Total Clases = "+ str(TotClases))
                        EntroCampoMas= EntroCampoMas +  P*math.log(1.0/P,2)
            #print("Entropy > index=" +str(i) + " field "+  str(Campo)+ " = " + str(EntroCampoMas) )
            HClase_Pregunta =(TotClaseMenos/(TotClaseMenos+TotClaseMas) )*EntroCampoMenos +  (TotClaseMas/(TotClaseMenos+TotClaseMas) )*EntroCampoMas
            #print("HClass_Question index =" +str(i) + " field "+  str(Campo)+ " = " + str(HClase_Pregunta) )
            if (HClase_Pregunta < HClase_PreguntaMin):
                indiceMin=i
                HClase_PreguntaMin=HClase_Pregunta
            ContaPanta=ContaPanta + 1
            if ContaPanta > 1000:
                print("Procesa 1000")
                ContaPanta=0
        print("Index minimum =" +str(indiceMin) + " field "+  str(Campo)+ " Class Question " + str(HClase_PreguntaMin) )
        ClasesMenos = np.zeros(NumClases)
        ClasesMas = np.zeros(NumClases)
        TotClaseMenos=0
        TotClaseMas=0
        # ANTES for y in range(indiceMin+1,TopeMemoria-2): QUITAR + 1
        for y in range(indiceMin,TopeMemoria-2):
               
                for w in range (NumClases):
                   
                    TotClaseMas= TotClaseMas + TabVotos[Campo,y,w]
                    ClasesMas[w]=ClasesMas[w]+ TabVotos[Campo,y,w]
        for y in range(indiceMin):
                
                for w in range (NumClases):
                   
                    TotClaseMenos = TotClaseMenos + TabVotos[Campo,y,w]
                    ClasesMenos[w]=ClasesMenos[w]+ TabVotos[Campo,y,w] 
        print(" " )
        print("Index Classes Values = " + str(indiceMin))
        for w in range (NumClases):
                    print("Class = " + str(w) + " in branch > "+ str( ClasesMas[w]) + " in branch < "+ str( ClasesMenos[w]))
                                                                                            
############################################################################33
# MAIN
###########################################################################333

W=[float(1.0)]
Hastie_C4_5( W)

    