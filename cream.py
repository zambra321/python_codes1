# *** Programa de Delivery para un supermercado ***


# Función para limpiar la pantalla del terminal (cmd o consola)
def limpiar_pantalla():
    from os import system
    system("cls")  # Comando para limpiar la consola en Windows

limpiar_pantalla()  # Llama a la función para limpiar la pantalla al inicio del programa

# Función principal del ciclo del menú de opciones
def val_inicio():
    while True:
        try:
            print("""Elija una opción\n\n
1 >>> Registrarse \n
2 >>> Iniciar Sesión\n
0 >>> Salir\n\n""")
            inicio = int(input(""))  # Solicita la opción de inicio
            if inicio>=0<=2:
              return inicio
            else:
                print("OPCIÓN NO VALIDA")
                
        except ValueError:
            limpiar_pantalla()
            print(">>> INGRESE UNA OPCIÓN EN NÚMEROS ENTEROS <<<\n")

def val_seccion():
    while True:
        try:
            seccion = int(input(""))  # Solicita la opción de inicio
            limpiar_pantalla()
            if seccion>=0<=4:
              return seccion
            else:
                print("OPCIÓN NO VALIDA")
                
        except ValueError:
            limpiar_pantalla()
            print(">>> INGRESE UNA OPCIÓN EN NÚMEROS ENTEROS <<<\n")
            print("""¿A qué sección quiere ir? (Ingrese el número de la sección)
               
1). Verduras y Frutas
2). Lacteos
3). Bebidas
4). Higiene personal
0). Salir""")


def ciclo_menu():
    print(f"*** Bienvenido/a {nombre} a Pedidos Nya! ***")
    print("")
    a = input("Presione ENTER para continuar...")  # Espera que el usuario presione ENTER
    limpiar_pantalla()   
    carrito_de_compra = 0  # Inicializa el total del carrito de compras
    productos_comprados = []  # Lista para almacenar los productos comprados
    
    # Ciclo principal donde se presenta el menú de secciones
    while True:
        print("""¿A qué sección quiere ir? (Ingrese el número de la sección)
               
1). Verduras y Frutas
2). Lacteos
3). Bebidas
4). Higiene personal
0). Salir""")
        
        print("")
        print(f"                         Carrito de compra actual: $ {carrito_de_compra}")
        print("")
        seccion=val_seccion()
        limpiar_pantalla()   
        
        # Sección de Verduras y Frutas
        if seccion == 1:
            while True:
                print(f"""*** SECCIÓN DE VERDURAS Y FRUTAS ***
                      
Ingrese el número de lo que desea agregar al carrito
                      

1). Papas (Kg) - $1000 x Kg
2). Tomate (Kg) - $1000 x Kg
3). Frutilla (Kg) - $2500 x Kg
4). Uva (Kg) - $6000 x Kg
0). Salir.
                                      

                         Carrito de compra: $ {carrito_de_compra}""")
                producto = int(input(""))  # Solicita el número del producto
                limpiar_pantalla()   
                if producto == 1:  # Opción de Papas
                    print(">>> Ingrese 0 para volver a la sección 'Verduras y Frutas' <<<\n")
                    print("$ 1.000 x Kg")
                    cant = int(input("Ingrese cuántos Kg desea: "))  # Solicita la cantidad de papas
                    limpiar_pantalla()   
                    if cant > 0:  # Verifica que la cantidad sea positiva
                        total_producto = cant * 1000  # Calcula el total por el precio
                        carrito_de_compra += total_producto  # Añade al total del carrito
                        productos_comprados.append((f"Papas (Kg)", cant, total_producto))  # Añade el producto a la lista
                        print(f"{cant} Kg de 'Papas' añadidas al carrito\n")
                        input("Presione ENTER para continuar...")  # Espera que el usuario presione ENTER
                        limpiar_pantalla()   
                elif producto == 2:
                    print(">>> Ingrese 0 para volver a la sección 'Verduras y Frutas' <<<\n")
                    print("$ 1.000 x Kg")
                    cant = int(input("Ingrese cuántos Kg desea: "))
                    limpiar_pantalla()
                    if cant > 0:
                        total_producto = cant * 1000
                        carrito_de_compra += total_producto
                        productos_comprados.append((f"Tomate (Kg)", cant, total_producto))
                        print(f"{cant} Kg de 'Tomate' añadidos al carrito")
                elif producto == 3:
                    print(">>> Ingrese 0 para volver a la sección 'Verduras y Frutas' <<<\n")
                    print("$ 2.500 x Kg")
                    cant = int(input("Ingrese cuántos Kg desea: "))
                    limpiar_pantalla()
                    if cant > 0:
                        total_producto = cant * 2500
                        carrito_de_compra += total_producto
                        productos_comprados.append((f"Frutilla (Kg)", cant, total_producto))
                        print(f"{cant} Kg de 'Frutilla' añadidos al carrito")
                elif producto == 4:
                    print(">>> Ingrese 0 para volver a la sección 'Verduras y Frutas' <<<\n")
                    print("$ 6.000 x Kg")
                    cant = int(input("Ingrese cuántos Kg desea: "))
                    limpiar_pantalla()
                    if cant > 0:
                        total_producto = cant * 6000
                        carrito_de_compra += total_producto
                        productos_comprados.append((f"Uva (Kg)", cant, total_producto))
                        print(f"{cant} Kg de 'Uva' añadidos al carrito")

                elif producto == 0:  # Salir de la sección de Verduras y Frutas
                    break
                else:  # Opción inválida
                    print("Ingrese una opción válida")
                    input("Presione ENTER para continuar...")
        elif seccion == 2:
            while True:
                print(f"""*** SECCION DE LACTEOS *** \n
Ingrese el numero de lo que desea agregar al carrito \n\n 
1). Leche Entera Colun 1L - $1000 c/u
2). Yogurt Batido Vainilla Soprole 165g - $490 c/u
3). Yogurt Batido Frutilla Soprole 165g - $490 c/u
4). Queso Gauda Soprole 15 Laminas - $2890 c/u
0). Salir.
                            \n                         Carrito de compra: $ {carrito_de_compra}""")
                producto = int(input(""))
                limpiar_pantalla()
                if producto == 1:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 1.000 c/u")
                    cant = int(input("Ingrese cuanta cantidad desea..."))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 1000
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Leche Entera Colun 1L", cant, multiplicacion))
                        print(f"{cant} 'Leche Entera Colun 1L' ha sido añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                        print("")
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                elif producto == 2:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 490 c/u")
                    cant = int(input("Ingrese cuanta cantidad desea..."))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 490
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Yogurt Batido Vainilla Soprole 165g", cant, multiplicacion))
                        print(f"{cant} 'Yogurt Batido Vainilla Soprole 165g' añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                elif producto == 3:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 490 c/u")
                    cant = int(input("Ingrese cuanta cantidad desea..."))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 490
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Yogurt Batido Frutilla Soprole 165g", cant, multiplicacion))
                        print(f"{cant} 'Yogurt Batido Frutilla Soprole 165g' añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")     
                elif producto == 4:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 2.890 c/u")
                    cant = int(input("Ingrese cuanta cantidad desea..."))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 2890
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Queso Gauda Soprole 15 Laminas", cant, multiplicacion))
                        print(f"{cant} 'Queso Gauda Soprole 15 Laminas' añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                elif producto == 0:
                    break
                else:
                    print("Ingrese opción válida...\n")
                    a = input("Presione ENTER para continuar...")
                    limpiar_pantalla()    
        elif seccion == 3:
            while True:
                print(f"""*** SECCION DE BEBIDAS *** \n
Ingrese el numero de lo que desea agregar al carrito \n
1). Coca Cola (2L) - $2.000 c/u
2). Sprite (2L) - $2.000 c/u
3). Monster (473ml) - $1.800 c/u
4). Red Bull (250ml) - $1.600 c/u
0). Salir.
                            \n                         Carrito de compra: $ {carrito_de_compra}""")
                producto = int(input(""))
                limpiar_pantalla()
                if producto == 1:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Bebidas' <<<\n")
                    print("$2.000 (c/u)")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 2000
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Coca Cola (2L)", cant, multiplicacion))
                        print(f"{cant} 'Coca Cola(s)' ha sido añadida(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                        print("")
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto == 2:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Bebidas' <<<\n")
                    print("$2.000 (c/u)")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 2000
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Sprite (2L)", cant, multiplicacion))
                        print(f"{cant} 'Sprite(s)' añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                        print("")
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                elif producto == 3:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Bebidas' <<<\n")
                    print("$1.800 c/u")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 1800
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Monster (473ml)", cant, multiplicacion))
                        print(f"{cant} 'Monster(s)' añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto == 4:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Bebidas' <<<\n")
                    print("$1.600 c/u")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 1600
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Red Bull (250ml)", cant, multiplicacion))
                        print(f"{cant} 'Red Bull(s)' añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto == 0:
                    break
                else:
                    print("Ingrese opción válida")
                    print("")
                    a = input("Presione ENTER para continuar...")
                    limpiar_pantalla()
  
        elif seccion == 4:
            while True:
                print(f"""*** SECCION DE HIGIENE PERSONAL *** \n
Ingrese el número de lo que desea agregar al carrito \n
1). Toallas femeninas 'Care Up' (8 unidades) - $1.000 c/u
2). Paquete Confort (4 unidades) - $1.000 c/u
3). Toallas húmedas 'Huggies' (48 unidades) - $1.500 c/u
4). Desodorante spray Nivea Man (150ml) - $2.000 c/u
0). Salir.
                    \n                         Carrito de compra: ${carrito_de_compra}""")
                producto = int(input(""))
                limpiar_pantalla()
                if producto == 1:
                    limpiar_pantalla()

                    print(">>> Ingrese 0 para volver a la sección 'Higiene Personal' <<<\n")
                    print("$1.000 (c/u)")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 1000
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Toallas femeninas 'Care Up' (8 unidades)", cant, multiplicacion))
                        print(f"{cant} 'Toallas femeninas' han sido añadidas al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()

                elif producto == 2:
                    limpiar_pantalla()

                    print(">>> Ingrese 0 para volver a la sección 'Higiene Personal' <<<\n")
                    print("$1.000 (c/u)")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 1000
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Paquete Confort (4 unidades)", cant, multiplicacion))
                        print(f"{cant} Paquete(s) Confort añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")

                elif producto == 3:
                    limpiar_pantalla()

                    print(">>> Ingrese 0 para volver a la sección 'Higiene Personal' <<<\n")
                    print("$1.500 (c/u)")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 1500
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Toallas húmedas 'Huggies' (48 unidades)", cant, multiplicacion))
                        print(f"{cant} Toallas húmedas añadidas al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()

                elif producto == 4:
                    limpiar_pantalla()

                    print(">>> Ingrese 0 para volver a la sección 'Higiene Personal' <<<\n")
                    print("$2.000 (c/u)")
                    cant = int(input("Ingrese la cantidad que desea... "))
                    limpiar_pantalla()
                    if cant > 0:
                        multiplicacion = cant * 2000
                        carrito_de_compra += multiplicacion
                        productos_comprados.append(("Desodorante spray Nivea Man (150ml)", cant, multiplicacion))
                        print(f"{cant} Desodorante(s) Nivea Man (150ml) añadido(s) al carrito\n")
                        input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()

                elif producto == 0:
                    break

                else:
                    print("Ingrese opción válida\n")
                    input("Presione ENTER para continuar...\n")
                    limpiar_pantalla()
        
        elif seccion==0:
            break
    total_pagar = carrito_de_compra
    limpiar_pantalla()
    print("*** Información del Cliente ***")
    print("")
    print(f"Nombre del cliente: {nombre}")
    print(f"Total a pagar: $ {total_pagar}")
    print("\n*** Detalle de productos comprados ***\n")
    for producto, cantidad, precio in productos_comprados:
        print(f"- {producto}: {cantidad} Unidad(es) - Total: $ {precio}\n")
    print("\n*** FIN DEL PROGRAMA ***\n")
    input("Presione ENTER para finalizar...\n")
    limpiar_pantalla()

# Ciclo para manejar el registro de usuarios y el inicio de sesión
usuarios=[]
while True:
    inicio = val_inicio()
    limpiar_pantalla()
    
    # Registro de usuario
    if inicio == 1:
        print("*** REGISTRO DE USUARIO ***\n\n")
        nombre = input("Cree el nombre de usuario...\n")  # Solicita un nombre de usuario
        contraseña = input("Cree su contraseña...\n")  # Solicita una contraseña
        limpiar_pantalla()
        while True:
            confirmar_contraseña = input("Confirme su contraseña...\n")  # Solicita confirmación de la contraseña
            limpiar_pantalla()
    
            if contraseña == confirmar_contraseña:  # Verifica que las contraseñas coincidan
                usuarios.append((nombre, contraseña))  # Agrega el usuario a la lista
                break
            else:
                print("No coinciden las contraseñas\n")  # Si no coinciden las contraseñas
                a = input("Presione ENTER para continuar...")
                limpiar_pantalla()

    # Inicio de sesión
    elif inicio == 2:
        print("*** INICIO DE SESION ***\n\n")
        nombre = input("Ingrese nombre de usuario\n\n")  # Solicita el nombre de usuario
        limpiar_pantalla()
       
        if any(user[0] == nombre for user in usuarios):  # Verifica si el usuario existe
            while True:
                contraseña = input("Ingrese su contraseña\n\n ")  # Solicita la contraseña
                limpiar_pantalla()
                if any(user[0] == nombre and user[1] == contraseña for user in usuarios):  # Verifica que la contraseña sea correcta
                    print("Inicio de sesión exitoso\n")
                    a = input("Presione ENTER para continuar...\n\n")
                    limpiar_pantalla()
                    ciclo_menu()  # Llama a la función para mostrar el menú de compras
                    break
                else:
                    print(">>> CONTRASEÑA NO VALIDA <<<\n")
        else:
            print(">>> USUARIO NO EXISTENTE <<<\n")  # Si el usuario no existe
    elif inicio == 0:  # Salir del programa
        break
