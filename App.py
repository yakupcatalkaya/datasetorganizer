#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:04:02 2019

@author: mrjacob
"""

from Person import *
from datetime import datetime



studentlist=[]
people=[]


file=open("student1.txt","r")
for line in file:
    student=line.split('"')[:-1]
    for indexpart in range(len(student)):
        if student[indexpart]=="" or student[indexpart]==" ":
            student=student[:indexpart]+["UNKNOWN"]+student[indexpart+1:]
    studentlist.append(student)   
count=0    
for a in range(len(studentlist)-2):
    if len(studentlist[a])>1:
        sid=studentlist[a][1]
        no=studentlist[a][3]
        TC=studentlist[a][5]
        isim=studentlist[a][7]
        soyisim=studentlist[a][9]
        mail=studentlist[a][11]
        mailTwo=studentlist[a][13]
        sinif=studentlist[a][15]
        sube=studentlist[a][17]
        danisman=studentlist[a][19]
        danismanTwo=studentlist[a][21]
        ingsube=studentlist[a][23]
        Twoyabdil=studentlist[a][25]
        Twoydsube=studentlist[a][27]
        alan=studentlist[a][29]
        ogrencisms=studentlist[a][31]
        velisms=studentlist[a][33]
        velismsTwo=studentlist[a][35]
        okul=studentlist[a][37]
        rol=studentlist[a][39]
        dogum=studentlist[a][41]
        cinsiyet=studentlist[a][43]
        veliTC=studentlist[a][45]
        anneAdi=studentlist[a][47]
        anneTC=studentlist[a][49]
        babaadi=studentlist[a][51]
        babaTC=studentlist[a][53]
        prol=studentlist[a][55]
        kardes=studentlist[a][57]
        donem=studentlist[a][59]
        kayit=studentlist[a][61]
        kayitTar=studentlist[a][63]
        kampus=studentlist[a][65]
        birim=studentlist[a][67]
        yenikampus=studentlist[a][69]
        yenibirim=studentlist[a][71]
        eokul=studentlist[a][73]
        servisS=studentlist[a][75]
        servisA=studentlist[a][77]
        servisC=studentlist[a][77]
        adres=studentlist[a][-1]      
        man=Person(sid,no,TC,isim,soyisim,mail,mailTwo,sinif,sube,danisman,danismanTwo,ingsube,Twoyabdil,Twoydsube,alan,ogrencisms,velisms,velismsTwo,okul,rol,dogum,cinsiyet,veliTC,anneAdi,anneTC,babaadi,babaTC,prol,kardes,donem,kayit,kayitTar,kampus,birim,yenikampus,yenibirim,eokul,servisS,servisA,servisC,adres)
        people.append(man)
        count+=1
    
    
   

print("            _______________________________________________________________________")
print("            |                                                                     |")
print("            |                                                                     |")
print("            |                                                                     |")
print("            |       ",count,"student's information added succesfully.","               |")
print("            |                                                                     |")
print("            |                                                                     |")
print("            |                                                                     |")
print("            |_____________________________________________________________________|\n\n")

                                            
#print(count,"people added succesfully.")




while True:
    print("\n\n\n______________________________________DATABASE SCRIPT_______________________________________")
    print("                                                                       | CREATED BY MRJACOB |")

    print("1.PRINT A STUDENT'S INFORMATION \n")
    print("2.IDENTIFY THE AGE OF A STUDENT \n")
    print("3.PRINT STUDENTS WHO BIRTH TODAY \n")
    print("4.PRINT STUDENTS WHO BIRTH IN A SPECIFIED DAY \n")
    print("5.PRINT SIBLINGS \n")
    girdi=int(input("(ENTER 6 TO FINALIZED THE SCRIPT.) CHOOSE ONE: "))
    print("\n\n__________________________________________________________\n\n")
    
    if girdi==1:
        lista=Person.createlist()
        Name=input("Enter a name(UPPER): ")
        Surname=input("Enter a surname(UPPER): ")
        print("\n\n")
        for person in people:
            person.finder(Name,Surname,lista)
        for person in lista:
            print(person.__repr__())
        continue
    if girdi==2:
        lista=Person.createlist()
        Name=input("Enter a name(UPPER): ")
        Surname=input("Enter a surname(UPPER): ")
        print("\n\n")
        for person in people:
            person.finder(Name,Surname,lista)
        for person in lista:
            print(person.howold())
        continue
    if girdi==3:
        lista=Person.createlist()
        for a in people:
            a.todayborn(a,lista)
        for person in lista:
            print(person.getisim(),person.getsoyisim(),person.getdogum())
        print("__________________________________________________________\n\n")
        continue
    if girdi==4:
        aDay=input("Enter a day in the format of MM.DD :  ")
        print("\n\n")
        lista=Person.createlist()
        for a in people:
            a.aDayborn(a,lista,aDay)
        for person in lista:
            print(person.getisim(),person.getsoyisim(),person.getdogum())
        print("__________________________________________________________\n\n")
        continue
    if girdi==5:
        lista=Person.createlist()
        listb=Person.createlist()
        for person in people:
            for per in people:
                person.findsibling(lista,listb,per)
        for c in range(len(lista)):
            print(lista[c].getisim(),lista[c].getsoyisim()," and ",listb[c].getisim(),lista[c].getsoyisim()," are siblings.")                
    if girdi==6:
        break
    else:
        break
    
    

    
    
    
    
    
    
    
    
    