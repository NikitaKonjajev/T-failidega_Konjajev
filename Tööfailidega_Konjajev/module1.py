def summa(a,b):
    pass
print(summa(4,2))


#Praktiline töö "Sõnastik"
#перевод с эстонского на русский:
def est_to_rus(text:str, text_est:list, text_rus:list):
    if text in text_est:
        ind=text_est.index(text)
    return text_rus[ind]

def rus_to_est(text:str, text_est:list,  text_rus:list ):
    if text in text_rus:
        ind=text_rus.index(text)
    return text_est[ind]

def kirjuta_failist(fail:str,jarjend:list):
    f=open(fail,"w",encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close

def text_add(text:str, text_est:list, text_rus:list):
    if text not in  text_est:
        text_est.append(text)
    a=input("Vene keeles on: ")
    text_rus.append(a)
    kirjuta_failist('est.txt', text_est)
    kirjuta_failist('rus.txt', text_rus)
    return  a

def loe_failist(fail:str)->list:
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def correct_word(text, text_est,text_rus):
    if text in text_rus:
       index = text_rus.index(text)
       text = input("Kirjuta sõna mida te tahate parandada: ")
       new_translation = input(f"Kirjuta uus sõna '{text}': ")
       text_est[index] = new_translation
       print("Sõna on parandatud")

def Teadmiste_kontroll(text_est,text_rus,valik):
    p=0
    kokku=int(input("Mitu küsimust?"))
    for i in range(kokku):
        järjend=valik([text_rus,text_est])
        sõna=valik(järjend) 
        print(f"{sõna} -", end="") 
        tõlke=input 
        if sõna in text_rus:
            i=text_rus.index(sõna)
            tõlke_kontroll=text_est[i] 
        elif sõna in text_rus:
            i=text_est.index(sõna)
            tõlke_kontroll=text_rus[i] 
        if tõlke==tõlke_kontroll:
            p+=1
            print("Õige")
        else:
            print("vale")
    if (p/kokku)*100>90:
        hinne=5 
    elif (p/kokku)*100>75:
        hinne=4
    elif (p/kokku)*100>60:
        hinne=3
    else: 
        hinne="Väga halb!"
    return hinne



 
#Работа в классе
def Loe_failist(fail:str)->list:
    """
    """
    f=open(fail,"r",encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,"w",encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()

from gtts import gTTS
import os
def Heli(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
