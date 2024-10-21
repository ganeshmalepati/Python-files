class Employee:
    name = "Malepati"     # class Attributes
    age = 23              # class Attributes
    salary = 263000              # class Attribute
    lang = "Python"

    def getInfo(self):
        print(f"This language belongs to {self.lang}.. \nThe name of the employee is {self.name}.... \nThis Employee is working in a {self.company} company")
        print(f"Based on my experience level i'm getting {self.salary}")

Ganesh = Employee()
Ganesh.company = "Capgemini"   #ObJ attribute
# print(Ganesh.name,"\n",Ganesh.age,"\n",Ganesh.salary, "\n", Ganesh.company)
Ganesh.lang = "Java"
Ganesh.getInfo()           # In this the method is called by using ObJ reference
Employee.getInfo(Ganesh)   # The mehtod is called by using Class name



class Investment:
    Company_1 = "Tata"
    Company_2 = "Banking Sector"
    Company_3 = "IT Sector"
    Mutual_funds = "ICICI prudential funds"

    def __init__(self):         # Constructor in python, Constructor is the special function of the class which is used to initialize the objects. 
        print("I'm creating a portfolio with good returns for the upcoming year")
        print(f"The provided three companies will give a good return in the nect couple of years \nThey are \n{self.Company_1}\n{self.Company_2}\n{self.Company_3}")
    
    def getInfo(self):         # The self parameter is the first parameter, it is used to access other data members of the class
        print(f"The {self.Company_1} and {self.Company_3} company stocks are providing much returns in a short period of time")
        print(f"Apart from stocks there is one Mutual fund which provide higher returns in a period of 3 years\nIt is : {self.Mutual_funds}")

Holding = Investment()
# print(end="\n")
Holding.getInfo()



Calculator functions

class Calculator:
    def __init__(self, n):
        self.n = n
    def Square(self):
        print(f"The Square of the provided number is {self.n * self.n}")
    def cube(self):
        print(f"The Cube of the provided number is {self.n * self.n * self.n}")
    def Squareroot(self):
        print(f"The Squareroot of the provided number is {self.n ** 1//2}")
    @staticmethod
    def Multiple():
        print("Hello there is no multiple of the give number")

Math = Calculator(6)
Math.cube()
Math.Square()
Math.Squareroot()
Math.Multiple()
        

#Train Ticket

from random import randint

class TrainTicket:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    @staticmethod
    def Book(Train_no, Start_Jun, end_Jun):
        # Train_no = randint(00000, 40000)
        # Start_Jun = "Yerraguntla"
        # end_Jun = "Delhi NCR"
        print(f"Your train ticket has been booked with train number {Train_no} and it will start from {Start_Jun} to {end_Jun}")
    @staticmethod
    def getStatus(name, age, sex, Train_no, Start_Jun, end_Jun):
        print(f"Your Ticket has been Booked \nYOur ticker details are : \n Name : {name} \n Age : {age} \n sex : {sex} \n Train_no : {Train_no} \n Starting_Junction : {Start_Jun} \n End_Junction : {end_Jun} \n")
    @staticmethod
    def getFare(ticket_price, Charges):
        # ticket_price = randint(500, 1500)
        # Charges = randint(10,30)
        print(f"The price of the ticket is {ticket_price} and charges for this ticket is {Charges}")
    


Ticket = TrainTicket("Ganesh", 23, "M")
Ticket.Book(randint(00000, 40000), "Yerraguntla", "Delhi NCR")
Ticket.getStatus("Ganesh", 23, "M", randint(00000, 40000), "Yerraguntla", "Delhi NCR")
Ticket.getFare(randint(500, 1500), randint(10,30))

