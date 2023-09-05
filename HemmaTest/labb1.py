flagga = True


def aritmetisk_sum(start, diff, antal):
    
    resultat = (antal * (start + (start + (antal - 1) * diff)))/2
    return resultat
   # print(f"Den aritmetiska summa är: {resultat}")



def geometrisk_sum(start, kvot, antal):
    resultat = start * (((kvot**antal) - 1) / (kvot - 1))
    return resultat
    #
    # print(f"Den geometriska summa är: {resultat}")



def Readtype(maxInt = float("inf"), minInt = float("-inf"), type = any, text = ""):
        
    falgga2 = True
    #kollar så talet är mellan min och max kravet
    while (falgga2):
                
        värde  = input(text)
        try:
            värde = type(värde)
        except:
            print("Felaktigt värde. Försök igen.")
            print(f"Värdet är inte av typen {type}")
        else:  
            if ((värde > maxInt or värde < minInt)): 
                print(f"Värdet måste ligga mellan {minInt - 1} och {maxInt + 1}")
            else:
                falgga2 = False
                return värde


while (flagga):
    print("För artmatisk summa tryck 1")
    print("För geometrisk summa tryck 2")
    print("För att avsluta tryck 3") 
    val = Readtype(3, 1, int)
    
    if (val == 1):
        
        start = Readtype(type= float, text= "Skriv in startvärdet (a1): ")
        diff = Readtype(type= float, text= "Skriv in differensen (d): ")
        antal = Readtype(type= int, text= "Skriv in antal element i följden (n): ")
        print(f"Den aritmetiska summa är: {aritmetisk_sum(start, diff, antal)}")
    elif (val == 2):
        start = Readtype(type= float, text= "Skriv in startvärdet (g1): ")
        kvot = Readtype(type= float, text= "Skriv in kvoten (q): ")
        antal = Readtype(type= float, text= "Skriv in antal element i följden (n): ")
        print(f"Den geometriska summa är: {geometrisk_sum(start, kvot, antal)}")
    elif (val == 3):
        print("Hej dåå")
        flagga = False
    else:
        print("Något gick snett")
    
    print("vill du fortsätta tryck 1")
    print("vill du avsluta tryck 2")
    val = Readtype(2, 1, int)
    if (val == 2):
        print("Hej dåå")
        flagga = False

    