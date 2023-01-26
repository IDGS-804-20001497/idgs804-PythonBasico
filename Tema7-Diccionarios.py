miDiccionario={"Matricula": 123456, "Apellidos" : "Torres"}

print(miDiccionario["Apellidos"])

miDiccionario["Materia"] = "DWP"
print(miDiccionario)

miDiccionario["Matricula"] = "67890"
print(miDiccionario)

del miDiccionario["Apellidos"]
print(miDiccionario)

