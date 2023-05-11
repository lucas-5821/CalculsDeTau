import numpy as np
import lib as lib


def tau_1_channel(h,filename):
    
    T,V = lib.readPicoCSV(filename)

    t1 = (10**(-6)) * T[0]      #secondes
    t2 = (10**(-6)) * T[h]      #secondes
    V1 = V[0]                   #Volts
    V2 = V[h]                   #Volts
    print(t1,t2,V1,V2)
  
    return ((t2-t1) / np.log(V1/V2))


def tau_sans_métal(filename):
    
    T,VA,VB = lib.readPicoCSV(filename)
    T += 25.3
    t1 = (10**(-6)) * T[270]      #secondes
    t2 = (10**(-6)) * T[400]      #secondes
    V1 = VA[270]                  #Volts
    V2 = VA[400]                  #Volts
    return ((t2-t1) / np.log(V1/V2))

def tau_avec_métal(filename):
    
    T,VA,VB = lib.readPicoCSV(filename)
    T += 25.3
    t1 = (10**(-6)) * T[245]      #secondes
    t2 = (10**(-6)) * T[408]      #secondes
    V1 = VA[245]                  #Volts
    V2 = VA[408]                  #Volts
    
    return ((t2-t1) / np.log(V1/V2))


def main():
    
    filename_1 = "bloc 2//circuit final (bloc 2 sans métal) R = 330//circuit final (bloc 2 sans métal_01.csv"
    R = 330                    #Ohm
    tau_1 = tau_sans_métal(filename_1)           #Henri/Ohm
    L_1 = tau_1*R            #Henri
    
    filename_2 = "bloc 2//circuit final (bloc 2 avec métal) R = 330//circuit final (bloc 2 avec métal)_01.csv"
    tau_2 = tau_avec_métal(filename_2)
    L_2 = tau_2*R
    
    print('Sans métal : \ttau = ',tau_1,"\tL = ",L_1,"\nAvec métal : \ttau = ",tau_2,"\tL = ",L_2)
    
    return tau_1,tau_2

main()
        