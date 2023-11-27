"""P-uppgift, Henrik Karlsson,CMAST1, DD1310"""

import tkinter as tk
import felhantering_gui
import random

class Memory:
    """
    Klass för att skapa tom spelplan, importera alla ord från en fil, skapa facit och bestämma längden på längsta ord i facit

    Attributer:
        self.storlek : int
        self.spelplan : list
        self.facit : list
        self.ordlista : list
        self.maxlängd_ord : int
    Metoder:
        __init__()
        tom_spelplan()
        skapa_ordlista()
        skapa_facit()
        längsta_ord()
    """
    def __init__(self, storlek):
        """ 
        Argument:
            storlek : int 
        """
        #Attributer
        self.storlek = storlek
        self.spelplan = []
        self.facit = []
        self.ordlista = []
        self.maxlängd_ord = 0
        
        #Kör metoder
        self.tom_spelplan()
        self.skapa_ordlista()
        self.skapa_facit()
        self.längsta_ord()        

    def tom_spelplan(self):
        """SKapar en tom spelplan i form av en lista med listor."""
        self.spelplan = [["" for kolumn in range(self.storlek)] for rad in range(self.storlek)]
   
    def skapa_ordlista(self):
        """Läser in alla ord från memo.txt och lägger dom i self.ordlista."""
        ordfil = open("memo.txt", "r", encoding="utf8")
        for rad in ordfil:
            self.ordlista.append(rad.strip())
        ordfil.close()           

    def skapa_facit(self):
        """Lägger till samma ord på två random men alltid olika koordinater i listan self.facit tills alla 
            tomma platser är fyllda."""
        
        #Skapar facit som en lista med listor
        self.facit = [[None for kolumn in range(self.storlek)] for rad in range(self.storlek)]
        
        #Loopar tills alla platser är tilledelade ett ord
        while any(None in i for i in self.facit):
            #Skapar två listor två random heltal som används som koordinater
            xy1 = random.choices(range(self.storlek), k=2)
            xy2 = random.choices(range(self.storlek), k=2)

            #Kontroller att koordinaterna inte är lika och att inget ord redan finns på den platsen i listan self.facit
            if xy1 != xy2 and self.facit[xy1[1]][xy1[0]] == None and self.facit[xy2[1]][xy2[0]] == None:
                ord = self.ordlista[random.randint(0, len(self.ordlista)-1)]
                
                #Kontrollerar att ordet inte redant finns i facit
                if any(ord in i for i in self.facit) == False:
                    self.facit[xy1[1]][xy1[0]] = self.facit[xy2[1]][xy2[0]] = ord
              
    def längsta_ord(self):
        """Lägger till alla ord i facit i listan ord_i_facit och sorterar dem efter längd. 
            Tilldelar variabeln maxlängd_ord längden av det längsta ordet."""
        ord_i_facit = []
        for rad in self.facit:
            for ord in rad:
                ord_i_facit.append(ord)        
        ord_i_facit.sort(key=len)
        self.maxlängd_ord = len(ord_i_facit[-1])

class Ranglista:
    """
    Kass för att skriva till filen poänglista.txt och kontrollera vilken plats spelaren kom på. Returnerar en sträng.

    Atribut:
        self.storlek : int
        self.försök : int
        self.alla_resultat : list
    Metoder:
        __init__()
        läs_in_ranglista()
        __str__
    """
    def __init__(self, storlek, försök):
        """    
        Argument:
        storlek : int
        försök : in
        """

        self.storlek = storlek
        self.försök = försök
        self.alla_resultat = []
        self.läs_in_ranglista()
        
    def läs_in_ranglista(self):
        """Skriver antalet försök och storlek till filen poänglista.txt. Läser sedan in tidigare försök och bestämer vilken 
            plats spelaren kom på för given storlek."""
        
        #Skriver det senaste resultatet i filen på formatet storlek:försök
        with open("poänglista.txt", "a", encoding="utf8") as ranglista:
            ranglista.write(f"{self.storlek}:{self.försök}\n")
            ranglista.close()

        #Läser in alla tidigare resultat och lägger dem med samma storlek till listan self.alla_resultat
        with open("poänglista.txt", "r", encoding="utf8") as ranglista:
            for rad in ranglista:
                resultat = rad.strip().split(":")
                if resultat[0] == str(self.storlek):
                    self.alla_resultat.append(resultat[1])
            ranglista.close()
        
        #Sorterar listan alla_resultat och bestämmer index i listan för antalet försök 
        self.alla_resultat.sort(key=int)
        self.rang = self.alla_resultat.index(str(self.försök)) + 1   

    def __str__(self):
        return f"\nDu ligger på plats {self.rang} på ranglistan för spelplansstorlek {self.storlek}!" 
                       

class Gui:
    """
    Klass för ett GUI till spelet.

    Attributer:
        self.vallista : list
        self.gjorda_val : list
        self.ej_par : list
        self.antal_par : int
        self.antal_försök : int
        self.valnr : int
    Metoder:
        __init__()
        ange_storlek()  
        tryck_ok()
        textrutor()
        skapa_spelplan()
        importera_memory()
        kortknappar()
        välj_kort()
        kontrollera_par()
        nytt_spel()
        starta_om()       
    """
    def __init__(self):  
        """Skapar ett fönster self.fönster för GUI:n"""

        #Attributer
        self.vallista = []
        self.gjorda_val = []
        self.ej_par = []
        self.antal_par = 0
        self.antal_försök = 0
        self.valnr = 0

        #Huvudfönster
        self.fönster = tk.Tk()
        self.fönster.title("Memory")
        
        #Kör ange_storlek
        self.ange_storlek()
        
        #Mainloop
        self.fönster.mainloop()
        

    def ange_storlek(self):
        """Skapar en ram som innehåller inmatning för storlek ock en OK-knapp."""

        #Ram för storlek
        self.storleksram = tk.Frame(self.fönster)
        self.storleksram.grid(row=0, column=0, sticky=tk.N+tk.W)

        #Etikett för storlek
        self.storlekstext = tk.StringVar()
        self.storlekstext.set("Ange spelplanens storlek (AxA):")
        self.storleksetikett = tk.Label(self.storleksram, textvariable=self.storlekstext)
        self.storleksetikett.pack()

        #Inmatningsruta
        self.storleksvariabel = tk.StringVar()
        self.inmatningsruta = tk.Entry(self.storleksram, textvariable=self.storleksvariabel)
        self.inmatningsruta.pack()

        #OK-knapp
        self.ok_knapp = tk.Button(self.storleksram, text="OK", command=self.tryck_ok)
        self.ok_knapp.pack()


    def tryck_ok(self):
        """Körs när användaren anger storlek och trycker på OK."""

        #Om inmatningen är korrekt och sparar då inamatingen i self.storlek
        if felhantering_gui.jämnt_tal(self.storleksvariabel.get()):
            self.storlek = int(self.storleksvariabel.get())
            
            #Förstör ramen för storleksinmatning
            self.storleksram.destroy()

            #Kör följande metoder
            self.skapa_spelplan()
            self.textrutor()
            self.nytt_spel()

        #Vid felaktig inmatning ändras self.storlekstext
        else:
            self.storlekstext.set("Ange ett jämnt heltal mellan 2 och 10:")


    def textrutor(self):
        """Skapar de textrutor som visas under spelets gång"""

        #Ram för inforutor
        self.inforam = tk.Frame(self.fönster)
        self.inforam.grid(row=1, column=0, sticky=tk.N+tk.W)

        #Ruta för info om spelet
        self.spelinfo_text = tk.StringVar()
        self.spelinfo_text.set("Välj kort 1")
        self.spelinfo_etikett = tk.Label(self.inforam, textvariable=self.spelinfo_text)
        self.spelinfo_etikett.grid(row=1, column=0, sticky=tk.N+tk.W)

        #Ruta för antal försök
        self.försöksnr = tk.StringVar()
        self.försöksnr.set("")
        self.försök_etiktett = tk.Label(self.inforam, textvariable=self.försöksnr)
        self.försök_etiktett.grid(row=0, column=0, sticky=tk.N+tk.W)

        #Ruta för info om rang
        self.rang_text = tk.StringVar()
        self.rang_text.set("")
        self.rang_etikett = tk.Label(self.inforam, textvariable=self.rang_text)
        self.rang_etikett.grid(row=2, column=0, sticky=tk.N+tk.W)

    
    def skapa_spelplan(self):
        """Skapar en ram för spelkorten och kör metoderna för att skapa en spelplan."""

        #Ram för spelkort
        self.kortram = tk.Frame(self.fönster)
        self.kortram.grid(row=0, column=0, sticky=tk.N+tk.W)

        #Kör följande metoder
        self.importera_memory()
        self.kortknappar()

    def importera_memory(self):
        """Skapar ett objekt till klassen Memory och hämtar instanserna spelplan, maxlängd_ord och facit."""
        self.spel = Memory(self.storlek)
        self.spelplan = self.spel.spelplan
        self.bredd = self.spel.maxlängd_ord
        self.facit = self.spel.facit
    
    def kortknappar(self):
        """Skapae en knapp för varje spelkort och plaserar dem i ett rutnät i ramen self.kortram."""

        #Skapar knappar för varje spelkort
        for rad in range(self.storlek):
            for kolumn in range(self.storlek):
                self.kort_knapp = tk.Button(self.kortram, text=self.spelplan[rad][kolumn],
                                            font=("Comic Sans MS", 14, "bold"), width=self.bredd, bg="lightgray",
                                            command=lambda rad = rad, kolumn = kolumn: self.välj_kort(rad, kolumn))  #Idé om lambdafunktion hämtad från: https://stackoverflow.com/questions/18052395/array-of-buttons-in-python
                self.kort_knapp.grid(row=rad, column=kolumn, sticky=tk.N+tk.W)
                
                #Lägger in knapparna i spelplanen
                self.spelplan[rad][kolumn] = self.kort_knapp

    def välj_kort(self, rad, kolumn):
        """Körs när spelaren trycker på ett spelkort. Vänder tillbaka kor som inte var par. 
            Kör kontrollera_par när två kort valts. Räknar antalet försök."""
        
        #Vänder tillbaka korten som inte var par. Nollställer listan med kort som ej var par        
        if len(self.ej_par) == 4:
            self.spelplan[self.ej_par[0]][self.ej_par[1]]['bg'] = self.spelplan[self.ej_par[2]][self.ej_par[3]]['bg'] = "lightgrey"
            self.spelplan[self.ej_par[0]][self.ej_par[1]]['text'] = self.spelplan[self.ej_par[2]][self.ej_par[3]]['text'] = ""
            self.ej_par = []
       
        #Kontrollera ifall valt kort är nedvändt
        if self.spelplan[rad][kolumn]['text'] == "":
            self.spelplan[rad][kolumn]['text'] = self.facit[rad][kolumn]
            
            #Sparar index för valt kort i listan self.gjorda_val
            gjort_val = [rad, kolumn]
            self.gjorda_val.extend(gjort_val)

            #Ökar räknaren för antal valda kort
            self.valnr += 1
            self.spelinfo_text.set(f"Välj kort nummer {self.valnr + 1}")
           
            #Ifall två kort valts, kör kontrollera_par och öka antalet försök
            if self.valnr == 2:
                self.valnr = 0
                self.antal_försök += 1
                self.försöksnr.set(f"Antal försök: {self.antal_försök}")
                self.kontrollera_par()

    def kontrollera_par(self):
        """Körs när två kort valts. Kontrollerar orden är par."""
        
        #Ifall orden är par skrivs det ut och korten blir gröna
        if self.facit[self.gjorda_val[0]][self.gjorda_val[1]] == self.facit[self.gjorda_val[2]][self.gjorda_val[3]]:
            self.spelplan[self.gjorda_val[0]][self.gjorda_val[1]]['bg'] = self.spelplan[self.gjorda_val[2]][self.gjorda_val[3]]['bg'] = "lightgreen"
            self.spelinfo_text.set("Par! Välj nästa kort")
            self.gjorda_val = []
            self.antal_par += 1
       
        #Ifall orden inte är par skrivs det ut och korten blir röda 
        else:
            self.spelplan[self.gjorda_val[0]][self.gjorda_val[1]]['bg'] = self.spelplan[self.gjorda_val[2]][self.gjorda_val[3]]['bg'] = "tomato"
            self.spelinfo_text.set("Inget par! Välj nästa kort")
            self.ej_par.extend(self.gjorda_val)
            self.gjorda_val = []
        
        #Skriver ut "Du vann!" när alla par hittats och kör klassen Ranglista
        if self.antal_par == (self.storlek**2)/2:            
            self.spelinfo_text.set("Du vann!")
            self.rang_text.set(Ranglista(self.storlek, self.antal_försök))

    def nytt_spel(self):
        """Skapar en knapp för att starta om spelet."""
        #Ram för nytt-spel-knapp
        self.nytt_spel_ram = tk.Frame(self.fönster)
        self.nytt_spel_ram.grid(row=2, column=0, sticky=tk.N+tk.W)

        #Knapp för nytt spel
        self.nytt_spel_knapp = tk.Button(self.nytt_spel_ram, text="Nytt spel", command=self.starta_om)
        self.nytt_spel_knapp.pack()

    def starta_om(self):
        """Körs när spelaren trycker på knappen Nytt spel. Startar om spelet."""
        
        #Förstör alla ramar
        self.kortram.destroy()
        self.inforam.destroy()
        self.nytt_spel_ram.destroy()
       
        #Nollställer attributer
        self.vallista = []
        self.gjorda_val = []
        self.ej_par = []
        self.antal_par = 0
        self.antal_försök = 0
        self.valnr = 0

        #Kör ange_storlek
        self.ange_storlek()

def main():
    Gui()

if __name__ == "__main__":
    main()      
