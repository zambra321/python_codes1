def promedio(a, b, c):
    return (a + b + c) / 3

def validar_edad():
    edad=0
    edad = int(input("Ingrese edad el alumno: "))
    if 10 <= edad <20:
        return edad
    else:
        print("La edad debe ser entre 10 y 20 años")
def validar_nota():
    nota=0
    nota = int(input("Ingrese nota el alumno: "))
    if 1 <= nota <=7:
        return nota
    else:
        print("La nota debe ser entre 1 y 7 años")

print("Bienvenido")

print("DATOS ALUMNO 1")
nombre1 = input("Ingrese nombre del alumno ")
edad1 = validar_edad()
nota1 = validar_nota()
mesada1 = int(input("Ingrese mesada del alumno "))

print("DATOS ALUMNO 2")
nombre2 = input("Ingrese nombre del alumno ")
edad2 = validar_edad()
nota2 = validar_nota()
mesada2 = int(input("Ingrese mesada del alumno "))

print("DATOS ALUMNO 3")
nombre3 = input("Ingrese nombre del alumno ")
edad3 = validar_edad()
nota3 = validar_nota()
mesada3 = int(input("Ingrese mesada del alumno "))

#ca lculos

prom_e = promedio (edad1,edad2,edad3)
prom_n = promedio(nota1,nota2,nota3)
prom_m = promedio(mesada1,mesada2,mesada3)
#resultados
print(f"El promedio de las edades de los 3 alumnos es: {prom_e} ")
print(f"El promedio de las notas de los 3 alumnos es: {prom_n}")
print(f"El promedio de las mesadas es de: {prom_m}")
	
