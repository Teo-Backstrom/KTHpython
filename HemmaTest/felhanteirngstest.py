def inthantring(text=""):
    
    
    while True:
        värde = input(text)
        try:
            värde = int(värde)
            return värde
            
        except:
            print("Fel")
    
    
print(inthantring())
