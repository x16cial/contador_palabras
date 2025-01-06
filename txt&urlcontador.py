import string
import urllib.request

stop_words = {"que", "la", "los", "el", "de", "en", "a", "y", "para", "con", "se", "por", "como", "al", "del", "un", "una", "a", "o", "e", "ah", "oh", "y", "i", "u", "uh", "hey"}

def obtener_contenido_de_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            contenido = response.read().decode('utf-8')
        return contenido
    except Exception as e:
        print(f"Hubo un error al intentar obtener el contenido: {e}")
        return ""

def contar_palabras(archivo_nombre):
    while True:
        try:
            if archivo_nombre.startswith("http" or "https"):
                contenido = obtener_contenido_de_url(archivo_nombre)
            else:
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
        
        respuesta = input("Quieres buscar otro archivo o enlace? (si/no): ")
        if respuesta.lower() != "si":
            print("Fin del programa.")
            break
        else:
            archivo_nombre = input("Ingresa el nombre del archivo o enlace: ")

archivo_nombre = input("Ingresa el nombre del archivo o enlace: ")
contar_palabras(archivo_nombre)

