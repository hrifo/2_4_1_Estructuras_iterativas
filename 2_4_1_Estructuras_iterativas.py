# print('Hola a todos, voy a ejecutar este programa')
# sentencia = True
# while(sentencia):
#     print('Hola mundo!')
#     print('La sentencia es True')
#     sentencia = bool(int(input('Ingrese valor de la sentencia(1=True||0=False): ')))

# print('La sentencia es falsa')

# numero = int(input('Ingrese un numero positivo: '))

# while numero<=0:
#     print('Estimado, el numero es negativo, por favor reintente: ')
#     numero=int(input('Ingrese nuevamente el numero positivo: '))

# print(f'El numero es {numero}, gracias por su cooperacion.')

# inicio = 0
# fin = 20

# while inicio<fin:
#     print(inicio)
#     if inicio == 10:
#         print('Se romperá el ciclo en la repetición N°10')
#         break
#     inicio+=1

####
####  Calculadora
####
salir=False
while not salir:
    print (" Calculadora")
    print ("=============")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicar")
    print ("4. Dividir")
    print ("5. Salir")
    print ("=============")
    variable=input("Ingrese la operación:")
    if (variable=="1"):
        n1=float(input('Ingrese el primer numero:'))
        n2=float(input('Ingrese el segundo numero:'))
        resultado=n1+n2
        print ("El resultado de sumar ",n1," y ",n2," es :",resultado)
        input("Presione Enter para continuar...!")
        continue
    if (variable=="2"):
        n1=float(input('Ingrese el primer numero:'))
        n2=float(input('Ingrese el segundo numero:'))
        resultado=n1-n2
        print ("El resultado de la resta ",n1," y ",n2," es :",resultado)
        input("Presione Enter para continuar...!")
        continue
    if (variable=="3"):
        n1=float(input('Ingrese el primer numero:'))
        n2=float(input('Ingrese el segundo numero:'))
        resultado=n1*n2
        print("La Multiplicación:",n1," y ",n2," es :",resultado)
        input("Presione Enter para continuar...!")
        continue
    if (variable=="4"):
        n1=float(input('Ingrese el primer numero:'))
        n2=float(input('Ingrese el segundo numero:'))
        if (n2==0):
            resultado=0
            print("Div. entre 0 es indeterminada")
        else:
            resultado=n1/n2
        print ("El resultado de Dividir ",n1," y ",n2," es :",resultado)
        input("Presione Enter para continuar...!")
        continue
    if (variable=="5"):
        salir=True
    else:
        print("Opción Inválida..Intente de nuevo")
        input("Presione Enter para continuar...!")

