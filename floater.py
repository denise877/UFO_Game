# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,0,5) 
        self.randomize_angle()

    def update(self):
        self.move()  
        if random.random() <= 0.3:
            n=random.random()-0.5
            speed=self.get_speed()
            angle=self.get_angle()
            if speed+n >=3 and speed+n <=7:
                self.set_speed(speed+n)
            self.set_angle(angle+n)
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                            self._x+Floater.radius, self._y+Floater.radius,
                            fill='red')
