class DistanceConversion:
    def __init__(self,distance):
        self.__distance = distance

    def display(self):
        print("Centimeter: ", self.centimeter())
        print("Kilometer: ", self.kilometer())
        print("Inches: ", self.inches())

    def centimeter(self):
        return self.__distance * 100

    def kilometer(self):
        return self.__distance/1000

    def inches(self):
        return self.__distance * 39.37

distance = int(input("Enter a distance in meter: "))
dstnc = DistanceConversion(distance)
dstnc.display()
