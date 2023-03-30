class Square:
    
    def __init__(self, size=0, position=(0, 0)):
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2: #or type(elem) is not int (for elem in value) or elem < 0 for elem in value:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value
    
    def area(self):
        x = self.__size
        return x * x

    def my_print(self):
        num = self.__size
        val = self.__position
        if num == 0:
            print("")
        else:
            for k in range(val):
                print(" ", end="")
            for i in range(num):
                print("#" * num)

    
    
