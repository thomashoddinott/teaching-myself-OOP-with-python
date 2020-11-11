import matplotlib.pyplot as plt

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, other):
    if isinstance(other, Point):
      x = self.x + other.x
      y = self.y + other.y
    else:
      x = self.x + other
      y = self.y + other
    
    return Point(x,y)

  def plot(self):
    plt.scatter(self.x, self.y)
    plt.show()

#a = Point(3,4)
#a.plot()
a = Point(1,1)
b = Point(2,2)
c = a + b #need to overload __add__ operator
#https://www.geeksforgeeks.org/operator-overloading-in-python/
#c.plot()

a = Point(0, 2)
d = a + 5
d.plot()