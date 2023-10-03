class Vara():

    def __init__(self, kod, namn, pris_antal):
        self.kod = kod
        self.namn = namn
        self.pris_antal = pris_antal



lager = []
file = f = open('HemmaTest\varu\lager.txt', 'r')
print(f.readline())