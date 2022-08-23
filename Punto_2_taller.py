"""
    Moisés De la Cruz Gallón
    Punto# 2: 
    En este punto lo que se busca es que 3 usuarios ingresen sus datos personales y que estos se guarden 
    en una estructura inmutable y luego mostrar los datos en una estructura mutable
    Se busca colectar la siguiente data: 
    ** Nombres y apellidos
    ** Ocupación
    ** Edad
    ** Ciudad
    ** Numero de Contacto
    ** Correo
    
    """
print("------------------------------------------------------------------------------------------")
print("                            (Usuario 1)                          ")
nombre_1 = str(input("Ingrese su nombre y apellido: "))
ocu_1 = str(input("A qué se dedica: "))
edad_1 = str(input("Que edad tiene: "))
ciudad_1 = str(input("En que ciudad recide: "))
numerotel_1 = str(input("Cual es su numero de telefono: "))
correo_1 = str(input("Cual es su correo: "))
usuario_1 = (nombre_1 , ocu_1, edad_1 , ciudad_1, numerotel_1 ,correo_1)
datos_1 = list (usuario_1)
print("------------------------------------------------------------------------------------------")
print("                            (Usuario 2)                          ")
nombre_2 = str(input("Ingrese su nombre y apellido: "))
ocu_2 = str(input("A qué se dedica: "))
edad_2 = str(input("Que edad tiene: "))
ciudad_2 = str(input("En que ciudad recide: "))
numerotel_2 = str(input("Cual es su numero de telefono: "))
correo_2 = str(input("Cual es su correo: "))
usuario_2 = (nombre_2 , ocu_2, edad_2 , ciudad_2, numerotel_2 ,correo_2)
datos_2 = list (usuario_2)
print("------------------------------------------------------------------------------------------")
print("                            (Usuario 3)                          ")
nombre_3 = str(input("Ingrese su nombre y apellido: "))
ocu_3 = str(input("A qué se dedica: "))
edad_3 = str(input("Que edad tiene: "))
ciudad_3 = str(input("En que ciudad recide: "))
numerotel_3 = str(input("Cual es su numero de telefono: "))
correo_3 = str(input("Cual es su correo: "))
usuario_3 = (nombre_3 , ocu_3, edad_3 , ciudad_3, numerotel_3 ,correo_3)
datos_3 = list (usuario_3)
print("------------------------------------------------------------------------------------------")


print (f"Los datos que fueron almacenados son los siguientes: {datos_1} , {datos_2}, {datos_3}")
print("------------------------------------------------------------------------------------------")