class Square:
    
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, z):
        if type(z) is not int:
            raise TypeError("size must be an integer")
        elif z < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = z
    
    def area(self):
        x = self.__size
        return x * x

