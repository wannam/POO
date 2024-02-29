

class Color:


    def __init__(self, namecolor, rgb, colorid):
        
        self.__namecolor = namecolor
        self.__rgb = rgb
        self.colorid = colorid


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

    #RGB encapsulate
    @property
    def rgb(self):
        return self.__rgb

    @rgb.setter
    def rgb(self, rgb):
        self.__rgb = rgb

    @rgb.deleter
    def rgb(self):
        self.__rgb = None
    
    #colorid encapsulate
    @property
    def colorid(self):
        return self.__colorid

    @colorid.setter
    def colorid(self, colorid):
        self.__colorid = colorid

    @colorid.deleter
    def colorid(self):
        self.__colorid = None

    def __str__(self):
        return self.namecolor

# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    red = Color('white', '000')

    print(red)
