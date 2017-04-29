from ev3dev.ev3 import *
from time import sleep



ts = TouchSensor();
assert ts.connected, "Connect a touch sensor to any port"
cl = ColorSensor();
assert cl.connected, "Connect a color sensor to any sensor port"
cl.mode='COL-REFLECT'
m=LargeMotor('outC')
m2=LargeMotor('outB')
m3=MediumMotor('outA')
btn = Button()


def left(state):

    if state:

        #grapR to senter2
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        m3.run_timed(time_sp=800, speed_sp=100)
        time.sleep(1)
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
        m.run_to_rel_pos(position_sp=-300, speed_sp=200, stop_action="hold")
        
        #grapR2
        time.sleep(3)
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        time.sleep(1)
        m3.run_timed(time_sp=500, speed_sp=-100)
        time.sleep(1)

        #reset
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
        while not ts.value():
          m.run_forever(speed_sp=200)
        m.run_to_rel_pos(position_sp=-300, speed_sp=200, stop_action="hold")
        
def right(state): 

    if state:
        
        #grapL to senter2
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        m3.run_timed(time_sp=800, speed_sp=100)
        time.sleep(1)
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
        m.run_to_rel_pos(position_sp=300, speed_sp=200, stop_action="hold")
        
        #grapL2
        time.sleep(3)
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        time.sleep(1)
        m3.run_timed(time_sp=500, speed_sp=-100)
        time.sleep(1)

        #reset
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
        while not ts.value():
          m.run_forever(speed_sp=200)
        m.run_to_rel_pos(position_sp=-300, speed_sp=200, stop_action="hold")
        
def up(state):

    if state:
            
       #grapR1
        time.sleep(2)
        m.run_to_rel_pos(position_sp=-300, speed_sp=200, stop_action="hold")
        time.sleep(2)
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        m3.run_timed(time_sp=800, speed_sp=100)
        time.sleep(1)
        
        #grapR to senter1
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
        m.run_to_rel_pos(position_sp=300, speed_sp=200, stop_action="hold")
        time.sleep(3)
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        m3.run_timed(time_sp=500, speed_sp=-100)
        time.sleep(1)
        
        #up
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
    
def down(state):

    if state:
            
        #grapR1
        time.sleep(2)
        m.run_to_rel_pos(position_sp=300, speed_sp=200, stop_action="hold")
        time.sleep(2)
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        m3.run_timed(time_sp=800, speed_sp=100)
        time.sleep(1)
        
        #grapR to senter1
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
        m.run_to_rel_pos(position_sp=-300, speed_sp=200, stop_action="hold")
        time.sleep(3)
        while cl.value() >=2:
          m2.run_forever(speed_sp=100)
        m2.stop(stop_action="hold")
        m3.run_timed(time_sp=500, speed_sp=-100)
        time.sleep(1)
        
        #up
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
    
def enter(state):

    if state:
        
        #reset
        while cl.value() <=5:
          m2.run_forever(speed_sp=-100)
          print(cl.value())
        m2.stop(stop_action="hold")
        while not ts.value():
          m.run_forever(speed_sp=200)
        m.run_to_rel_pos(position_sp=-300, speed_sp=200, stop_action="hold")


btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter

while True:
    btn.process()
    sleep(0.01)
#If you want stop program ,you will press down 'ctrl' and 'c'


