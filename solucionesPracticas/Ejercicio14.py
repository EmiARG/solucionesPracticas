# Ejercicio 14  ESTRUCTURAS DE DATOS

"""
Desarrollar en Python un módulo que gestione una agenda telefónica en un diccionario de Python utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:

Mostrar al usuario un menú de opciones

Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono). Esta opción debe agregar al diccionario a la persona que el usuario ingrese

Opción 2: Modificar una persona: dado su dni debe buscar la persona y preguntar si desea cambiar los demás campos de la persona, cambiando los que quiera.

Opción 3: Eliminar una persona del diccionario. Elimina según el DNI

Opción 4: Mostrar todos la agenda

Opción 5: Salir
"""

agenda = {}

while True:
    print("**" * 30)  
    print("Agenda telefónica")
    print("**" * 30)    
    print("1. Agregar contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")
    print("**" * 10)

    opcion = int(input("Elija una opción: "))
    
    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        dni = int(input("Ingrese su DNI: "))
        email = input("Ingrese su correo: ")
        telefono = int(input("Ingrese su número de telefono: "))

        persona = {
            "nombre" : nombre,
            "apellido" : apellido,
            "dni" : dni,
            "email" : email,
            "telefono" : telefono
        }
        agenda[dni] = persona
        print("Contacto Agendado")
    elif opcion == 2 :
        dni = input("Ingrese DNI de contacto que desee modificar: ")
        
        if dni in agenda:
            persona = agenda[dni]
            print("Datos de la persona: ")
            print(persona)
            
            modificarContacto = input("Desea editar el contacto? (si/no): ")
            
            if modificarContacto.lower() == "si":
                nombre = input("Ingrese el nuevo nombre: ")
                apellido = input("Ingrese el nuevo apellido: ")
                email = input("Ingrese el nuevo email: ")
                telefono = input("Ingrese el nuevo número de teléfono: ")
                persona["nombre"] = nombre
                persona["apellido"] = apellido
                persona["email"] = email
                persona["telefono"] = telefono

                print("Persona modificada exitosamente.")
            else:
                print("No se realizaron cambios.")
        else:
            print("No se encontró ninguna persona con ese DNI.")
    elif opcion == "3":
        dni = input("Ingrese el DNI de la persona que desea eliminar: ")

        if dni in agenda:
            del agenda[dni]
            print("Persona eliminada exitosamente.")
        else:
            print("No se encontró ninguna persona con ese DNI.")        
            
    elif opcion == 4 :
        if agenda :
            print("Agenda:")
            for dni, persona in agenda.items():
                print(f"DNI: {dni}")
                print(f"Nombre: {persona['nombre']}")
                print(f"Apellido: {persona['apellido']}")
                print(f"Email: {persona['email']}")
                print(f"Teléfono: {persona['telefono']}")
        else :
            print("La agenda no tiene contactos")
        
    elif opcion == 5 :
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")           