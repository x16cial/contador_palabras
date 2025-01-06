import string
import urllib.request
import sys

stop_words = {"que", "la", "los", "el", "de", "en", "a", "y", "para", "con", "se", "por", "como", "al", "del", "un", "una", "a", "o", "e", "ah", "oh", "y", "i", "u", "uh", "hey"}

def obtener_contenido_de_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            contenido = response.read().decode('utf-8')
        return contenido
    except Exception as e:
        print(f"Hubo un error al intentar obtener el contenido: {e}")
        return ""

def contar_palabras(archivo_nombre, revertir=False):
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
            
            if revertir:
                palabras_ordenadas.reverse()
            
            for palabra, frecuencia in palabras_ordenadas:
                print(f"{palabra}: {frecuencia}")
        
        except FileNotFoundError:
            print("El archivo no existe. Por favor verifica el nombre y la ubicacion.")
        
        break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso incorrecto. Por favor escribe un archivo o enlace.")
    else:
        archivo_nombre = sys.argv[1]
        revertir = "-revertir" in sys.argv

        contar_palabras(archivo_nombre, revertir)
