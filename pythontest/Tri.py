class Tri:
    def __init__(self, b, h ):
        print("Running constructor")
        self.b = b
        self.h = h

    def __del__(self):
        print("Running destructor")

    def findarea(self):
        self.area = 1/2 * self.b * self.h

    def show(self):
        print("Area of the triangle est: ", self.area)


