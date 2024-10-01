#Realizar un programa que solucione lo siguiente:
#problematica VENTA DE FRUTAS Y VERDURAS
#Ingrese por teclado la cantidad de ventas a realizar

#cada venta debe registrar
#Nombre del vendedor
#Apellido del vendedor
#Nombre del cliente
#Apellido del cliente
#Cantidad que va a comprar el usuario (en kgs)
#fruta quue va a comprar el usuario
#Precio de la fruta o verdura (en pesos chilenos, por kilo)
#Con cuanto pago el cliente
#Funcion: calcular total a pagar 
#funcion: calcular vuelto
#funcion: calcular nombre completo

def calcular_total_a_pagar(cant, precio):
    return cant * precio

def calcular_vuelto(pago, total):
    if total<pago:
        result=pago-total    
        return result
    elif pago-total==0:
        result="0"
        return result
    else:
        print("DInero insuficiente")
    
def calcular_nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

ventas=[]

print("Bienvenido a distribuidora  x")
print("")

#datos:

n=int(input("Ingrese cuantas ventas realizara: "))
print("")
for i in range(n):
    print(f"Venta {i + 1}:")

    v_name=input("Ingrese nombre del vendedor: ") 
    print("")
    v_lastname=input("Ingrese apellido del vendedor: ") 
    print("")
    client_name=input("Ingrese noombre del cliente: ") 
    print("")
    client_lastname=input("Ingrese apellido del cliente: ") 
    print("")
    cant=float(input("Ingrese cantidad en kilogramos: "))
    print("")
    fruta=input("Ingrese fruta o verdura que comprara: ")
    print("")
    precio=float(input("Ingrese precio del producto: "))
    print("")
    pago=float(input("Ingrese con cuanto pago el cliente: "))

    total_a_pagar = calcular_total_a_pagar(cant, precio)
    vuelto = calcular_vuelto(pago, total_a_pagar)

    venta = {
        "client_name": client_name,
        "client_lastname": client_lastname,
        "total_a_pagar": total_a_pagar,
        "vuelto": vuelto
    }
    ventas.append(venta)
    print("")

#mostrar datos :3
for i, venta in enumerate(ventas):
    nombre_completo_cliente = calcular_nombre_completo(venta["client_name"], venta["client_lastname"])
    
    print(f"Venta {i + 1}:")
    print(f"Nombre del vendedor: {nombre_completo_cliente}")
    print(f"Total a pagar: ${venta["total_a_pagar"]}")
    print(f"Vuelto: ${venta["vuelto"]}")
    print("")