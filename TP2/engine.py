

class Engine:
    def __init__(self, fuel, power, torque, displacement, clylinders, system, weight, manufacturer):
        
        self.fuel = fuel
        self.power = power
        self.torque = torque
        self.displacement = displacement
        self.clylinders = clylinders
        self.system = system
        self.weight = weight
        self.manufacturer = manufacturer


    #fuel encapsulate
    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel

    @fuel.deleter
    def fuel(self):
        self.__fuel = None



    #power encapsulate
    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    @power.deleter
    def power(self):
        self.__power = None


    #torque encapsulate
    @property
    def torque(self):
        return self.__torque

    @torque.setter
    def torque(self, torque):
        self.__torque = torque

    @torque.deleter
    def torque(self):
        self.__torque = None


    #displacement encapsulate
    @property
    def displacement(self):
        return self.__displacement

    @displacement.setter
    def displacement(self, displacement):
        self.__displacement = displacement

    @displacement.deleter
    def displacement(self):
        self.__displacement = None


    #clylinders encapsulate
    @property
    def clylinders(self):
        return self.__clylinders

    @clylinders.setter
    def clylinders(self, clylinders):
        self.__clylinders = clylinders

    @clylinders.deleter
    def clylinders(self):
        self.__clylinders = None


    #system encapsulate
    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        self.__system = system

    @system.deleter
    def system(self):
        self.__system = None


    #weight encapsulate
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @weight.deleter
    def weight(self):
        self.__weight = None


    #manufacturer encapsulate
    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @manufacturer.deleter
    def manufacturer(self):
        self.__manufacturer = None

    def __str__(self):
        return (f'\nFuel: {self.system}\nHorsepower: {self.power}\nTorque: {self.torque}\nDisplacement: {self.displacement}\nNumber clylinders: {self.clylinders}\nStarting system: {self.system}\nWeight: {self.weight}\nManufacturer: {self.manufacturer}')
                


# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    v8 = Engine('gasoline', 56325, 556.6, 5656.5, 5, 'manual', 85, 'honda')

    print(v8)
