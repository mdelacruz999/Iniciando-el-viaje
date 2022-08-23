"""
    Moisés De la Cruz Gallón
    Punto# 3 
    En este punto lo que se busca es pasar una temperatura en grados Fahrenheit a grados centigrados o viceversa
    """
    ##PARA CONVERTIR DE FAHRENHEIT A CELCIUS
print("------------------------------------------------------------------------------------------")    
temperatura_Fahrenheit = float(input("Ingrese el valor de la temperatura en escala fahrenheit: "))
print (f"El valor de la temperatura ingresada es: {temperatura_Fahrenheit}°F")
conversion_temp_C = ((temperatura_Fahrenheit-32)/1.8) ## Formula para cambiar grados Fahrenheit a Celcius
print (f"La temperatura ingresada es igual en grados celcius a: {conversion_temp_C}°C")
print("------------------------------------------------------------------------------------------")
    ##PARA CONVERTIR DE CELCIUS A FAHRENHEIT
temperatura_celcius = float(input("Ingrese el valor de la temperatura en escala celcius: "))
print (f"El valor de la temperatura ingresada es: {temperatura_celcius}°C")
conversion_temp_F = ((9*temperatura_celcius)/5)+32 ## Formula para cambiar grados Celcius a Fahrenheit
print (f"La temperatura ingresada es igual en grados Fahrenheit a: {conversion_temp_F}°F")
print("------------------------------------------------------------------------------------------")