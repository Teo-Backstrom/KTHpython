# Teo Bäckström, Otto Bahrke, Tim


def aritmetisk_sum(start, diff, antal):
    """räknar ut den aritematiska summan

    Args:
        start (float): startvärde i den artiematiska summan
        diff (float): differansen i den aritematiska summan
        antal (int): antalet steg i den aritematiska summan

    Returns:
        float: aritematiska summan
    """
    #aritematiska summaformel
    resultat = (antal * (start + (start + (antal - 1) * diff)))/2
    return resultat


def geometrisk_sum(start, kvot, antal):
    """räknar ut geometrisk summa

    Args:
        start (float): startvärde i den geometriska summan
        kvot (float): kvoten i geometriska summman
        antal (int): atnal steg i den geometriska summan

    Returns:
        float: geometriska summan
    """
    #geometriskas summaformel
    resultat = start * (((kvot**antal) - 1) / (kvot - 1))
    return resultat
    


#ett inläsningverktyg där den felhanterar felinmating, kan ställa in vilken typ av värde på inmating, och välja en sträng som skrivs ut
def Readtype(typ = any, text = ""):
        
        #tar in värde från användare
        värde  = input(text)
        """
        försöker konvertera värdet till rätt typ och om den misslyckas så får användaren text feedback
        och programmet stängs ned
        """
        try:
            värde = typ(värde)
        except:
            print("Felaktigt värde. Försök igen.")
            print(f"Värdet är inte av typen {typ}")
            quit()
        return värde

print("Är den första summan [a]rtimetisk eller [g]eometrisk?")

val = input()
    
if (val.lower() == "a"):
    start = Readtype(float, "Skriv in startvärdet (a1):")
    diff = Readtype(float, "Skriv in differensen (d):")
elif (val.lower() == "g"):
    start = Readtype(float, "Skriv in startvärdet (g1):")
    kvot = Readtype(float, "Skriv in kvoten (q):")        
else:
    print("Inmatningen måste vara a eller g")
    quit()
        
print("Är den andra summan [a]rtimetisk eller [g]eometrisk?")

val_2 = input()
    
if (val_2.lower() == "a"):
    start_2 = Readtype(float, "Skriv in startvärdet (a1):")
    diff_2 = Readtype(float, "Skriv in differensen (d):")
elif (val_2.lower() == "g"):
    start_2 = Readtype(float, "Skriv in startvärdet (g1):")
    kvot_2 = Readtype(float, "Skriv in kvoten (q):")        
else:
    print("Inmatningen måste vara a eller g")
    quit()
antal = Readtype(int, "Hur många termer (n)?")
        
if (val.lower() == "a"):
    sum_1 = aritmetisk_sum(start, diff, antal)
else:
    sum_1 = geometrisk_sum(start, kvot, antal)

if (val_2.lower() == "a"):
    sum_2 = aritmetisk_sum(start_2, diff_2, antal)
else:
    sum_2 = geometrisk_sum(start_2, kvot_2, antal)
    
if (sum_1 == sum_2):
    print("Summorna är lika")
elif (sum_1 > sum_2):
    print("Den första summan är störst.")
else:
    print("Den andra summan är störst.")
    
    