

class Person:
    def __init__(self, firstname, lastname, address, cc, phone):

        self.__firstname = firstname
        self.__lastname = lastname
        self.__address = address
        self.__cc = cc
        self.__phone = phone
    



    #firstname encapsulate
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @firstname.deleter
    def firstname(self):
        self.__firstname = None


    #lastname encapsulate
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @lastname.deleter
    def lastname(self):
        self.__lastname = None


    #address encapsulate
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @address.deleter
    def address(self):
        self.__address = None


    #cc encapsulate
    @property
    def cc(self):
        return self.__cc

    @cc.setter
    def cc(self, cc):
        self.__cc = cc

    @cc.deleter
    def cc(self):
        self.__cc = None


    #phone encapsulate
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @phone.deleter
    def phone(self):
        self.__phone = None

    def __str__(self):
        return  self.firstname + ' ' + self.lastname + ' ' + f'\n ID: {self.personid}'








# Only runs if this file is executed directly
if __name__ == "__main__":
    name = input('name ').capitalize()
    ze = Person(name, 'de deus', 'ualg', '45632155', '556 325 369')

    print(ze)
