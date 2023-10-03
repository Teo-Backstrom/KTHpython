# Teo Tim Otto


class Person:
    """
    Person klass med för och efternamn samt person nummer som egenskaper
    """

    # sparar egenskaperna hos objektet
    def __init__(
        self,
        förnamn,
        efternamn,
        person_nr,
    ):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.person_nr = person_nr

    # bestämmer hur objektet representeras som en sträng
    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.person_nr}"


class School:
    students = []

    def __init__(self, students):
        self.students.append(students)


def inläsning(typ=any, text="", ordtal=1):
    """
    Inläsningsverktyg som kollar att det är rätt typ och att det är rätt antal mellanslag

    Returns:
         En godkänd inmatning
    """
    while True:
        # skriver ut en text och tar in värde från användaren
        värde = input(text)

        try:
            # kollar om det är rätt typ
            typ(värde)
        except:
            # Skriver ut felmedelande ifall det behövs
            print("Personnumret får bara innehålla siffror, försök igen!")
        else:
            # Kollar att det är rätt antal mellanslag
            if len(värde.split(" ")) != ordtal:
                # Ger konstruktiv feedback
                print("Skriv förnamn och efternamn skillt av ett mellanslag")
            else:
                return värde


def main():
    """
    program för att ta in personerser och dess egenskapar och sedan skriva ut dem
    """
    # lista för att spara objekten i

    # Tar in 3st personer
    for i in range(3):
        # tar in namn
        namn = inläsning(
            typ=str, text="Vad heter studenten? (förnamn efternamn)", ordtal=2
        )
        # Delar på namnen till för och efternamn
        förnamn, efternamn = namn.split(" ")
        # tar in personnr
        person_nr = inläsning(typ=int, text="Vad är studentens personnr?")
        # sparar objektet i listan
        School((Person(förnamn, efternamn, person_nr)))
        print("\nObjektet skapat!\n")

    print("Här är alla studenter på KTH:")
    # Loppar igenom listan och skriver ut objekten och dess egenskaper
    for i in School.students:
        print(i)


# Kör mainfunktionen
main()
