from module1 import *
#Praktiline töö "Sõnastik"
text_est=Loe_failist("est.txt")
text_rus=Loe_failist("rus.txt")
while True:
    print("1 - eesti keelest vene keelde ja vene keelest eesti keelde")
    print("2 - kui otsisõna sõnaraamatust puudub, andke kasutajale võimalus see sõnaraamatusse lisada")
    print("3 - kui kasutaja leiab sõnastikust vea, peab tal olema võimalus seda parandada")
    print("4 - kasutaja soovi korral kontrollida sõnaraamatu sõnade tundmist, rakendage seda võimalust ")
    v=int(input("Выберите действие: "))
    if v==1:
       text_es = input("Введите слово на эстонском языке: ")
       text_ru = est_to_rus(text_es, text_est, text_rus)
       if text_ru:
           print("В переводе на русский это", text_ru)
       else:
            print("Ошибка")
    elif v==2:
        text_ru=input("Введите слово на русском языке: ")
        text_es=rus_to_est(text_ru, text_est, text_rus)
        if text_es:
            print("В переводе на эстонский это", text_es)
        else:
             print("Ошибка")

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
