import random

def generuj(n):
    zoz1 = []
    for i in range (0,n):
        zoz1.append(random.randrange(5,11))
    return zoz1

def sucet_parne(z):
    zoz2 = z
    sucet = 0
    for i in zoz2:
        if i%2 == 0:
            sucet += i
    return sucet 



def coho_je_viac(z):
    zoz3 = z 
    p = 0
    n = 0
    for i in zoz3:
        if i%2 == 0:
            p += 1
        else:
            n += 1
    if p > n:
        return "parne"
    elif n > p:
        return "neparne"
    elif n == p:
        return "rovnako"
    

def parne_pozicie(z):
    zoz4 = z
    parne = []
    for i in range(len(zoz4)):
        if i%2 == 0:
            parne.append(zoz4[i])
    return parne

#def nie_cisla(z):
    #zoz5 = z
    #novy_zoz5 = []
    #for i in zoz5:
        #if not i.isdigit():
            #novy_zoz5.append[i]
    #return novy_zoz5




def spolu_do_retazca(z):
    zoz6 = z
    retaz = ''
    for i in zoz6:
        retaz += str(i)
    return retaz


def zoznam_mocnin(n):
    zoz7 = []
    for i in range(0,n+1):
        zoz7.append(pow(i,2))
    return zoz7


    

  

    




   
    


    