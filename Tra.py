import matplotlib 
import math
Cd=[
    [0.47,'Sphere'],
    [0.42,'Half-sphere'],
    [0.50,'Cone'],
    [1.05,'Cube'],
    [0.80,'Angled cube'],
    [0.82,'Long Cylinder'],
    [1.15,'Short cylinder'],
    [0.04,'Streamlined Body'],
    [0.09,'Streamlined HalfBody']
    ]
Ad=[]
V=0
G=9.80665
P=1.25
D=1.255
Fr=0
theta=0
M=0
r=0
alt=0
index=0
time=0
Radius=1
X=[alt,]
Y=[alt,]

def Move(V,theta,x,y):
    X.append(X[len(X)-1]+math.cos(theta)*(V*0.01))
    Y.append(Y[len(Y)-1]+math.sin(theta)*(V*0.01))

def Surface(Radius):
    return 2*Radius*math.pi

def Dragf(Cd,Surface,V,Ad,alt):
    return ( Cd[0] * (int(Ad[alt]) * int(V)**2/2) * Surface(Radius))

fo = open("Density.txt", "r")
for x in range(40000):
    print(fo.readline(x))
    Ad.append(fo.readline(x))

#Remove
V=100
theta=45
alt=0
M=10
#///
while True:
    alt = round(alt+X[len(X)-1])
    Move(V,theta,X,Y)
    V=V-(Dragf(Cd,Surface,V,Ad,alt) / M)*0.01
    time=time+0.01#seconds
