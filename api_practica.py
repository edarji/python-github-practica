import requests

url = "https://jsonplaceholder.typicode.com/posts"

datos_enviados = {
    "tema": "Python",
    "objetivo": "aprender IA",
    "nivel": "principiante"
}

respuesta = requests.post(url, json=datos_enviados)

print(respuesta.status_code)
print(respuesta.json())

