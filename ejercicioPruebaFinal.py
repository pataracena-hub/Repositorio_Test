productos_repositorio = []

def menu():
    print("\n----Menu Gestion de Productos----")
    print("1. Agregar Producto")
    print("2. Buscar Producto")
    print("3. Eliminar Producto")
    print("4. Actualizar Disponibilidad (Sustraer Stock)")
    print("5. Mostrar Productos Disponibles")
    print("6. Salir")

def validar_string(texto: str):
    return texto.strip() != ""

def validar_precio(precio: int):
    return precio > 0

def validar_stock(cantidad: int):
    return cantidad >= 0

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion (1/6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debes ingresar una opcion entre el 1 y el 6")
        except ValueError:
            print("Opcion no valida")

def agregar_producto(nombre: str, precio: int, stock: int, disponibilidad: bool):
    producto = {
        "nombre": nombre, 
        "precio": precio, 
        "stock": stock, 
        "disponibilidad": disponibilidad 
    }
    productos_repositorio.append(producto)
    print("¡Producto agregado correctamente!")

def validar_producto():
    nombre = input("Ingrese un nombre para su producto: ")
    if not validar_string(nombre):
        input("El nombre ingresado no es valido. Presione ENTER para continuar")
        return
    
    try:
        precio = int(input("Ingrese el valor de su producto: "))
        if not validar_precio(precio):
            input("El precio debe ser mayor a 0. Presione ENTER para continuar.")
            return
    except ValueError:
        input("Valor incorrecto. Presione ENTER para continuar")
        return
    
    try:
        stock = int(input("Ingrese el stock inicial: "))
        if not validar_stock(stock):
            input("El stock no debe ser menor a 0. Presione ENTER para continuar.")
            return
    except ValueError:
        input("El valor ingresado no es correcto. Presione ENTER para continuar")
        return
    
    disponibilidad = stock > 0
    agregar_producto(nombre, precio, stock, disponibilidad)

def buscar_producto(nombre: str):
    for p in productos_repositorio:
        if p["nombre"].lower() == nombre.lower():
            print(f"\nNombre: {p['nombre']}\nPrecio: {p['precio']}\nStock: {p['stock']}\nDisponible: {p['disponibilidad']}")
            return p
    print("Producto no encontrado.")
    return None
        
def eliminar_producto(nombre: str):
    for p in productos_repositorio:
        if p["nombre"].lower() == nombre.lower():
            productos_repositorio.remove(p)
            print("Producto eliminado correctamente")
            return
    print("No se encontro el producto para eliminar.")

def actualizar_disponibilidad(nombre: str):
    # Buscamos el producto internamente
    producto = None
    for p in productos_repositorio:
        if p["nombre"].lower() == nombre.lower():
            producto = p
            break

    if not producto:
        input("No se ha encontrado el producto solicitado. Presione ENTER para continuar.")
        return
        
    try:
        stock_a_restar = int(input(f"Stock actual ({producto['stock']}). Ingrese las unidades a sustraer: "))
        if stock_a_restar < 0:
            input("La cantidad no puede ser negativa. Presione ENTER para continuar")
            return
        if producto["stock"] - stock_a_restar < 0:
            input("La cantidad ingresada excede el stock disponible. Presione ENTER para continuar")
            return
            
        producto["stock"] -= stock_a_restar
        
        # Actualiza el estado de disponibilidad automáticamente si llega a 0
        if producto["stock"] == 0:
            producto["disponibilidad"] = False
            
        input("Stock actualizado correctamente. Presione ENTER para continuar...")
    except ValueError:
        input("Cantidad no valida. Se esperaba un valor numerico entero. Presione ENTER para continuar...")

def mostrar_disponibilidad():
    if not productos_repositorio:
        print("No hay productos en el sistema.")
        return
    for p in productos_repositorio:
        print(f"Nombre: {p['nombre']} | Estado Disponible: {p['disponibilidad']} | Stock: {p['stock']}")

# Bucle principal
while True:
    menu()
    opcion = leer_opcion()

    if opcion == 1:
        validar_producto()
    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto a buscar: ")
        buscar_producto(nombre)
    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(nombre)
    elif opcion == 4:
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        actualizar_disponibilidad(nombre)
    elif opcion == 5:
        mostrar_disponibilidad()
    else:
        print("Saliendo del programa. ¡Hasta luego!")
        break
