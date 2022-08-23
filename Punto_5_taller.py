"""
        Moisés De la Cruz gallón 
        
        Punto# 5: 
        
        En el siguiente ejercicio al igual que el punto anterior se busca saber el promedio 
        pero esta vez se busca calcular el promedio de notas de un estudiante universitario.
        Tener en cuenta:
        * La nota maxima es 5
        * Porcentaje debe ser un numero entero debido a que en las formulas ya se esta dividiendo entre 100
        para hacer el calculo
                                                                                                                """
    
"""
    Primero se toman las notas del estudiante     
                                                 """
print("------------------------------------------------------------------------------------------")
nota_1= float(input("Ingrese la primera nota: "))
porcentaje_1 = float(input("Ingrese el porcentaje para esta nota: "))
nota_2= float(input("Ingrese la segunda nota: "))
porcentaje_2 = float(input("Ingrese el porcentaje para esta nota: "))
nota_3= float(input("Ingrese la tercera nota: "))
porcentaje_3= float(input("Ingrese el porcentaje para esta nota: "))
print("------------------------------------------------------------------------------------------")

""" Se calculan los porcentajes que van dstinados para cada nota
                                                                    """
porcen_1= porcentaje_1/100
porcen_2= porcentaje_2/100
porcen_3= porcentaje_3/100
promedio_estudiante= float((nota_1*porcen_1)+(nota_2*porcen_2)+(nota_3*porcen_3)) ##Se calcula el total o la nota final

""" Se muestra el promedio que lleva el estudiante segun sus notas
                                                                        """
print("------------------------------------------------------------------------------------------")
print(f"El promedio final para el estudiante es: \n\
      \n\
      {promedio_estudiante}\n\
      \n\
------------------------------------------------------------------------------------------")
