#ett inläsningverktyg där den felhanterar felinmating, kan ställa in max och min nummer och undantag och vilken typ av värde på inmating, och välja ett sträng som skrivs ut
def readtype(maxInt = float("inf"), minInt = float("-inf"), typ = any, undantag = []  ,text = ""):
    # flagga för att säga till whileloopen om inmatningen är tillåten   
    flagga2 = True
    #kollar så talet är mellan min och max kravet
    while (flagga2):
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