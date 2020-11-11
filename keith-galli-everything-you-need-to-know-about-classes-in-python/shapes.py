import turtle

class Polygon: 
  def __init__(self, sides, name, edge_length=100, color="black"):
    self.sides = sides
    self.name = name
    self.edge_length = edge_length
    self.color = color
    
  def draw(self):
    for i in range(self.sides):
      turtle.color(self.color)
      turtle.forward(self.edge_length)
      turtle.right(360/self.sides)
    #turtle.done()
    return
      
triangle = Polygon(3, 'triangle', 100, 'red')
square = Polygon(4, 'square', 50)
pentagon = Polygon(5, 'pentagon', 100)
hexagon = Polygon(6, 'hexagon', 100)

print('name: {}, sides: {}'.format(triangle.name, triangle.sides))
#print('name: {}, sides: {}'.format(pentagon.name, pentagon.sides))

#triangle.draw()
#square.draw()
#pentagon.draw()
#hexagon.draw()

#inheritance - create subclass
class Square(Polygon):
  def __init__(self, edge_length=100, color="black"):
    super().__init__(4, 'square', edge_length, color) #get init from Polygon

  #method overiding
  def draw(self):
    turtle.begin_fill()
    super().draw()
    turtle.end_fill()

square = Square(color='blue')
square.draw()