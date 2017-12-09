
import time,math,turtle
#Presets:
colour=000,000,000#Stores colour of line. Preset to Black
g=9.81
cD=0.47
v=0
cDs=[[0.47,'Sphere'],
    [0.42,'Half-sphere'],[0.50,'Cone'],
    [1.05,'Cube'],[0.80,'Angled Cube 45°'],
    [0.82,'Long cylinder'],[1.15,'Short cylinder'],
    [0.04,'Streamlined Body'],[0.09,'Stramlined Half-body']]

def input(g,colour,cD):
    g=input('What is the gravity of the situation:')
    v=input('what is the launch velocity')
    cd=input(cDs)

class Frame:#updates turtle frame

    def __init__(self):
        self.colour=colour
    def Draw(coordx,coordy):
        turtle.screensize(math.ceil(max(coordx)),math.ceil(max(coordy)))
        for x in range(len(Coodx)):

    #def update():# updates the frame

class projectile:
    coordx=[]
    coordy=[]
    def __init__(self):
        self.v=v
        self.g=g
        self.cD=cD
    def path():


while True:
