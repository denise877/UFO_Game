# Black_Hole is derived from Simulton only: it updates by finding/removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model

class Black_Hole(Simulton):
    radius=10   
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20) 
        
    def contains(self,xy):
        if self.distance(xy) < self.get_dimension()[1]/2:
            return True
        return False
    
    def update(self):
        eaten_1= model.find(lambda x:isinstance(x, Prey))
        eaten=set()
        for i in eaten_1:
            if self.contains(i.get_location()):
                eaten.add(i)
        for i in eaten:
            model.remove(i)
        return eaten
    
    def display(self,canvas):
        w,h = self.get_dimension()
        canvas.create_oval(self._x - w/2, self._y - h/2, self._x + w/2, self._y + h/2,
                            fill='black')
        
        
#         self._x-Black_Hole.radius, self._y-Black_Hole.radius,
#                             self._x+Black_Hole.radius, self._y+Black_Hole.radius,
