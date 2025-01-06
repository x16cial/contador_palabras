import string

stop_words = {"que", "la", "los", "el", "de", "en", "a", "y", "para", "con", "se", "por", "como", "al", "del", "un", "una"}

def contar_palabras(archivo_nombre):
    while True:
        try:
            with open(archivo_nombre, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            
            contenido = contenido.lower().translate(str.maketrans("", "", string.punctuation))
            palabras = contenido.split()
            
            conteo = {}
            for palabra in palabras:
                if palabra not in stop_words:
                    conteo[palabra] = conteo.get(palabra, 0) + 1
            
            palabras_ordenadas = sorted(conteo.items(), key=lambda x: x[1], reverse=False)
            
            respuesta = input("Quieres ver la lista ordenada de mayor a menor? (si/no): ")
            if respuesta.lower() == "si":
                palabras_ordenadas.reverse()
            
            
            for palabra, frecuencia in palabras_ordenadas:
                print(f"{palabra}: {frecuencia}")
        
        except FileNotFoundError:
            print("El archivo no existe. Por favor verifica el nombre y la ubicacion.")
        
        respuesta = input("Quieres buscar otro archivo? (si/no): ")
        if respuesta.lower() != "si":
            print("Fin del programa.")
            break
        else:
            archivo_nombre = input("Ingresa el nombre del archivo (ejemplo: archivo.txt): ")

archivo_nombre = input("Ingresa el nombre del archivo (ejemplo: archivo.txt): ")
contar_palabras(archivo_nombre)

