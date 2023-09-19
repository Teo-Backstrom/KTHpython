
#ett inläsningverktyg där den felhanterar felinmating, kan ställa in max och min nummer och undantag och vilken typ av värde på inmating, och välja ett sträng som skrivs ut

def readtype(maxInt = float("inf"), minInt = float("-inf"), typ = any, undantag = []  ,text = ""):
    """_summary_

    Args:
        maxInt (float): värde för att sätta maxgräns till inmatingsvärde. Defaultar till float("inf").
        minInt (float): värde för att sätta mingräns till inmatingsvärde. Defaultar till float("-inf").
        typ (datatype): sätter vilken datatyp som accepteras till inmating. Defaultar till any.
        undantag (list): Lista för att sätt undantag som värdet inte får vara. Defaults to [].
        text (str): text sträng som skrivs ut när man kallar på funktionen. Defaults to "".

    Returns:
        värde (typ) : retunerar ett accepterat värde som användaren matat in
    """  
    
    # flagga för att säga till whileloopen om inmatningen är tillåten   
    flagga2 = True
    
    while (flagga2):
        
        #tar in värdet av användaren och skriver ut text        
        värde  = input(text)
        
        #försöker konvertera värdet till rätt typ och om den misslyckas så får användaren mata in nytt värde och får text feedback
        #om det är rätt typ så kollar ifsatsen om värdet stämmer överens med de överiga parametrarna
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
                flagga2 = False
                return värde