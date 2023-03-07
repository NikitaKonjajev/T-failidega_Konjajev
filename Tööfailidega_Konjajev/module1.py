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
