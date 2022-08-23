""" 
    Moisés De la Cruz gallón
    Punto # 6: 

    La siguiente matriz (o lista con listas anidadas) debe cumplir que el cuarto elemento de cada fila 
    sea la suma de los tres primeros elementos de la fila respectivamente. Si nota las sumas que se encuentran 
    están erróneas,debe modificarlas dando 2 soluciones, una con append y otra con slicing.
                                                                                                                """

"""                         Primera propuesta se solicion para el ejercicio
                                                                                        """

matriz_1 = [          ##DISEÑO DE LA MATRIZ DADA
    [2,4,3],
    [8,3,4],
    [7,1,3],
    [9,2,1]
    ]
suma1 = sum(matriz_1[0]) # SUMA DE TODOS LOS DATOS DE LA LISTA 0
suma2 = sum(matriz_1[1]) # SUMA DE TODOS LOS DATOS DE LA LISTA 1
suma3 = sum(matriz_1[2]) # SUMA DE TODOS LOS DATOS DE LA LISTA 2
suma4 = sum(matriz_1[3]) # SUMA DE TODOS LOS DATOS DE LA LISTA 3

matriz_1[0].append(suma1) # AGREGAR CON APPEND EL RESULTADO DE LA SUMA DE  
matriz_1[1].append(suma2) # TODOS LOS NUMEROS DENTRO DE NUESTRA LISTA
matriz_1[2].append(suma3) # AL FINAL DE LA MISMA
matriz_1[3].append(suma4)
print("----------------------------------Primera Solución----------------------------------------")
print(matriz_1) #RESULTADOS DE LA SUMA AGREGADOS A LA MATRIZ
print("------------------------------------------------------------------------------------------")
"""                         Segunda propuesta de solucion al ejercicio. 
                                                                                                """
matriz_2 = [          ##DISEÑO DE LA MATRIZ DADA
    [2,4,3],
    [8,3,4],
    [7,1,3],
    [9,2,1]
    ]

valor1 = matriz_2[0][0::1] # Con el uso de slicing escogemos los dato de la lista que vamos a sumar
valor2 = matriz_2[1][0::1] # Y los almacenamos en las variable valor_x  
valor3 = matriz_2[2][0::1] # Así mismo primero le indicamos a cual de las lista de nuestra matriz
valor4 = matriz_2[3][0::1] # va a ingresar 

suma_1 = sum(valor1) #Luego adicionamos los valores que guardamos en las variables valor_x
suma_2 = sum(valor2)
suma_3 = sum(valor3)
suma_4 = sum(valor4)

matriz_2[0].insert(4,(suma_1)) # insertamos el resultado de la suma a cada una de las 
matriz_2[1].insert(4,(suma_2)) # listas de la matriz
matriz_2[2].insert(4,(suma_3))
matriz_2[3].insert(4,(suma_4))
print("----------------------------------Segunda Solución----------------------------------------")
print(matriz_2)
print("------------------------------------------------------------------------------------------")