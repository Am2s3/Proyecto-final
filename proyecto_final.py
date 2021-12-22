alumnos = []

id_counter = 1

menu = """
Que desea hacer?: 
1-Añadir
2-Listar
3-Eliminar 
4-Editar
5-Salir
"""
menu_edit = """
Qué deseas editar?
1-Nombre
2-Calificaciones
3-Editar todo
"""

user_input = input(menu)

while True:
    
    if user_input == "1":
        
        name = input("Cómo se llama el alumno?: ")
        while True: 
            
            grades = input("Cúales son las calificaciónes del aluno? Indíquelas separadas por una coma: ")

            grades_list = grades.split(",")
            
            grades_list_n = []
        
            for grade in grades_list:
                if grade.isdigit(): 
                    grade_number = int(grade)
                    grades_list_n.append(grade_number)
                else:
                    print(f"{grade} no es una clasificación válida!")
                    break
            else:
                break    
        
        average = sum(grades_list_n) / len(grades_list_n)   
        
        alumno = {
            "id": id_counter,
            "name": name ,
            "grades": grades_list_n ,
            "average": round(average, 2)
        }

        
        alumnos.append(alumno)

        id_counter += 1
    
    elif user_input == "2":

        if len(alumnos) <= 0:
            print("No hay alumnos en la base de datos")
        else:
            
            for alumno in alumnos:
                text = """
id: {0}
name: {1}
grades: {2}
average: {3}
                """
                print(text.format(alumno["id"], alumno["name"], alumno["grades"], alumno["average"]))

    
    elif user_input == "3":
        
        if len(alumnos) <= 0:
            print("No hay alumnos en la base de datos")
        else:
            
            alumno_id = input("Que alumno desea elminar?, Indique el id del alumno: ")
            
            alumno_index = None
            
            for index, alumno in enumerate(alumnos):
               
                if alumno["id"] == int(alumno_id):
                    print("Encontré el alumno")
                    
                    alumno_index = index
                    break

            if alumno_index == None:
                print("El alumno no existe en la base de datos")
            else:
                print("Eliminando alumno...") 
                
                a = alumnos.pop(alumno_index)
                print(f"El alumno {a['name']} fué eliminado") 
    
    
    elif user_input == "4": 
        
        if len(alumnos) <= 0:
            print("No hay alumnos en la base de datos")
        else:
            
            alumno_id = input("Qué alumno desea editar? Indique el id del alumno: ")
            
            alumno_index = None

            for index, alumno in enumerate(alumnos):
                if alumno["id"] == int(alumno_id):
                    print("Encontré el alumno")
                    alumno_index = index
                    break
            
            if alumno_index == None:
                print("El alumno no existe en la base de datos")
            else:
                user_edit = input(menu_edit)

                if user_edit == "1":
                    new_name = input("Qué nombre deseas poner?: ")
                    
                    alumnos[alumno_index]["name"] = new_name
                 
                elif user_edit == "2":
                    while True:    
                    
                        new_grades = input("Qué calificaciones desea poner? Separar por una coma: ")
                        
                        grades_list = new_grades.split(",")
                        
                        grades_list_n = []

                        for grade in grades_list:
                            if grade.isdigit():
                                grade_number = int(grade)
                                grades_list_n.append(grade_number)
                            else:
                                print(f"{grade} no es una calificación válida! ")
                                break
                        else:
                            break        
                    
                    alumnos[alumno_index]["grades"] = grades_list_n

                    average = sum(grades_list_n)/ len(grades_list_n)
                    alumnos[alumno_index]["average"] = round(average, 2)    
                    print(alumnos[alumno_index])

               
                elif user_edit == "3":
                    new_name = input("Qué nombre deseas poner?: ")
                    alumnos[alumno_index]["name"] = new_name
                    while True:
                        new_grades = input("Qué calificaciones desea poner?: ")
                        grades_list = new_grades.split(",")
                        grades_list_n = []
                        for grade in grades_list:
                            if grade.isdigit():
                                grade_number = int(grade)
                                grades_list_n.append(grade_number)
                            else:
                                print(f"{grade} no es una calificación válida! ")
                                break 
                        else:
                            break       
                    
                    alumnos[alumno_index]["grades"] = grades_list_n
                    average = sum(grades_list_n)/ len(grades_list_n)
                    alumnos[alumno_index]["average"] = round(average, 2)
                    print(alumnos[alumno_index])

    
    elif user_input == "5":
        user_exit = input("Estás seguro que quieres salir? (Y/N)")

        if user_exit in ["Y", "y"]:
            print("El programa está terminando. Hasta la próxima!")
            break

    user_input = input(menu) 

