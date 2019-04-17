#sebastian vasquez ejercicio 1
rut=int(input("rut: "))
rutp=str(rut)
rutv=rutp[::-1]
d=list(rutv)
h=len(rutv)
if (h==7):
    a=(d[0]*2+d[1]*3+d[2]*4+d[3]*5+d[4]*6+d[4]*7+d[5]*2)
elif (h==8):
    a=int(d[0]*2+d[1]*3+d[2]*4+d[3]*5+d[4]*6+d[4]*7+d[5]*2+d[6]*3)
D=a%11
if (D==11):
    print("Su RUT es ", rut,"0")
if (D==10):
    print("Su RUT es ", rut,"k")
else:
    print("Su RUT es ", rut,"-", D)
