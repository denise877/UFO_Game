#This special object is something which may randomly generate a new ball or shrink for each cycle. 
#Each time when a new ball be created, the special object will grew up a little bit.
#If there is no new ball be created in one cycle, the special object will shrink a little bit.
from simulton import Simulton
from prey import Prey
from ball import Ball
import model
import random 

class Special(Simulton):
    def __init__(self,x,y):
        
        Simulton.__init__(self,x,y,20,20)
    
    def update(self):
        if random.random() <= 0.2:
            model.add(Ball(self._x,self._y))
            self.change_dimension(2, 2)
        else:
            self.change_dimension(-1, -1)
        if self.get_dimension() == (0,0):
            model.remove(self)
    
    def display(self,canvas):
        w,h = self.get_dimension()
        canvas.create_oval(self._x - w/2, self._y - h/2, self._x + w/2, self._y + h/2,
                            fill='green')
            
    