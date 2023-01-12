import turtle
import time

# Global Parameters
INITIAL_X = -300
INITIAL_Y = 0
V_0 = 0
MASS = 0.25 #kg
g = 0 # m/s^2
DELTA_T = 0.01 # seconds
TIMER = 0

# -----------------

def Simulation():
    print("Running Sim")
    Insight = Rocket()
    Bay = Docking_Bay()
    Driver = Pilot()
    Info = Diagnostics()
    wn = turtle.Screen()
    wn.title("Rocket Simulation")
    wn.bgcolor("Blue")
    wn.setup(height=600, width=800)
    wn.tracer(0)
    TIMER = 0
    wn.listen()
    
    end_sim = False
    while end_sim == False:
        #Driver.reset_thrust() # re-set thrust to 0
        x = Insight.get_xpos()
        Driver.compute(Insight.get_xpos())
        thrust = Driver.get_thrust()
        print(f"X Position: {x}   Velocity: {Insight.get_velocity()}   Acceleration: {Insight.get_acceleration()}")
        time.sleep(DELTA_T)
        Insight.set_acceleration(thrust)
        Insight.set_velocity()
        Insight.set_xpos()
        Info.update(thrust)
        wn.update()
        TIMER += 1



class Rocket(object):
    def __init__(self):
        global Rocket
        self.Rocket = turtle.Turtle()
        self.Rocket.speed(0)
        self.Rocket.shape("square")
        self.Rocket.color("Black")
        self.Rocket.penup()
        self.Rocket.goto(INITIAL_X,INITIAL_Y)
        #physics
        self.xpos = INITIAL_X
        self.velocity = V_0
        self.acceleration = 0
    def set_acceleration(self, thrust):
        self.acceleration = g + (thrust / MASS)
    def get_acceleration(self):
        return self.acceleration
    def set_velocity(self):
        self.velocity = self.velocity + (self.acceleration * DELTA_T)
    def get_velocity(self):
        return self.velocity
    def set_xpos(self):
        self.Rocket.setx(self.xpos + self.velocity * DELTA_T)
    def get_xpos(self):
        self.xpos = self.Rocket.xcor()
        return self.xpos



class Docking_Bay(object):
    def __init__(self):
        global Docking_Bay
        self.Dock = turtle.Turtle()
        self.Dock.speed(0)
        self.Dock.shape("square")
        self.Dock.color("white")
        self.Dock.shapesize(stretch_wid=5, stretch_len= 0.1)
        self.Dock.penup()
        self.Dock.goto(0, 0)

class Pilot(object):
    def __init__(self):
        self.force = 0
    def compute( self, position):
        x = position        
        if x < 0: # less than 0
            self.force = -x
        elif x > 0: # greater than 0
            self.force = -x
    def reset_thrust(self):
        self.force = 0
    def get_thrust(self):
        return self.force

class Diagnostics(object):
    def __init__(self):
        self.thrust = 0
        global Diagnostics
        self.Info = turtle.Turtle()
        self.Info.penup()
        self.Info.hideturtle()
        self.Info.goto(0,200)
        self.Info.color("white")
        self.Info.write(f"Thrust = {self.thrust}")
    def update(self, power):
        self.thrust = power
        self.Info.clear()
        self.Info.write(f"Thrust = {self.thrust}", align= "center")
    

def main():
    Simulation()
main()