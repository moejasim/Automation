class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        arearesult = self.length*self.width
        print(arearesult)
my_area=Rectangle(10,5)
print(my_area.length)
print(my_area.width)

my_area.area()