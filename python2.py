def promedio(a, b, c):
    pro = (a + b + c) / 3
    return pro

def validar_genero(genero):
    generos_validos = ["masculino", "femenino"]
    genero = genero.lower()  # convertir la entrada a minusculas
    return genero in generos_validos

print("Bienvenido a la calculadora python")
print("")

cont_masc = 0
cont_fem = 0
suma_notas_masc = 0

ca = int(input("Ingrese la cantidad de alumnos: "))
print("")
for i in range(ca):
    nom = input("Ingrese el nombre del alumno:  ")
    print("")

    print("""    masculino
    femenino""")
    genero = input("Ingrese genero del alumno (masculino o femenino):  ")

    if validar_genero(genero):
        print("Genero valido")
    else:
        print("Genero invalido, por favor ingrese uno de los siguientes: masculino, femenino  ")
        continue

    print("Ingrese notas: ")
    nota1 = float(input("NOTA 1:  "))
    nota2 = float(input("NOTA 2:  "))
    nota3 = float(input("NOTA 3:  "))

    pro = promedio(nota1, nota2,nota3)
    print(f"El promedio del alumno {nom} es {pro}") #agregue la f (f-strings) para poder incluiur las variables en la cadena de texto

    if genero == "femenino":
        cont_fem += 1 #"+=" para simpliificar "variable = variable + valor" :3
    else:
        cont_masc += 1
        suma_notas_masc += pro

print("La cantidad de mujeres es ", cont_fem)
if cont_masc > 0:
    promedio_masc = suma_notas_masc / cont_masc
    print("El promedio de los hombres es ", promedio_masc)
else:
    print("No hay hombres para calcular el promedio")
	
