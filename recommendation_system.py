productos = {
    "Laptop": ["tecnologia", "estudio", "trabajo"],
    "Tablet": ["tecnologia", "estudio"],
    "Smartphone": ["tecnologia", "comunicacion"],
    "Audifonos": ["tecnologia", "musica"],
    "Teclado": ["tecnologia", "trabajo"],
    "Libro de Python": ["estudio", "programacion"]
}

def recomendar_producto(nombre):
    if nombre not in productos:
        return []

    categorias = productos[nombre]
    recomendaciones = []

    for producto, etiquetas in productos.items():
        if producto != nombre:
            coincidencias = 0

            for categoria in categorias:
                if categoria in etiquetas:
                    coincidencias += 1

            if coincidencias > 0:
                recomendaciones.append(producto)

    return recomendaciones


print("Productos disponibles:")

for producto in productos:
    print("-", producto)

nombre = input("\nEscribe un producto exactamente como aparece: ")
resultado = recomendar_producto(nombre)

if resultado:
    print("\nProductos recomendados:")
    for producto in resultado:
        print("-", producto)
else:
    print("\nNo encontré recomendaciones. Revisa el nombre escrito.")