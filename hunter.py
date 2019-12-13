# Hunter is derived from the Mobile_Simulton/Pulsator classes: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    dis=200
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        width,height=self.get_dimension()
        self.speed=5
        self.angle=0
        Mobile_Simulton.__init__(self,x,y,width,height,self.angle,self.speed)
        self.randomize_angle()
        
    def update(self):
        Pulsator.update(self)
        a_set=model.find(lambda x:isinstance(x,Prey))
        chase=None
        d=Hunter.dis
        for i in a_set:
            if self.distance(i.get_location()) <= d:
                d=self.distance(i.get_location())
                chase=i.get_location()
        if chase != None:
            angle=atan2(chase[1]-self.get_location()[1],chase[0]-self.get_location()[0])
            self.set_angle(angle)
        self.move()
        
        
            