"""
    Moisés De la Cruz Gallon
    Punto#7: 
    Debes utilizar todo lo que sabes sobre los strings, las listas y sus métodos o funciones para transformar 
    el siguiente texto:
    thorlanzó su martillo#flashha fallado por un pie! -gritóLoki Laufeyson#dos pies-le   
    corrigió Hulk#flashmenea   la   cabeza   como   disgustado...-agrega   el comentarista
    En:
    Thor lanzó su martillo...
    -¡Flash ha fallado por un pie!-gritó Loki Laufeyson.
    -Dos pies le corrigió Hulk.
    -Flash menea la cabeza como disgustado... -agrega el comentarista.
    """


texto= "thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado… -agrega el comentarista"

texto_lista = texto.split("#") # ME DELIMITA CADA PARTE DE LA ORACION CUANDO ENCUENTRA UN 
                                # ASI MISMO ME CREA LAS POSICIONES Y LAS ALMACENA EN UNA LISTA

primer = texto_lista[0].capitalize() + "..." #Thor lanzó su martillo...

segundo = " - "+ "¡"+texto_lista[1].capitalize().replace("loki laufeyson","Loki Laufeyson") # -!Flash ha fallado por un pie!-gritó Loki Laufeyson.
                                                 
tercero= " - "+texto_lista[2].capitalize().replace("-","").replace("hulk","Hulk")+"." # -Dos pies le corrigió Hulk.
                                                                
cuarto = " - "+texto_lista[3].capitalize() # -Flash menea la cabeza como disgustado... -agrega el comentarista.
texto_final = primer+"\n"+segundo+"\n"+tercero+"\n"+cuarto+"\n" # CONCATENACION DE TODOS LOS STRING
""" Al concatenar todo este deberia ser el resultado:
    Thor lanzó su martillo...
    -¡Flash ha fallado por un pie!-gritó Loki Laufeyson.
    -Dos pies le corrigió Hulk.
    -Flash menea la cabeza como disgustado... -agrega el comentarista.
                                                                        """
print(texto_final) # MOSTRAR RESULTADO FINAL
