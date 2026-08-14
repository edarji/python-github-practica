def saludar(nombre):
    return f"Estoy aprendiendo {nombre}"

personas = ["Python", "Git", "Github","IA"]

for persona in personas:
	if persona=="IA":
		print("IA es nuestro objetivo final")    
	else:	
		print(saludar(persona))
	