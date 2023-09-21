#importerar filen felhantering
import felhantering

#funktion för att räkna ut den aritematiska summan
def aritmetisk_sum(start, diff, antal):
    """funktion som räknar ut och retunerar den aritemetiska summan
        med den aritemetiska summaformeln

    Args:
        start (float): startväde av aritmetisk talförjden
        diff (float): differansen i aritemetisk talföljden
        antal (int): antal element i aritemetisk talföljden

    Returns:
        float: summa av aritemetisk talföljd
    """
    #aritematiska summaformel
    resultat = (antal * (start + (start + (antal - 1) * diff)))/2
    return resultat


#funktion för att räkna ut den geometriska summan
def geometrisk_sum(start, kvot, antal):
    """funktion som räknar ut och retunerar den geometriska summan
        med den aritemetiska summaformeln

    Args:
        start (float): startvärde av geometrisk talföljden
        kvot (float): kvoten av geometrisk talföljden
        antal (int): antal element i geometrisk talföljden

    Returns:
        float: summa av geometrisk talföljd
    """
    #geometriskas summaformel
    resultat = start * (((kvot**antal) - 1) / (kvot - 1))
    return resultat


def störst(första, andra):
    """tar in 2 värden och kollar vilken som är stört eller om de är lika stora
        och skriver ut resultatet
        
    Args:
        första (float): första värdet
        andra (float): andra värdet
    """
    
    if (första == andra):
        print("Summorna är lika")
    elif (första > andra):
        print("Den första summan är störst.")
    else:
        print("Den andra summan är störst.")
        

def main():
    """
    Programmet där användaren får flervalsfrågor och får mata in sitt svar
    Först en huvudmeny där använaderen får välja vad den vill göra
    Sedan får den mata in värderna i kalkylatorn
    Programmet kallar på rätt funktion och skriver ut vilken summa som är störst eller om de är lika stora
    Användaren får slutligen fråga om den vill göra en ny beräkning eller avsluta
    """
    #flagga för att kolla om användare vill avsluta programmet
    flagga = True
    while (flagga):
        #räknare som håller koll på hur många summor användaren räknat ut
        räknare = 0
        #Lista som sparar inmatningsvärderna för summorna
        värden = []
        #Lista som sparar menyval från användaren
        menyval = []
        #loopar tills användaren räknat ut 2 summor
        while (räknare < 2):
            #skriver ut menyn
            print(f"\nval {räknare + 1}")
            print("För artmatisk summa tryck 1")
            print("För geometrisk summa tryck 2")
            print("För att avsluta tryck 3")
            #tar emot menyval och sparar i lista 
            menyval.append(felhantering.inläsning(3, 1, int))

            #kollar vilket val som gjorts
            if (menyval[räknare] == 1):
                #frågar och tar emot värden för aritemetisk summa
                värden.append(felhantering.inläsning(typ = float, text = "Skriv in startvärdet (a1): "))
                värden.append(felhantering.inläsning(typ = float, text = "Skriv in differensen (d): "))
            elif (menyval[räknare] == 2):
                #frågar och tar emot värden för geometrisk summa
                värden.append(felhantering.inläsning(typ = float, text = "Skriv in startvärdet (g1): "))
                värden.append(felhantering.inläsning(typ = float, undantag = [1], text= "Skriv in kvoten (q): "))
            elif (menyval[räknare] == 3):
                print("Hej dåå")
                quit() #stoppar programmet
            else:
                print("Något gick snett")
            
            #tickar upp räknaren     
            räknare += 1
            
        #frågar om antalet värden i talförjderna och sparar i listan    
        värden.append(felhantering.inläsning(minInt= 1, typ = int, text= "Skriv in antal element i följden (n): "))
        
        #kollar vilket menyval som gjorts och räknar ut rätt summa 1
        if (menyval[0] == 1):
            sum_1 = aritmetisk_sum(värden[0], värden[1], värden[4])
        else:
            sum_1 = geometrisk_sum(värden[0], värden[1], värden[4])
            
        #kollar vilket menyval som gjorts och räknar ut rätt summa 2    
        if (menyval[1] == 1):
            sum_2 = aritmetisk_sum(värden[2], värden[3], värden[4])
        else:
            sum_2 = geometrisk_sum(värden[2], värden[3], värden[4])

        #kallar på funktionen som skriver ut vilken summa som är störst eller lika
        störst(sum_1, sum_2)

        #frågar om användaren vill fortsätta och tar emot valet
        print("vill du fortsätta tryck 1")
        print("vill du avsluta tryck 2")
        val = felhantering.inläsning(2, 1, int)
        #om val = 2 så avslutas loopen/programmet
        if (val == 2):
            print("Hej dåå")
            flagga = False

#Kallar på main-funtionen
main()
    