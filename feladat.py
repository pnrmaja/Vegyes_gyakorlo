
import random

def feladat1():
    
    
    szam:int= int(input("Kérek egy páratlan számot"))
    while not szam %2==1:
        
        szam=int(input("Kérek egy páratlan számot"))

    print("Ez egy páratlan szám")
            
        

def feladat2():
    i:int= 0
    db:int=0

    while i<7:
        szam:int=random.randint(5,100)
        print(szam,end=" ")
        
        if szam %5==0:
            db+=1
        i+=1
    print(f"A számok között {db} db 5-el osztható van")


def feladat3(text:str,betu:str):
    hossz:int=len(text)
    db:int=0
    i:int=0

    while i<hossz:
        if betu == text[i]:
            db+=1
        i+=1
    print(f"A szövegben {db} db '{betu}' betű van")

def feladat4():

    nev:str=input("Kérek egy nevet")
    db:int=0
    i:str="@"

    while nev != i:
        nev=input("Kérek egy nevet")
        db+=1
        if nev == i:
            print(f"A felhasználó {db} nevet adott meg.")

def feladat5():
    felhasznalo_tipjje:str=input("Kérek egy tippet: 1-Kő/2-papír/3-olló").lower()
    while felhasznalo_tipjje != "kő" and felhasznalo_tipjje != "papír" and felhasznalo_tipjje != "olló":
        felhasznalo_tipjje:str=input("Kérek egy tippet: 1-Kő/2-papír/3-olló").lower()

    
    gep_tippje:int=random.randint(1,3)

    if gep_tippje ==1:
        gep_tippje ="kő"
    elif gep_tippje ==2:
        gep_tippje="papír"
    else:
        gep_tippje="olló"

    print(felhasznalo_tipjje)
    print(gep_tippje)
    

    if felhasznalo_tipjje==gep_tippje:
        print("Döntetlen")
    elif felhasznalo_tipjje=="kő" and gep_tippje=="papír":
        print("Gép nyert!")
    elif felhasznalo_tipjje=="papír" and gep_tippje=="olló":
        print("Gép nyert!")
    elif felhasznalo_tipjje=="olló" and gep_tippje=="kő":
        print("Gép nyert!")
    elif felhasznalo_tipjje=="kő" and gep_tippje=="olló":
        print("Felhasználó nyert!")
    elif felhasznalo_tipjje=="papír" and gep_tippje=="kő":
        print("Felhasználó nyert!")
    else :
        print("Felhasználó nyert!")
    





        
