"""P-uppgift, Henrik Karlsson, CMAST1, DD1310"""

def jämnt_tal(storlek):
    """
    Konrtollerar ifall storlek är ett jämnt tal, returnerar då True, annars False
    Variabler:
        storlek : str
   """
    while True:
        try:
            storlek = int(storlek)
            if int(storlek) % 2 == 0 and int(storlek) >= 2 and int(storlek) <= 10:
                return True
            else:
                return False
        except ValueError:
            return False
        

