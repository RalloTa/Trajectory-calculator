
import time
import math
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

coordx=[]
coordy=[]
coordz=[]

cD=[[0.47,'Sphere'],
    [0.42,'Half-sphere'],[0.50,'Cone'],
    [1.05,'Cube'],[0.80,'Angled Cube 45°'],
    [0.82,'Long cylinder'],[1.15,'Short cylinder'],
    [0.04,'Streamlined Body'],[0.09,'Stramlined Half-body']]

c=0
g=9.81

print("\033c")
#print("\033c")
v=input('velocity ')
#print("\033c")
theta=input('angle ')
#print("\033c")
alt=input('launch altitude ')
#print("\033c")

def Graph(v,theta,alt,c):

    D=(float(v)**2)*math.sin(math.radians(2*float(45)))/9.81

    print('Distance: '+str(D)+" m")


    for x in range(0,int(2*D),1):

        y=float(x)*math.tan(math.radians(float(theta)))
        y=y-(g*(float(x)**2)/(2*(float(v)*math.cos(math.radians(float(theta))))**2))

        coordy.append(y)
        coordx.append(float(x))

        if y<=0:
            c=c+1
            if c==2:
                break
with plt.xkcd():
    Graph(v,theta,alt,c)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(coordx,coordy, label='Trajectory')
    ax.legend()
    plt.show()
