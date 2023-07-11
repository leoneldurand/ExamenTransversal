import sys

import os

# Variables
num_filas = 10
num_columnas = 4
precio_por_hectarea = 1000000
salir = 0

# Matriz de lotes disponibles
lotes_disponibles = [[' ' for _ in range(num_columnas)] for _ in range(num_filas)]

# Lista de lotes seleccionados por los clientes
lotes_seleccionados = []

# Lista de clientes
clientes = []

#Lista montos
montos = []
detalle = []
# Función para mostrar la disponibilidad de lotes
def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila in lotes_disponibles:
        for lote in fila:
            print('[X]' if lote == 'X' else '[ ]', end=' ')
        print()

# Función para seleccionar un lote
def seleccionar_lote():
    while True:
        
        try:
            fila = int(input("Ingrese el piso desde el 1 hasta el 10: "))
            columnaStr = input("Ingrese la letra del departamento: ")
            while columnaStr not in {'a', 'b','c','d','A','B','C', 'D'}:
                print("Debes elegir un departamento correcto, bien sea A, B, C o D")
                columnaStr = input("Ingrese la letra del departamento: ")
            
        except ValueError:
            print("Opción inválida. Intente nuevamente.")
            continue
        if columnaStr == 'a' or columnaStr == 'A':
            columna = 0
        elif columnaStr == 'b' or columnaStr == 'B':
            columna = 1
        elif columnaStr == 'c' or columnaStr == 'C':
            columna = 2
        elif columnaStr == 'd' or columnaStr == 'D':
            columna = 3
        
        fila = fila -1
        
        if fila < 0 or fila >= num_filas or columna < 0 or columna >= num_columnas:
            print("Debe elegir el piso y/o número de departamento correctamente. Intente nuevamente.")
            continue

        if lotes_disponibles[fila][columna] == ' ':
            break
        else:
            print("El departamente seleccionado no está disponible. Por favor, elija otro.")

    # Capturar datos del cliente
    try:
        rut = input("Ingrese el RUT del cliente: ")
        while rut.isnumeric() == False:
            print("El RUT debe ser número, no puede contener puntos o guiones")
            rut = input("Ingrese el RUT del cliente: ")
        nombre = str(input("Ingrese el nombre completo del cliente: "))
        
        while nombre.isalpha() == False:
            nombre = str(input("Ingrese el nombre completo del cliente: "))
        telefono = input("Ingrese el número de teléfono del cliente: ")
        while telefono.isnumeric() == False:
            print("El telefono debe ser numerico")
            telefono = input("Ingrese el telefono del cliente: ")
        email = str(input("Ingrese el correo electrónico del cliente: "))
        while email.isalpha() == False:
            email = str(input("Ingrese el correo electrónico del cliente: "))
    except ValueError:
        print("Debes ingresar opciones validas según corresponda")
    # Agregar el lote seleccionado a la lista de lotes seleccionados
    lotes_seleccionados.append((fila, columna))

    # Marcar el lote como vendido en la matriz de lotes disponibles
    lotes_disponibles[fila][columna] = 'X'

    # Agregar el cliente a la lista de clientes
    clientes.append((rut, nombre, telefono, email))
    print("Departamento seleccionado con éxito.")
    if columna == 0:
        monto= 3800
        col0 = " Tipo A "
    elif columna == 1:
        monto= 3000
        col0 = "Tipo B "
    elif columna == 2:
        monto= 2800
        col0 = "Tipo C "
    elif columna == 3:
        monto= 3500
        col0 = "Tipo D "
    piso = "Piso "
    fil = (fila+1)
    
    montos.append((monto))
    detalle.append((piso, fil, col0, monto))
    



# Función para mostrar la lista de clientes
def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    print("Lista de Clientes:")
    for cliente in clientes:
        rut, nombre, telefono, email = cliente
        print(f"RUT: {rut}")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Email: {email}")
        print()

def salir_del_programa():
    print("Saliendo del programa, gracias...")
    sys.exit(0)
    
def mostrar_ganancias_totales():
    print("Detalle vendidos")
    print(detalle)
    global suma
    suma=float(sum(montos))
    print ("Total vendido",suma,"UF")
    
    


# Función principal del programa
def main():
    while True:
        print("----- Menú -----")
        print("1. Comprar departamento")
        print("2. Mostrar disponibilidad de departamentos")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida. Intente nuevamente.")
            continue

        if opcion == 2:
            mostrar_disponibilidad_lotes()
        elif opcion == 1:
            seleccionar_lote()
        elif opcion == 3:
            mostrar_clientes()
        elif opcion == 4:
            mostrar_ganancias_totales()
        elif opcion == 5:
            salir_del_programa()
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa principal
main()