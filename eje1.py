notas={
    "Gomez":[],
    "Perez":[],
    "Martinez":[],
    "Fischer":[],
    "Iglesias":[]
}

while True:
    print("Menú")
    menu={
        1:"Ver notas",
        2:"Ver notas por alumnos",
        3:"Cargar notas",
        4:"Promedio",
        5:"Salir"
    }
    for key, values in menu.items():
        print(key, ":", values)
    op=int(input("Ingrese el número de la opción que desea:"))
    if op == 1:
        print("Notas de los alumnos:")
        for key, values in notas.items():
            print(key, ":", values)
    if op ==2:
        print("Notas por alumnos")
        alumno=input("Ingrese el apellido del alumno :")
        for alumno in notas.values():
            print("Las notas son:",alumno)
    if op ==3:
        print("Cargar notas")
        alumno=input("Ingrese el apellido del alumno")
        if alumno in notas.items():
            for nota in range(5):
                nota=int("Ingrese la nota del alumno:")
                notas[alumno].append(nota)
        else:
            print("El alumno no esta cargado")
    if op==4:
        print("Promedios")
        nom=input("Ingrese el apellido del alumno:")
        for nom in notas.values():
            suma=0
            for notas in values:
                suma = suma + notas
                prom=suma/5
                print("El promedio del alumno es:",prom)
    if op ==5:
        print("Gracias por fijarse en las notas")
        print("Nico aprobame")
        break
