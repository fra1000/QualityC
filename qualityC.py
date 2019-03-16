#! /usr/bin/python
################################################################
#                   PROGRAMMA QUALITYC                         #
################################################################
#Programma per il controllo di qualità
#  
import matplotlib as plt
import datetime
import math
array=[]
tmeArray=[]
b=0
som=0
num=0

class qualityC (misura):
    def __init__(self,misura):
        #prendere come input due valori che sono l'ora attuale e la misura
        array.append(misura)
        #aggiungere l'ora attuale e la misura all'array di numeri
        tmeArray.append(datetime.datetime.now())
        #calcola la media con la funzione media
        self.media(array)
        #calcola la deviazione standard con la funzione deviazione standard
        self.devSt(array)
        #plot l'array in un grafico con in x l'ora e in y il valore inserito e i valori di media piu o meno 1,2,3deviazione standard
        self.qualityPlot(x,misura,dev)
        #se il tuo valore è in  
    
    #sommare i valori di un array
    def somma(self, a):
        sum=0
        for i in a:
            sum+=a[i-1]
        return sum
    
    #contare i valori array
    def conta(self, a):
        num=0
        for i in a:
            num+=1
        return num

    #media dell'array
    def media(self, x):
        self.somma(x)
        self.conta(x)
        media =som/num
        return media

    #array di scarti al quadrato
    def sScart(self,x):
        ss=0
        for i in x:
            sc=[]
            ss=(x[i-1]- self.media(x))*(x[i-1]- self.media(x))
            sc.append(ss)
        return sc

    #Deviazione standard
    def devSt(self, y):
        dev=0
        dev =math.sqrt(qualityC.somma(sc)/qualityC.conta(sc))
        return dev

    def lungass(x):
        if qualityC.conta(x) < 2:
            return 100
        else:
            lung= max(x)*1.1
            return lung
    
    def qualityPlot(self,x,y,dev):
        #plot il grafico dei valori inseriti
        plt.plot(x, y, 'ro')
        #plot la media più o meno una, due e tre deviazioni stndard
        linm=qualityC.media(y)
        linm1=qualityC.media(y)+qualityC.devSt(y)
        linm2=qualityC.media(y)+(2*qualityC.devSt(y))
        linm3=qualityC.media(y)+(3*qualityC.devSt(y))
        linm_3=qualityC.media(y)-(3*qualityC.devSt(y))
        linm_1=qualityC.media(y)-qualityC.devSt(y)
        linm_2=qualityC.media(y)-(2*qualityC.devSt(y))

        plt.plot(linm,0, ro)
        plt.plot(linm1,0, ro)
        plt.plot(linm2,0, ro)
        plt.plot(linm3,0, ro)
        plt.plot(linm_1,0, ro)
        plt.plot(linm_2,0, ro)
        plt.plot(linm_3,0, ro)
        #plot gli assi
        plt.axis([0, max(x), 0, 20])
        plt.show()
        #plt.plot([1,2,3,4], [1,4,9,16], 'ro')
        #plot(devSt)
        #plt.axis([0, 6, 0, 20])
        #plt.show()
     

VAL=input("SCRIVI IL VALORE MISURATO")
qualityC(VAL)
