#flagga för att kolla om användare vill avsluta programmet
flagga = True

#funktion för att räkna ut den aritematiska summan
def aritmetisk_sum(start, diff, antal):
    #aritematiska summaformel
    resultat = (antal * (start + (start + (antal - 1) * diff)))/2
    return resultat
   # print(f"Den aritmetiska summa är: {resultat}")


#funktion för att räkna ut den geometriska summan
def geometrisk_sum(start, kvot, antal):
    #geometriskas summaformel
    resultat = start * (((kvot**antal) - 1) / (kvot - 1))
    return resultat
    #
    # print(f"Den geometriska summa är: {resultat}")


#ett inläsningverktyg där den felhanterar felinmating, kan ställa in max och min nummer och undantag och vilken typ av värde på inmating, och välja ett sträng som skrivs ut
def Readtype(maxInt = float("inf"), minInt = float("-inf"), typ = any, undantag = []  ,text = ""):
    # flagga för att säga till whileloopen om inmatningen är tillåten   
    falgga2 = True
    #kollar så talet är mellan min och max kravet
    while (falgga2):
        #tar in värdet av användaren och skriver ut text        
        värde  = input(text)
        """
        försöker konvertera värdet till rätt typ och om den misslyckas så får användaren mata in nytt värde och får text feedback
        om det är rätt typ så kollar ifsatsen om värdet stämmer överens med de överiga parametrarna
        """
        
        try:
            värde = typ(värde)
        except:
            print("Felaktigt värde. Försök igen.")
            print(f"Värdet är inte av typen {typ}")
        else:  
            #Kollar max och min väreden stämmer 
            if ((värde > maxInt or värde < minInt)): 
                print(f"Värdet måste ligga mellan {minInt - 1} och {maxInt + 1}")
            #kollar så värdet inte tillhör ett undantag
            elif (värde in undantag):
                print(f"Värdet får inte vara {undantag}")
            else:
                falgga2 = False
                return värde

"""
Programmet där användaren får flervalsfrågor och får mata in sitt svar
Först en huvudmeny där använaderen får välja vad den vill vad den vill göra
Sedan får den mata in värderna i kalkylatorn
Programmet kallar på rätt funktion och skriver ut svaret
Användaren får slutligen fråga om den vill göra en ny beräkning eller avsluta
"""
while (flagga):
    print("För artmatisk summa tryck 1")
    print("För geometrisk summa tryck 2")
    print("För att avsluta tryck 3") 
    val = Readtype(3, 1, int)
    
    if (val == 1):
        
        start = Readtype(typ= float, text= "Skriv in startvärdet (a1): ")
        diff = Readtype(typ= float, text= "Skriv in differensen (d): ")
        antal = Readtype(typ= float, text= "Skriv in antal element i följden (n): ")
        print(f"Den aritmetiska summa är: {aritmetisk_sum(start, diff, antal)}")
    elif (val == 2):
        start = Readtype(typ= float, text= "Skriv in startvärdet (g1): ")
        kvot = Readtype(typ = float, undantag = [1], text= "Skriv in kvoten (q): ")
        antal = Readtype(typ= float, text= "Skriv in antal element i följden (n): ")
        print(f"Den geometriska summa är: {geometrisk_sum(start, kvot, antal)}")
    elif (val == 3):
        print("Hej dåå")
        break #stoppar whileloopen
        
    else:
        print("Något gick snett")
    
    print("vill du fortsätta tryck 1")
    print("vill du avsluta tryck 2")
    val = Readtype(2, 1, int)
    if (val == 2):
        print("Hej dåå")
        flagga = False

    