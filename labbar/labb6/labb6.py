# Teo Bäckström, Otto, Tim grupp 29

class Person:
    """
    Person klass med egenskpar som förnamn efternamn personnummer och roll,
    Funktioner som kan ändra namn på person
    """

    def __init__(self, firstname, lastname, person_nr):
        """
        sparar egenskaperna hos objektet
        """
        self.firstname = firstname
        self.lastname = lastname
        self.person_nr = person_nr
        self.roll = "None"

    def __str__(self):
        """
        bestämmer hur objektet representeras som en sträng
        """
        return f"Namn: {self.firstname} {self.lastname} Personnr: {self.person_nr} Roll: {self.roll}"

    def rename(self):
        """
        Funktion som först kollar om användaren vill ändra namn om ja så ändrar den till det givna namnnet
        """
        control_quest = ""

        while control_quest not in ["j", "n"]:
            control_quest = input(
                f"Vill du ändra namn på {self.firstname} {self.lastname} (j/n)?"
            ).lower()
            if control_quest == "j":
                #tar in nytt namn
                firstname, lastname = nameinput(
                    text="Skriv in det nya namnet:", wordcount=2
                )
                #sparar in nytt namn på personen
                self.firstname = firstname
                self.lastname = lastname
                print(
                    f"Nu är namnet för {self.person_nr} ändrat till {firstname} {lastname}!"
                )

            else:
                print("Namnnet är inte ändrat")
                break


class Student(Person):
    """
    klassen student ärver från klassen Person och lägger till så rollen är Student
    """

    def __init__(self, firstname, lastname, person_nr):
        super().__init__(firstname, lastname, person_nr)
        self.roll = "Student"


class Teacher(Person):
    """
    klassen Teacher ärver från klassen Person och lägger till så rollen är Lärare
    """

    def __init__(self, firstname, lastname, person_nr):
        super().__init__(firstname, lastname, person_nr)
        self.roll = "Lärare"


class School:
    """
    Klassen School har 2 attribut där det är en var sin lista att spara student och teacher objekt i
    Klassen har också funktioner så som att skriva ut alla personer i vald lista, Lägga till personer i en lista,
    döpa om en person i en lista, ta bor en person i en lista, söka upp en person i en lista.
    """

    def __init__(self):
        """
        skapar 2 tomma listor när klassen School initiserar
        """
        self.students = []
        self.teachers = []

    def print_students(self):
        """
        Skriver ut alla studenter i listan students
        """
        for student in self.students:
            print(student)

    def print_teachers(self):
        """
        Skriver ut alla lärare i listan teachers
        """
        for teacher in self.teachers:
            print(teacher)

    def auto_add_student(self):
        """
        funktion för att automatsikt lägga till studenter från en fil
        Den retunerar ävan filnamnet så det kan användas för att spara filen
        """
        filefound = False
        filename = input("Vad heter filen med alla studenter?")
        #Kollar att filen finns
        while not filefound:
            try:
                studentsfile = open(filename, "r")
                filefound = True
            except:
                filename = input("Den filen fanns inte! Skriv in en ny fil:")
        
        students = []
        #läser in varje rad i filen och sparar respektive egenskapar i en variabel
        person_nr = studentsfile.readline().strip()
        while person_nr != "":
            lastname = studentsfile.readline().strip()
            firstname = studentsfile.readline().strip()
            #Sparar person info i lista
            students.append([firstname, lastname, person_nr])
            person_nr = studentsfile.readline().strip()
        studentsfile.close()
        #Skapar studentbojekt för vare person och lägger i school's lista
        for student in students:
            self.students.append(Student(student[0], student[1], student[2]))
        #retunerar filnamn
        return filename

    def person_nr_list(self):
        """
        funktion för att sammla alla personers personnummer i en lista som sedan retuneras
        """
        nr_list = []
        
        for student in self.students:
            nr_list.append(student.person_nr)
        for teacher in self.teachers:
            nr_list.append(teacher.person_nr)
        return nr_list

    def addperson(self):
        """
        funktion för att lägga till en person i en vald lista,
        frågar vilken roll personen har vad den heter och dens personnummer och sparar rätt objekt i rätt lista
        """
        print("Är personen en Lärare eller Student?")
        role = ""
        
        while role.lower() not in ["lärare", "student"]:
            role = input()
            if role.lower() not in ["lärare", "student"]:
                print('Du måste ange "Lärare" eller "Student"')
        #tar in namn
        firstname, lastname = nameinput(
            text="Vad heter personen? (firstname lastname)", wordcount=2
        )
        #tar in personnummer
        person_nr = person_nr_input(self.person_nr_list())
        #sparar som rätt objekt i rätt lista
        if role.lower() == "lärare":
            self.teachers.append(Teacher(firstname, lastname, person_nr))
        else:
            self.students.append(Student(firstname, lastname, person_nr))

    def rename_person(self):
        """
        funktion för att döpa om en person i vald lista
        frågar vilket peronnummer personen har och söker personen i listorna,
        tar ut personen och skickar den till rename funktionen
        """
        #tar in personnummer
        person_nr = person_nr_input()
        person = None
        #letar efter rätt person
        for student in self.students:
            if person_nr == student.person_nr:
                person = student
        for teacher in self.teachers:
            if person_nr == teacher.person_nr:
                person = teacher
        if (person == None):
            print("Ingen person hittades")
        else:
            person.rename()

    def remove_person(self):
        """
        Funktion för att ta bort vald person
        frågar för om personnummer och söker personen i listorna och kontrollfårgar användaren,
        sedan så tar den bort personen
        """
        is_teacher = False
        #tar in personnummer
        person_nr = person_nr_input()
        person = None
        #letar efter rätt person
        for student in self.students:
            if person_nr == student.person_nr:
                person = student
        for teacher in self.teachers:
            if person_nr == teacher.person_nr:
                person = teacher
                is_teacher = True

        if person == None:
            print("Ingen person hittades")
        else:
            control_quest = ""

            while control_quest not in ["j", "n"]:
                control_quest = input(
                    f"Vill du ta bort {person.firstname} {person.lastname} (j/n)?"
                ).lower()

                if control_quest == "j":
                    #tar bort personen från rätt lista
                    if is_teacher:
                        self.teachers.remove(person)
                    else:
                        self.students.remove(person)
                    print(
                        f"Nu är {person.person_nr}: {person.firstname} {person.lastname} borttagen!"
                    )
                else:
                    print("Inget har ändrats")

    def search_people(self):
        """
        funktion för att söka en person på namn,
        frågar först vad personen heter, två loopar itterar över listorna och sparar personerna i listan people
        Sedan så skrivs alla personer i listan ut
        """
        people = []
        #tar in namn
        firstname, lastname = nameinput(text="Vem vill du söka efter", wordcount=2)
        #kollar efter alla lärare med namnent
        for teacher in self.teachers:
            if teacher.firstname.lower() == firstname.lower() and (
                teacher.lastname.lower() == lastname.lower()
            ):
                people.append(teacher)
        #kollar efter alla studenter med namnet
        for student in self.students:
            if student.firstname.lower() == firstname.lower() and (
                student.lastname.lower() == lastname.lower()
            ):
                people.append(student)
        if len(people) == 0:
            print(f"Ingen person med namnet {firstname} {lastname} kunde hittas")
        else:
            #printar ut alla personer i listan
            for person in people:
                print(person)


def nameinput(text="", wordcount=1):
    """
    Funktion för att ta in namn i vald format(antal mellanslag)
    först frågar den om namn och kollar om den stämemr med kravet på mellanslag,
    sedan så splittar den namnet vid varje mellanslag för enklare hantering
    """
    name = ""
    # Kollar att det är rätt antal mellanslag
    while len(name.split(" ")) != wordcount:
        name = input(text)
        if len(name.split(" ")) != wordcount:
            # Ger konstruktiv feedback
            print(f"inmatningen måste vara uppdalad i {wordcount} del/delar")
        else:
            return name.split(" ")


def person_nr_input(used_nr = []):
    """
    kollar så att personnummret är ett gilltigt personnummer med 10 siffor,
    kollar först om det bara är siffror sdan om den tillhör en månad och en dag i den valda månaden
    """
    allowedinput = False
    monthday = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while not allowedinput:
        person_nr = input("Mata in personnummer (YYMMDDXXXX)")
        #kollar att det är en int
        try:
            int(person_nr)
        except:
            print("Personnummret får bara innehålla siffor")
        else:
            #kollar att datumet stämmer och att längden är 10 karaktärer
            month = int(person_nr[2:4])
            day = int(person_nr[4:6])
            if len(person_nr) != 10:
                print("Skriv personnummret med 10 siffror")
            elif month < 1 or month > 12:
                print(f"Månaden {person_nr[2:4]} finns inte")
            elif day < 1 or day > monthday[month - 1]:
                print("Dagen finns inte i vald månad")
            elif person_nr in used_nr:
                print("Personnummret är upptaget")
            else:
                allowedinput = True

    return person_nr

def save_to_file(school, filename):
    """
    funktion för att spara studenterna till vald lista
    loopar igenom alla studenter och skriver ut varje rad i filen
    """
    file = open(filename, "w")
    for person in school.students:
        file.write(person.person_nr + "\n")
        file.write(person.lastname + "\n")
        file.write(person.firstname + "\n")
        
    file.close()

def main():
    """
    funktion som kallar på alla andra funktioner,
    börjar med att skapa en instans av School samt kallar på auto_add_student() som lägger till alla studenter i en lista
    sedan så skriver den ut en meny till användaren där val leder till rätt funkiton som körs
    """
    
    school = School()
    filename = school.auto_add_student()
    value = ""
    while value != "7":
        value = input(
            "1 Vill du lägga till\n2 Ändra namn\n3 Ta bort\n4 Söka ett objekt\n5 Skriva ut alla studenter\n6 Skriva ut alla lärare\n7 Avsluta och spara\n"
        )
        if value == "1":
            school.addperson()
        elif value == "2":
            school.rename_person()
        elif value == "3":
            school.remove_person()
        elif value == "4":
            school.search_people()
        elif value == "5":
            school.print_students()
        elif value == "6":
            school.print_teachers()
        elif value == "7":
            save_to_file(school, filename)
            print("Hejdå")
        else:
            print("felaktig input")

#kör main-funktionen
main()
