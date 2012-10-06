# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *
import operator

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (0.5 * self.base) * self.height
    def __str__(self):
        return "Triangle with base %0.1f and height %0.1f" % (self.base, self.height)

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.shape_list = []
        self.index = -1

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if sh not in self.shape_list:
            self.shape_list.append(sh)
        else:
            print "Class is already there"

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        return self

    def next(self):
        if self.index == len(self.shape_list) - 1:
            raise StopIteration
        self.index += 1
        return self.shape_list[self.index]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        temp_list = []
        for cls in self.shape_list:
            if isinstance(cls, Square):
                temp_list.append("Square with side %0.1f" % cls.side)
            elif isinstance(cls, Circle):
                temp_list.append("Circle with radius %0.1f" % cls.radius)
            elif isinstance(cls, Triangle):
                temp_list.append("Triangle with base %0.1f and height %0.1f" % (cls.base, cls.height))
        temp_list.sort()
        return join(temp_list, "\n")

#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    shapes_area = {}
    for i in shapes:
        shapes_area[i] = i.area
    return max(shapes_area.iteritems(), key=operator.itemgetter(1))[0]


#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    f = open(filename, "r")
    f_list = f.readlines()
    f.close()
    shapes = ShapeSet()
    
    for i in range(0, len(f_list)): 
            f_list[i] = f_list[i].strip()	
	
    for i in f_list:
            info = i.split(",")            
            if info[0] == "circle":                    
                    shapes.addShape(Circle(float(info[1])))
            elif info[0] == "square":                    
                    shapes.addShape(Square(float(info[1])))
            elif info[0] == "triangle":
                    shapes.addShape(Triangle(float(info[1]),float(info[2])))
    return shapes
    
    
    
    
if __name__ == "__main__":
    #newSet = ShapeSet()
    #newSq = Square(15)
    #newCi = Circle(10)
    #newTr = Triangle()
    #anotherSq = Square(11)
    #newSet.addShape(newSq)
    #newSet.addShape(newTr)
    #newSet.addShape(newCi)
    #print newSet
    print readShapesFromFile("shapes.txt")
    
