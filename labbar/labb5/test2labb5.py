# Teo Tim Otto


class Person:
    """
    Person klass med för och lastname samt person nummer som egenskaper
    """

    # sparar egenskaperna hos objektet
    def __init__(self, firstname, lastname, person_nr):
        self.firstname = firstname
        self.lastname = lastname
        self.person_nr = person_nr
        self.roll = "None"

    # bestämmer hur objektet representeras som en sträng
    def __str__(self):
        return f"Namn: {self.firstname} {self.lastname} Personnr: {self.person_nr} Roll: {self.roll}"

    def rename(self):
        control_quest = ""

        while control_quest != ("j" or "n"):
            control_quest = input(
                f"Vill du ändra namn på {self.firstname} {self.lastname} (j/n)?"
            ).lower()
        if control_quest == "j":
            firstname, lastname = nameinput(
                text="Skriv in det nya namnet:", wordcount=2
            )
            self.firstname = firstname
            self.lastname = lastname
            print(
                f"Nu är namnet för {self.person_nr} ändrat till {firstname} {lastname}!"
            )

        else:
            print("Namnnet är inte ändrat")


class Student(Person):
    def __init__(self, firstname, lastname, person_nr):
        super().__init__(firstname, lastname, person_nr)
        self.roll = "Student"


class Teacher(Person):
    def __init__(self, firstname, lastname, person_nr):
        super().__init__(firstname, lastname, person_nr)
        self.roll = "Lärare"


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def print_students(self):
        for student in self.students:
            print(student)

    def print_teachers(self):
        for teacher in self.teachers:
            print(teacher)

    def addperson(self):
        print("Är personen en Lärare eller Student?")
        role = ""
        while role.lower() not in ["lärare", "student"]:
            role = input()
            if role.lower() not in ["lärare", "student"]:
                print('Du måste ange "Lärare" eller "Student"')
        firstname, lastname = nameinput(
            text="Vad heter personen? (firstname lastname)", wordcount=2
        )
        person_nr = person_nr_input()

        if role.lower() == "lärare":
            self.teachers.append(Teacher(firstname, lastname, person_nr))
        else:
            self.students.append(Student(firstname, lastname, person_nr))

    def rename_person(self):
        person_n = person_nr_input()

        for student in self.students:
            if person_n == student.person_nr:
                person = student
        for teacher in self.teachers:
            if person_n == teacher.person_nr:
                person = teacher
        person.rename()

    def remove_person(self):
        is_teacher = False
        person_n = person_nr_input()
        person = None
        for student in self.students:
            if person_n == student.person_nr:
                person = student
        for teacher in self.teachers:
            if person_n == teacher.person_nr:
                person = teacher
                is_teacher = True
                

        if person == None:
            print("Ingen person hittades")
        else:
            control_quest = ""

            while control_quest != ("j" or "n"):
                control_quest = input(
                    f"Vill du ta bort {person.firstname} {person.lastname} (j/n)?"
                ).lower()

                if control_quest == "j":
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
        people = []
        firstname, lastname = nameinput(text="Vem vill du söka efter", wordcount=2)
        for teacher in self.teachers:
            if teacher.firstname.lower() == firstname.lower() and (
                teacher.lastname.lower() == lastname.lower()
            ):
                people.append(teacher)
        for student in self.students:
            if student.firstname.lower() == firstname.lower() and (
                student.lastname.lower() == lastname.lower()
            ):
                people.append(student)
        if len(people) == 0:
            print(f"Ingen person med namnet {firstname} {lastname} kunde hittas")
        else:
            for person in people:
                print(person)


def nameinput(text="", wordcount=1):
    name =""
    # Kollar att det är rätt antal mellanslag
    while len(name.split(" ")) != wordcount:
        name = input(text)
        if len(name.split(" ")) != wordcount:
        # Ger konstruktiv feedback
            print(f"inmatningen måste vara uppdalad i {wordcount} del/delar")
        else:
            return name.split(" ")


def person_nr_input():
    allowedinput = False
    monthday = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while not allowedinput:
        person_nr = input("Mata in personnummer (YYMMDDXXXX)")

        try:
            int(person_nr)
        except:
            print("Personnummret får bara innehålla siffor")
        else:
            month = int(person_nr[2:4])
            day = int(person_nr[4:6])
            if len(person_nr) != 10:
                print("Skriv personnummret med 10 siffror")
            elif month < 1 or month > 12:
                print(f"Månaden {person_nr[2:4]} finns inte")
            elif day < 1 or day > monthday[month - 1]:
                print("Dagen finns inte i vald månad")
            else:
                allowedinput = True
    return person_nr


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
                print(f"inmatningen måste vara uppdalad i {ordtal} del/delar")
            else:
                return värde


def main():
    school = School()

    value = ""
    while value != "7":
        value = input(
            "1 Vill du lägga till\n2 Ändra\n3 Ta bort\n4 Söka ett objekt\n5 Skriva ut alla studenter\n6 Skriva ut alla lärare\n7 För att avsluta\n"
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
            print("Hejdå")
        else:
            print("felaktig input")



main()