
p_0 = 101.325
T0=288.15
g=9.80665
L=0.0065
R = 8.31447
M =0.0289644
h=0
fo=open("Density.txt", "w")
while h!= 40000:

    h=h+0.5
    print(h)
    p=p_0*(1-(L*h/T0))**(g*M/R*L)
    D=(p*M/R*T0)
    print(D)
    fo.write(str(D)+'\n')
