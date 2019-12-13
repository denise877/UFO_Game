import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
import random
import math
from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running     = False
cycle_count = 0
simultons       = set()
clicked     = ''
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,simultons
    running     = False
    cycle_count = 0
    simultons       = set()

#start running the simulation
def start ():
    global running
    running = True 


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 


#step just one update in the simulation
def step ():
    global cycle_count
    if running == True:
        update_all()
        running = False
    else:
        running = True
        update_all()
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global clicked
    clicked=kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if clicked =='':
        pass
    else:
        if clicked=='Remove':
            for object in simultons: #simulton is a set of objects on canvas which includes Balls/Preys/Blackholes/Hunter/Special
                if object.contains((x,y)): #xy tuple 
                    remove(object)
        else:
            add(eval('{}(x,y)'.format(clicked))) 
        


#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    a_set=set()
    for object in simultons:
        if p(object):
            a_set.add(object)
    return a_set


#call update for every simulton in the simulation
def update_all():
    global cycle_count,simultons,running
    if running:
        cycle_count += 1
        new_s=[s for s in simultons]
        for b in new_s:
                b.update()


#delete every simulton being simulated from the canvas; then call display for every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in simultons:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(str(cycle_count)+" cycles/"+str(len(simultons)))+" simultons")
