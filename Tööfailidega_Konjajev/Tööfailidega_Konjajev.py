



from module1 import *
#Praktiline töö "Sõnastik"
text_est=Loe_failist("est.txt")
text_rus=Loe_failist("rus.txt")
while True:
     print("1-Tõlge eesti keelest vene keelde")
     print("2-Tõlge vene keelest eesti keelde")
     print("3-Lisa sõnastikku")
     print("4-Te võite sõnavea parandada")
     print("5-Sõnade tundmise kontrollimine")
     print("6-Välja")
     v=int(input("Выберите действие: "))
     if v==1:
         text_es = input("Kirjuta eestis: ")
         text_ru = est_to_rus(text_es, text_est, text_rus)
         if text_ru:
            print("Vene keles see on", text_ru)
     elif v==2:
         text_ru=input("Kirjuta vene keeles: ")
         text_es=rus_to_est(text_ru, text_est, text_rus)
         if text_es:
             print("Eesti keeles see on", text_es)
     elif v==3:
         text=input("Kirjuta sõna eestis: ")
         text_add(text, text_est, text_rus)
         laused=Loe_failist("est.txt")
         for line in laused:
             print(line) 
         laused=Loe_failist("rus.txt")
         for line in laused:
             print(line)
     elif v==4:
        correct_word(text, text_est, text_rus)               
        laused=loe_failist("est.txt")
        for line in laused:
            print(line)    
     elif v==5:
         hinne=Teadmiste_kontroll(text_est,text_rus,valik)
     elif v=="6":
         break
#Работа в классе
laused=[]
while True:
    v=int(input("1-Loeme failist\n2-Salvestame failisse\n3-Tekst helisse\n"))
    if v==1:
        laused=Loe_failist("Laused.txt")
        for line in laused:
            print(line)
    elif v==2:
        line=input("Lisa lause: ")
        laused.append(line)
        Kirjuta_failisse("Laused.txt",laused)
    elif v==3:
            text=""
            for line in laused:
                text=text+" "+line
            #text : kõik elemendis järjendis
            ind=int(input("Number:"))
            Heli(laused[ind],'et')
