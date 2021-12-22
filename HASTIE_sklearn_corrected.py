  
f=open("C:\Hastie10_2.csv","r")
with open("C:\Hastie10_2Corrected.txt","w") as  w:
    ContaMax=12000
    ContAciertos=0
    ContErrores=0
    Conta=0;
    for linea in f:
        Conta=Conta+1
        if Conta > ContaMax :break
        lineadelTrain =linea.split(";")
      
     
        linea_x =[""]
        z=0
        Suma=0.0
        for x in lineadelTrain:
            
                z=z+1
                if z==11: break
                if z==1: linea_x[0]=float(lineadelTrain[z])
                else:
                     linea_x.append(float(lineadelTrain[z]))
                     Suma=Suma+(float(lineadelTrain[z])**2)
        Y = 1.0 if Suma > 9.34 else -1.0
        lineadelTrain[0]=str(Y)
        separator=";"
        linea1=separator.join(lineadelTrain)
        strlinea1=str(linea1)
        if Y==float(lineadelTrain[0]):
             ContAciertos=ContAciertos+1
             #strlinea1=strlinea1+";"+ str(Y) + "\n"
             w.write(strlinea1)
        else:
            ContErrores=ContErrores +1
            #strlinea1=strlinea1+";"+ str(Y) + "\n"
            w.write(strlinea1)
    f.close()
    w.close()
    print (" Total hits TRAIN = " + str(ContAciertos))
    print (" Total failures TRAIN = " + str(ContErrores))
        
