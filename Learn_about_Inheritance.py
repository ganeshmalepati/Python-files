# Multi-Level Inheritance

class GrandFather:
    G_Assest = "Land of 5 Acres"
    def __init__(self):
        self.money = 1000000
        self.gold = 1
        print(f"In my entire life span i have earned {self.money} lakhs of money and {self.gold} kg of gold")
    def Assests(self, P_Assest):
        pass
class Son(GrandFather):
    def __init__(self):
        super().__init__()
        self.Investment = "5M"
        print(f"Hello, My Dear son from my parents assests I have invested some money and make it double in my whole life. My father gave me worth {self.Investment} of money")
    def Assests_of_Son(self, P_Assest):
        # super.__init__()
        P_Assests_of_Son = "10 M worth Shares in Investment"
        print(P_Assests_of_Son, end="\n" f"We also have a house of {P_Assest}")
        print("\n")

class Grand_son(Son):
    def Assests_of_GrandSon(self):
        # super().__init__()
        P_Assests_of_GrandSon = "200 M worth Cryptocurrency"
        print(P_Assests_of_GrandSon)
G_son = Grand_son()
# G_son.Assests_of_Son()
G_son.Assests_of_Son("10 M worth")
G_son.Assests_of_GrandSon()


# Multiple Inheritance

class Shirt:
            Size = "M"
            colour = "Green"
            def __init__(self):
                print("I'm looking for a perfect pair of shirt and pant for me")
                print(f"Based on my fitness the size that fit for me is {self.Size} and i mostly prefer {self.colour} colour shirts")
class Pant:

    fit_1 = "skinny-fit"
    def __init__(self):
        super().__init__()
    def Show(self, fit_1):
        print(f"I love {self.fit_1} type of Jeans")
class Men(Shirt, Pant):
    def Perfect_match(self, colour, likes):
        # super().__init__()
        self.likes = "Grey"
        print(f"This {self.colour} colour shirt and {self.likes} pant is the perfect combination for me")

Comb = Men()
Comb.Show("skinny-fit")
Comb.Perfect_match("Blue", "Grey")







