"""
        Moisés De la Cruz Gallón
        
    Punto #4
    
    La idea de este codigo es corregir el error para que nuestro algoritmo calcule la media entre 3 numeros
    
    Ejercicio sin corregir: 
    
    number_1 = 10
    number_2 = 20
    number_3 = 6.5
    media = number_1 + number_2 + number_3/3
    print(f"{media} es la nota media.")  
        """ 
"""
Solucion
    """
number_1 = 10
number_2 = 20
number_3 = 6.5

""" Al no colocar los parentesis se prioriza la division entre el number_3 y 3, lo que ocasiona
    que al sumar luego todo esto nos de un valor de 32.166666667 en vez del promedio real que es 12.166666666666666
                                                                                                                    """
media = (number_1 + number_2 + number_3)/3  
print(f"{media} es la nota media.")

