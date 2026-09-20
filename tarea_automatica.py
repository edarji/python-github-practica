from datetime import datetime

ahora = datetime.now()

with open("registro.txt", "a") as archivo:
    archivo.write(f"Mac mini ejecutó la tarea: {ahora}\n")

print(f"Tarea terminada: {ahora}")
