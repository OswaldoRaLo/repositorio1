import sys

sumafinal=[]
acarreofinal=[]
sumafinalfinal=[]
#necesitamos dos digitos
numero1=sys.argv[1] if len(sys.argv) > 1 else input("Defina el primer numero: ")
longitudnumero1=len(numero1)
numero2=sys.argv[2] if len(sys.argv) > 1 else input("defina el segundo numero: ")
longitudnumero2=len(numero2)
#definamos como c al acarreo
c=0

#necesitamos comparar las longitudes

digitosfaltantes=longitudnumero1-longitudnumero2

#como sabemos a cual de los dos numeros es al que hay que acompletar

while longitudnumero1!=longitudnumero2:
    
    if longitudnumero1>longitudnumero2:
        #significa que hay que acompletar al numero 2
        numero2="0"+numero2
        longitudnumero2=longitudnumero2+1
    else:
        #hay que acompletar al numero 1
        numero1="0"+numero1
        longitudnumero1=longitudnumero1+1        

for i in range(longitudnumero1):

#necesitamos decirle la pareja de numeros que va a tomar
    
    a=numero1[-i-1]
    a=int(a)
    b=numero2[-i-1]
    b=int(b)
    
    resultado=a+b+c

    if (resultado)>9:
        resultado=resultado-10
        c=1
        sumafinal.append(resultado)
    else:
        c=0
        sumafinal.append(resultado)

acarreofinal.append(c)
sumafinal.reverse()

sumafinalfinal=acarreofinal+sumafinal

if c==0:
    print("El resultado final es: ",sumafinal)

else:
    print("El resultado final es: ",sumafinalfinal)
