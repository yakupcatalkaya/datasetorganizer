#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:38:22 2019

@author: mrjacob
"""

from datetime import datetime

class Person():
    def __init__ (self,sid,no,TC,isim,soyisim,mail,mailTwo,sinif,sube,danisman,danismanTwo,ingsube,Twoyabdil,Twoydsube,alan,ogrencisms,velisms,velismsTwo,okul,rol,dogum,cinsiyet,veliTC,anneAdi,anneTC,babaadi,babaTC,prol,kardes,donem,kayit,kayitTar,kampus,birim,yenikampus,yenibirim,eokul,servisS,servisA,servisC,adres):
        self.__sid=sid
        self.__no=no
        self.__TC=TC
        self.__isim=isim
        self.__soyisim=soyisim
        self.__mail=mail
        self.__mailTwo=mailTwo
        self.__sinif=sinif
        self.__sube=sube
        self.__danisman=danisman
        self.__danismanTwo=danismanTwo
        self.__ingsube=ingsube
        self.__Twoyabdil=Twoyabdil
        self.__Twoydsube=Twoydsube
        self.__alan=alan
        self.__ogrencisms=ogrencisms
        self.__velisms=velisms
        self.__velismsTwo=velismsTwo
        self.__okul=okul
        self.__rol=rol
        self.__dogum=dogum
        self.__cinsiyet=cinsiyet
        self.__veliTC=veliTC
        self.__anneAdi=anneAdi
        self.__anneTC=anneTC
        self.__babaadi=babaadi
        self.__babaTC=babaTC
        self.__prol=prol
        self.__kardes=kardes
        self.__donem=donem
        self.__kayit=kayit
        self.__kayitTar=kayitTar
        self.__kampus=kampus
        self.__birim=birim
        self.__yenikampus=yenikampus
        self.__yenibirim=yenibirim
        self.__eokul=eokul
        self.__servisS=servisS
        self.__servisA=servisA
        self.__servisC=servisC
        self.__adres=adres
 
##################################   GET    ###################################
    
    def getsid(self):
        return self.__sid
    def getno(self):
        return self.__no
    def getTC(self):
        return self.__TC
    def getisim(self):
        return self.__isim
    def getsoyisim(self):
        return self.__soyisim
    def getmail(self):
        return self.__mail
    def getmailTwo(self):
        return self.__mailTwo
    def getsinif(self):
        return self.__sinif
    def getsube(self):
        return self.__sube
    def getdanisman(self):
        return self.__danisman
    def getdanismanTwo(self):
        return self.__danismanTwo
    def getingsube(self):
        return self.__sube
    def getTwoyabdil(self):
        return self.__Twoyabdil
    def getTwoydsube(self):
        return self.__Twoydsube
    def getalan(self):
        return self.__alan
    def getogrencisms(self):
        return self.__ogrencisms
    def getvelisms(self):
        return self.__velisms
    def getvelismsTwo(self):
        return self.__velismsTwo
    def getokul(self):
        return self.__okul
    def getrol(self):
        return self.__rol
    def getdogum(self):
        return self.__dogum
    def getcinsiyet(self):
        return self.__cinsiyet
    def getveliTC(self):
        return self.__veliTC
    def getanneAdi(self):
        return self.__anneAdi
    def getanneTC(self):
        return self.__anneTC
    def getbabaadi(self):
        return self.__babaadi
    def getbabaTC(self):
        return self.__babaTC
    def getprol(self):
        return self.__prol
    def getkardes(self):
        return self.__kardes
    def getdonem(self):
        return self.__donem
    def getkayit(self):
        return self.__kayit
    def getkayitTar(self):
        return self.__kayitTar
    def getkampus(self):
        return self.__kampus
    def getbirim(self):
        return self.__birim
    def getyenikampus(self):
        return self.__yenikampus
    def getyenibirim(self):
        return self.__yenibirim
    def geteokul(self):
        return self.__eokul
    def getservisS(self):
        return self.__servisS
    def getservisA(self):
        return self.__servisA
    def getservisC(self):
        return self.__servisC
    def getadres(self):
        return self.__adres
    
    
#################################   SET   #####################################
        
    def setsid(self,new):
        self.__id=new
    def setno(self,new):
        self.__no=new
    def setTC(self,new):
        self.__TC=new
    def setisim(self,new):
        self.__isim=new
    def setsoyisim(self,new):
        self.__soyisim=new
    def setmail(self,new):
        self.__mail=new
    def setmailTwo(self,new):
        self.__mailTwo=new
    def setsinif(self,new):
        self.__sinif=new
    def setsube(self,new):
        self.__sube=new
    def setdanisman(self,new):
        self.__danisman=new
    def setdanismanTwo(self,new):
        self.__danismanTwo=new
    def setingsube(self,new):
        self.__ingsube=new
    def setTwoyabdil(self,new):
        self.__Twoyabdil=new
    def setTwoydsube(self,new):
        self.__Twoydsube=new
    def setalan(self,new):
        self.__alan=new
    def setogrencisms(self,new):
        self.__ogrencisms=new
    def setvelisms(self,new):
        self.__velisms=new
    def setvelismsTwo(self,new):
        self.__velismsTwo=new
    def setokul(self,new):
        self.__okul=new
    def setrol(self,new):
        self.__rol=new
    def setdogum(self,new):
        self.__dogum=new
    def setcinsiyet(self,new):
        self.__cinsiyet=new
    def setveliTC(self,new):
        self.__veliTC=new
    def setanneAdi(self,new):
        self.__anneAdi=new
    def setanneTC(self,new):
        self.__anneTC=new
    def setbabaadi(self,new):
        self.__babaadi=new
    def setbabaTC(self,new):
        self.__babaTC=new
    def setprol(self,new):
        self.__prol=new
    def setkardes(self,new):
        self.__kardes=new
    def setdonem(self,new):
        self.__donem=new
    def setkayit(self,new):
        self.__kayit=new
    def setkayitTar(self,new):
        self.__kayitTar=new
    def setkampus(self,new):
        self.__kampus=new
    def setbirim(self,new):
        self.__birim=new
    def setyenikampus(self,new):
        self.__yenikampus=new
    def setyenibirim(self,new):
        self.__yenibirim=new
    def seteokul(self,new):
        self.__eokul=new
    def setservisS(self,new):
        self.__servisS=new
    def setservisA(self,new):
        self.__servisA=new
    def setservisC(self,new):
        self.__servisC=new
    def setadres(self,new):
        self.__adres=new

################################    ADDITIONAL    #############################        
    def finder(self,Name,Surname,newlist):
        if Name.upper().strip() in self.getisim().upper().strip():
            if Surname.lower().strip() in self.getsoyisim().lower().strip():
                newlist.append(self)      
    def howold(self):
        gun=self.getdogum().split(".")
        if len(gun)>2 and gun[1]!="00":
            if gun[1][0]=="0":
                gun[1]==gun[1][1:]
            year,month,day=gun[0],gun[1],gun[2]
            bugün = datetime.today()
            dogumgünü = datetime(int(year),int(month),int(day))
            fark = bugün-dogumgünü
            aYear=fark.days//365.25
            aDay=fark.days-aYear*365
            aMonth=aDay//30.4375
            aDay=aDay-aMonth*30
            return self.__isim+" "+self.__soyisim+" was born "+str(int(aYear))+" years and "+str(int(aMonth))+" months and "+str(int(aDay))+" days ago."
        return "UNKNOWN"
    def createlist():
        lista=[]
        return lista 
    def todayborn(self,person,bornlist):
        gun=self.getdogum().split(".")
        if len(gun)>2 and gun[1]!="00":
            if gun[1][0]=="0":
                gun[1]==gun[1][1:]
            year,month,day=gun[0],gun[1],gun[2]
            bugün = datetime.today()
            dogumgünü = datetime(int(year),int(month),int(day))
            if bugün.month==dogumgünü.month and bugün.day==dogumgünü.day:
                bornlist.append(person)
    def aDayborn(self,person,bornlist,aDay):
        gun=self.getdogum().split(".")
        if len(gun)>2 and gun[1]!="00":
            if gun[1][0]=="0":
                gun[1]==gun[1][1:]
            year,month,day=gun[0],gun[1],gun[2]
            dogumgünü = datetime(int(year),int(month),int(day))
#            bugün = datetime.today()
            aDay=aDay.split(".")
            if len(aDay)>1 and aDay[1]!="00":
                Amonth,Aday=aDay[0],aDay[1]
                specifiedDay= datetime(1970,int(Amonth),int(Aday))
            if specifiedDay.month==dogumgünü.month and specifiedDay.day==dogumgünü.day:
                bornlist.append(person) 
    def siblingnum(self):
        count=0
        if self.__kardes!="UNKNOWN":
            count+=len(self.__kardes.split(","))
        return count
    
    def findsibling(self,lista,listb,per):
        if self.__TC!=per.__TC and self.__TC==per.__kardes:
            lista.append(per)
            listb.append(self)
    
#############################   REPR  ######################################### 
    def __repr__(self):
        out="________________STUDENT INFORMATION________________\n"
#        if not "UNKNOWN"==self.__sid :  
        out+="SID:                 "+self.__sid+"\n"
#        if not "UNKNOWN"== self.__no:            
        out+="NO:                  "+self.__no+"\n"
#        if not "UNKNOWN"== self.__TC:            
        out+="TC:                  "+self.__TC+"\n"
#        if not "UNKNOWN"== self.__isim:            
        out+="İSİM:                "+self.__isim+"\n"
#        if not "UNKNOWN"== self.__soyisim:            
        out+="SOYİSİM:             "+self.__soyisim+"\n"
#        if not "UNKNOWN"==self.__mail :            
        out+="MAİL:                "+self.__mail+"\n"
#        if not "UNKNOWN"== self.__mailTwo:            
        out+="2.MAİL:              "+self.__mailTwo+"\n"
#        if not "UNKNOWN"==self.__sinif :            
        out+="SINIF:               "+self.__sinif+"\n"
#        if not "UNKNOWN"==self.__sube :            
        out+="SUBE:                "+self.__sube+"\n"
#        if not "UNKNOWN"==self.__danisman :            
        out+="DANIŞMAN:            "+self.__danisman+"\n"
#        if not "UNKNOWN"== self.__danismanTwo:            
        out+="2.DANISMAN:          "+self.__danismanTwo+"\n"
#        if not "UNKNOWN"== self.__ingsube :            
        out+="İNGİLİZCE SUBE:      "+self.__ingsube+"\n"
#        if not "UNKNOWN"== self.__Twoyabdil:            
        out+="2. YABANCI DİL:      "+self.__Twoyabdil+"\n"
#        if not "UNKNOWN"== self.__Twoydsube:            
        out+="2.YABANCI DİL ŞUBE:  "+self.__Twoydsube+"\n"
#        if not "UNKNOWN"== self.__alan:            
        out+="ALAN:                "+self.__alan+"\n"
#        if not "UNKNOWN"== self.__ogrencisms:            
        out+="ÖĞRENCİ TELEFON:     "+self.__ogrencisms+"\n"
#        if not "UNKNOWN"== self.__velisms:            
        out+="VELİ TELEFON:        "+self.__velisms+"\n"
#        if not "UNKNOWN"== self.__velismsTwo:           
        out+="2.VELİ TELEFON:      "+self.__velismsTwo+"\n"      
#        if not "UNKNOWN"== self.__okul:           
        out+="GELDİĞİ OKUL:        "+self.__okul+"\n"
#        if not "UNKNOWN"== self.__rol:           
        out+="ROLU:                "+self.__rol+"\n"
#        if not "UNKNOWN"== self.__dogum:           
        out+="DOĞUM TARİHİ:        "+self.__dogum+"\n"
#        if not "UNKNOWN"== self.__cinsiyet:           
        out+="CİNSİYET:            "+self.__cinsiyet+"\n"
#        if not "UNKNOWN"== self.__veliTC:           
        out+="VELİ TC:             "+self.__veliTC+"\n"
#        if not "UNKNOWN"==self.__anneAdi :           
        out+="ANNE ADI:            "+self.__anneAdi+"\n"
#        if not "UNKNOWN"==self.__anneTC :           
        out+="ANNE TC:             "+self.__anneTC+"\n"
#        if not "UNKNOWN"== self.__babaadi:           
        out+="BABA ADI:            "+self.__babaadi+"\n"
#        if not "UNKNOWN"==self.__babaTC :           
        out+="BABA TC:             "+self.__babaTC+"\n"
#        if not "UNKNOWN"== self.__prol:           
        out+="PROL:                "+self.__prol+"\n"
#        if not "UNKNOWN"==self.__kardes :           
        out+="KARDEŞ TC:           "+self.__kardes+"\n"
#        if not "UNKNOWN"== self.__donem:           
        out+="DÖNEM:               "+self.__donem+"\n"
#        if not "UNKNOWN"== self.__kayit:           
        out+="KAYIT:               "+self.__kayit+"\n"
#        if not "UNKNOWN"== self.__kayitTar:           
        out+="KAYIT TARİHİ:        "+self.__kayitTar+"\n"
#        if not "UNKNOWN"== self.__kampus:          
        out+="KAMPÜS:              "+self.__kampus+"\n"
#        if not "UNKNOWN"== self.__birim:          
        out+="BİRİM:               "+self.__birim+"\n"
#        if not "UNKNOWN"== self.__yenikampus:          
        out+="YENİ KAMPÜS:         "+self.__yenikampus+"\n"
#        if not "UNKNOWN"== self.__yenibirim:          
        out+="YENİ BİRİM:          "+self.__yenibirim+"\n"
#        if not "UNKNOWN"== self.__eokul:          
        out+="E-OKUL:              "+self.__eokul+"\n"
#        if not "UNKNOWN"== self.__servisS:          
        out+="SABAH SERVİS:        "+self.__servisS+"\n"
#        if not "UNKNOWN"==self.__servisA :          
        out+="AKŞAM SERVİSİ:       "+self.__servisA+"\n"
#       if not "UNKNOWN"== self.__servisC:          
        out+="CUMARTESİ SERVİSİ:   "+self.__servisC+"\n"
#        if not "UNKNOWN"== self.__adres:          
        out+="EV ADRESİ:           "+self.__adres+"\n"
            
        return out
