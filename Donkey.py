#Version Python 3.8.3
#Класс Осел

class Donkey:
    def __init__ (self, name, capacity, years):
        self.name = name
        self.capacity = capacity
        self.years = years

    def __str__ (self):
        return 'Donkey-boy ' + self.name + ', ' + str(self.capacity)
    
    def cry (self):
        return 'Eeyore'*self.years

    def work_hard (self, amount):
        if (amount <= 0): 
            self.years = self.years + 2
        else:
            amount = amount // 5
            if (amount < self.years):
                self.years = self.years - amount
            else:
                self.years = 0

    def carry (self, load):
        if (load > self.years):
            return False
        else:
            return True
