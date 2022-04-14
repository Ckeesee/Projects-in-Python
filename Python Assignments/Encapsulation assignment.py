
#utilize protected variables and objects
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 56
print(obj._protectedVar)

#utilize private variables and objects

class Protected2:
    def __init__(self):
        self.__privateVar = 37

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar=private

obj = Protected2()
obj.getPrivate()
obj.setPrivate(58)
obj.getPrivate()
