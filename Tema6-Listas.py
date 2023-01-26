lista1 = ["Amanda", 1.2, 23, True]
print(lista1)
print(lista1[2:4])
print(lista1[:2])
print(lista1[3:])

lista1.append("Noemí") #agrega elementos a la lista
print(lista1)

lista1.insert(0, "Torres")
print(lista1)

lista1.extend([9, 10, 11])
print(lista1)

print(lista1.index("Noemí"))
lista1.remove("Amanda")
print(lista1)

lista1.pop()
print(lista1)
