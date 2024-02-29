

from person import Person
from color import Color
from engine import Engine


class Car:
    def __init__(self, owner, color, engine, brand, model, consumption, kms):
        # Verify the argument types
        assert isinstance(owner, Person)
        assert isinstance(color, Color)
        assert isinstance(engine, Engine)

        # Define the properties
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.kms = kms

    #brand encapsulate
    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @brand.deleter
    def brand(self):
        self.__brand = None


    #model encapsulate
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @model.deleter
    def model(self):
        self.__model = None


    #consumption encapsulate
    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption):
        self.__consumption = consumption

    @consumption.deleter
    def consumption(self):
        self.__consumption = None


    #kms encapsulate
    @property
    def kms(self):
        return self.__kms

    @kms.setter
    def kms(self, kms):
        self.__kms = kms

    @kms.deleter
    def kms(self):
        self.__kms = None

    def __str__(self):
        return f'\nbrand: {self.brand}' + f'\nmodel: {self.model}'


# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    ze = Person('ze', 'de deus', 'ualg', '45632155', '556 325 369')
    v8 = Engine('gasoline', 56325, 556.6, 5656.5, 5, 'manual', 85, 'honda')
    red = Color('white', '000')

    car = Car(
        owner=ze,
        color=red,
        engine=v8,
        brand="UMM",
        model="Alter",
        consumption=8,
        kms=100000,
    )

    print(car)
