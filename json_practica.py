import json

aprendizaje = {
    "tema": "Python",
    "nivel": "principiante",
    "objetivo": "usar IA"
}

print(type(aprendizaje))
texto_json = json.dumps(aprendizaje)

print(texto_json)
print(type(texto_json))
nuevo_diccionario = json.loads(texto_json)

print(type(nuevo_diccionario))
with open("datos.json", "w") as archivo:
    json.dump(aprendizaje, archivo)

with open("datos.json", "r") as archivo:
    datos_leidos = json.load(archivo)

print(type(datos_leidos))
print(datos_leidos["tema"])