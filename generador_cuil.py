'''El sufijo actúa como dígito verificador, su valor está en función de los 10 dígitos previos(prefijo y DNI)
El prefijo y el sufijo se calculan de la siguiente manera:
1.	Se multiplica cada uno de los 8 dígitos del DNI por un factor, y se suman las multiplicaciones; los 8 
factores, en orden, son (3, 2, 7, 6, 5, 4, 3, 2)
2.	A la suma anterior se le suma 10 si es varón o 38 si es mujer.
3.	Se calcula el resto de dividir esa suma por 11.
4.	Si el resto es uno, entonces el prefijo es 23, y el sufijo es 9 para varón y 4 para mujer.
5.	Si el resto es cero, entonces el prefijo es 20 para varón y 27 para mujer, y el sufijo es cero.
6.	Si no, el prefijo es 20 para varón y 27 para mujer, y el sufijo es 11 menos el resto calculado en (3).
Por ejemplo, dado un varón con DNI 08424054, su CUIL es 20-08424054-1.'''

print('*'* 20)
print("GENERACION DE CUIL")
print('*' * 20)

#Variables
edad = 0
genero = 0
prefijo = 0
sufijo = 0
m = 0
f = 0

#Ingresar datos
nombre = input("Dime tu nombre: ")
dni = input("Ingrese su dni: ")

#Chequear la edad
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Eres menor de edad, no puedes tener CUIL todavía")
else:
    print("Eres mayor de edad, puedes tener CUIL")

#Ingresar el genero
genero = input("ingrese su genero m, f: ")

#Agregar prefijo y sufijo

lista1 = [int(a) for a in str(dni)]
lista2 = [3, 2, 7, 6, 5, 4, 3, 2]
producto = [x*y for x, y in zip(lista1, lista2)]

suma = sum(producto)
print(suma) #solo para chequear hay que borrarlo

#Si es varon suma + 10
if m:
    resto = (suma + 10)
    print(resto)  # solo para chequear hay que borrarlo

#Si es mujer suma + 38
#else:
    #resto = (suma + 38) % 11
    #print(resto) #solo para chequear hay que borrarlo

#Si el resto es uno, entonces el prefijo es 23, y el sufijo es 9 para varón y 4 para mujer.
    #if resto == 1:
        #prefijo = 23
        #print (prefijo) #solo para chequear hay que borrarlo
        #if genero:
            #m
            #sufijo = 9
            #print(sufijo) #solo para chequear hay que borrarlo
        #else:
            #sufijo = 4
            #print(sufijo) #solo para chequear hay que borrarlo
    
    
#Si el resto es cero, entonces el prefijo es 20 para varón y 27 para mujer, y el sufijo es cero.
    #if resto == 0:
        #sufijo = 0
    #print(sufijo) #solo para chequear hay que borrarlo
        #if genero:
            #m
            #prefijo = 20
    #print(prefijo) #solo para chequear hay que borrarlo
        #else:
            #prefijo = 27
    #print(prefijo) #solo para chequear hay que borrarlo

#Si no, el prefijo es 20 para varón y 27 para mujer, y el sufijo es 11 menos el resto calculado en(3).
    #if resto != 0 and resto != 1:
        #sufijo = 11 - resto
    #print(sufijo) #solo para chequear hay que borrarlo
        #if genero:
            #m
            #prefijo = 20
    #print(prefijo) #solo para chequear hay que borrarlo
        #else:
            #prefijo = 27
    #print(prefijo)#solo para chequear hay que borrarlo

#print(f'Hola {nombre} tu número de cuil es {prefijo} - {dni} - {sufijo}')

        
        
