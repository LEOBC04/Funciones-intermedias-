# Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6
# print(matriz)

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]
cantantes[0]["nombre"] = "Enrique Martin Morales"
# print(cantantes)


ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}
ciudades["México"][2] = "Monterrey"
# print(ciudades)

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]
coordenadas[0]["latitud"] = 9.9355431
# print(coordenadas)

# ===================================================================

# Iterar a través de una lista de diccionarios

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]


def iterar_diccionario(lista):
  
  for diccionario in lista:
    
    print(f"nombre - {diccionario["nombre"]} - país - {diccionario["pais"]} ")
    
# iterar_diccionario(cantantes)


# ===================================================================

#  Obtener valores de una lista de diccionarios

def iterar_diccionario_2 (key, array):
  
  for item in array:
    print(f"{key} - {item[key]}")
    
# iterar_diccionario_2("nombre", cantantes)


# ===================================================================

# Iterar a través de un diccionario con valores de lista

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimir_info (dicc):
  
  for items in dicc.items():
    
    print(f"{len(items[1])} {items[0]} \n")
    
    for element in items[1]:
      print(f"{element} \n")
    
imprimir_info(costa_rica)    