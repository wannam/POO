

class Color:


    def __init__(self, namecolor, r, g, b):
        
        self.__namecolor = namecolor
        self.__r = r
        self.__g = g
        self.__b = b


    #color name encapsulate
    @property
    def namecolor(self):  
        return self.__namecolor

    @namecolor.setter
    def namecolor(self, namecolor):
        self.__namecolor = namecolor

    @namecolor.deleter
    def namecolor(self):
        self.__namecolor = None

    #R encapsulate
    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        self.__r = r

    @r.deleter
    def r(self):
        self.__r = None

    #G encapsulate
    @property
    def g(self):
        return self.__g

    @g.setter
    def g(self, g):
        self.__g = g

    @g.deleter
    def g(self):
        self.__g = None

    #B encapsulate
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @b.deleter
    def b(self):
        self.__b = None
    

    def __str__(self):
        return self.namecolor

# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    red = Color('white', '000')

    print(red)
