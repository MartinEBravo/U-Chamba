import pandas as pd
import random 

nombres_hombre = [
    "Juan", "Pedro", "Carlos", "Manuel", "Luis", "Andrés", "Jorge", "Felipe", "Fernando", "Miguel",
    "Gonzalo", "Rodrigo", "Pablo", "Hernán", "Sebastián", "Cristián", "Eduardo", "José", "Alejandro", "Raúl",
    "Roberto", "Ricardo", "Francisco", "Javier", "Mario", "Antonio", "Nicolás", "Patricio", "Álvaro", "Diego",
    "Guillermo", "René", "Claudio", "Daniel", "Héctor", "Víctor", "Feliciano", "Félix", "Hugo", "Alberto",
    "Sergio", "Emilio", "Renato", "Ernesto", "Maximiliano", "Iván", "Marco", "Rafael", "César", "Julio",
    "Armando", "Camilo", "Eugenio", "Federico", "Joaquín", "Leonardo", "Luciano", "Marcelo", "Nelson", "Oscar",
    "Pascual", "Ramón", "Rubén", "Simón", "Tobías", "Ulises", "Xavier", "Yerko", "Zenón", "Adolfo",
    "Benjamín", "Clemente", "Dante", "Elias", "Flavio", "Gaspar", "Homero", "Ignacio", "Jacinto", "Kelvin",
    "Leandro", "Mauricio", "Nemesio", "Osvaldo", "Pedro", "Quintín", "Rafael", "Salvador", "Teobaldo", "Urbano",
    "Valentín", "Waldo", "Ximeno", "Yago", "Zaqueo"
]

nombres_mujer = [
    "Ana", "María", "Isabel", "Sofía", "Carmen", "Luisa", "Andrea", "Fernanda", "Carolina", "Valentina",
    "Javiera", "Camila", "Antonia", "Paula", "Elena", "Claudia", "Alejandra", "Rocío", "Pilar", "Daniela",
    "Verónica", "Mónica", "Rosa", "Valeria", "Victoria", "Natalia", "Lucía", "Margarita", "Francisca", "Bárbara",
    "Gabriela", "Valeria", "Natalia", "Laura", "Isabella", "Romina", "Ignacia", "Josefina", "Constanza", "Gabriela",
    "Francisca", "Beatriz", "Marcela", "Adriana", "Raquel", "Pamela", "Eugenia", "Ximena", "Tatiana", "Renata",
    "Ximena", "Catalina", "Valerie", "Antonella", "Paulina", "Pía", "Sara", "Emilia", "Lorena", "Marjorie",
    "Cecilia", "Rita", "Ruth", "Gloria", "Susana", "Eva", "Nora", "Celia", "Alicia", "Elisa", "Diana",
    "Teresa", "Yolanda", "Violeta", "Patricia", "Magdalena", "Montserrat", "Cristina", "Elena", "Olga", "Rocio",
    "Ángela", "Yasna", "Ivonne", "Mónica", "Claudia", "Marisol", "Ingrid", "Lourdes", "Vanessa", "Wendy", "Luz",
    "Renata", "Delfina", "Emiliana", "Valerie", "Belen", "Mireya", "Julieta", "Camelia", "Ximena"
]


apellidos = [
    "González", "Rodríguez", "Martínez", "López", "Pérez", "Fernández", "Gómez", "Díaz", "Hernández", "Silva",
    "Torres", "Vargas", "Ramírez", "Rojas", "Morales", "Soto", "Romero", "Álvarez", "Vásquez", "Reyes",
    "Araya", "Espinoza", "Cabrera", "Flores", "Gutiérrez", "Muñoz", "Ortiz", "Castro", "Núñez", "Ávila",
    "Figueroa", "Mendoza", "Poblete", "Vergara", "Jiménez", "Carvajal", "Valenzuela", "Ríos", "Suárez", "Lara",
    "Fuentes", "Orellana", "Sanchez", "Peña", "Pizarro", "Leiva", "Herrera", "Lagos", "Aguilera", "Bravo",
    "Escobar", "Cáceres", "Sandoval", "Carrasco", "Salazar", "Osorio", "Navarro", "Santos", "Villanueva", "Arancibia",
    "Garrido", "Ovalle", "Bustos", "Mora", "Valdés", "Donoso", "Sepúlveda", "Moreno", "Tapia", "Lara", "Pavez",
    "Vidal", "Cisternas", "Montes", "Palma", "Venegas", "Sáez", "Valencia", "Toro", "Cortés", "Riquelme", "Cuevas",
    "Barrios", "Catalán", "Ibarra", "Quinteros", "Ortega", "Rivas", "Medina", "Campos", "Guzmán", "Villalobos",
    "Fariña", "Baeza", "Lillo", "Oyarzún", "Toledo", "Calderón", "Avendaño", "Aravena", "Contreras", "Cádiz"
]


universidades_chilenas = [
    "Pontificia Universidad Católica de Chile",
    "Universidad de Chile",
    "Universidad de Concepción",
    "Universidad de Santiago de Chile",
    "Universidad Técnica Federico Santa María",
    "Universidad Adolfo Ibáñez",
    "Universidad Diego Portales",
    "Universidad Austral de Chile",
    "Universidad de Valparaíso",
    "Universidad de La Serena"
]

correos_universidades = {
    "Pontificia Universidad Católica de Chile": "puc.cl",
    "Universidad de Chile": "ug.uchile.cl",
    "Universidad de Concepción": "udec.cl",
    "Universidad de Santiago de Chile": "usach.cl",
    "Universidad Técnica Federico Santa María": "utfsm.cl",
    "Universidad Adolfo Ibáñez": "uai.cl",
    "Universidad Diego Portales": "udp.cl",
    "Universidad Austral de Chile": "ua.cl",
    "Universidad de Valparaíso": "uv.cl",
    "Universidad de La Serena": "userena.cl"
}

indice = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'K']

sectores_de_estudios = {
    "Ciencias de la Salud": ["Medicina", "Enfermería", "Odontología", "Kinesiología"],
    "Ciencias Sociales y Humanidades": ["Psicología", "Derecho", "Trabajo Social", "Sociología"],
    "Ingeniería y Tecnología": [
        "Ingeniería Civil",
        "Ingeniería Civil en Computación",
        "Ingeniería Civil Industrial",
        "Ingeniería Civil Eléctrica",
        "Ingeniería Civil Mecánica",
    ],
    "Ciencias Naturales": ["Biología", "Química", "Física", "Geología"],
    "Arte y Diseño": ["Arquitectura", "Diseño Gráfico", "Arte Digital"],
    "Educación": ["Pedagogía en Educación Básica", "Pedagogía en Educación Parvularia", "Pedagogía en Historia"],
}

estudiantes = pd.DataFrame(columns=['nombre', 'sexo', 'edad', 'RUT', 'correo' , 'universidad'])
for i in range(10000):

    # Selección del Nombre y Sexo
    genero = random.randint(0, 2)
    if genero > 0:
        nombre = random.choice(nombres_hombre)
        nombre2 = random.choice(nombres_hombre)
        sexo = 'Hombre'
    else:
        nombre = random.choice(nombres_mujer)
        nombre2 = random.choice(nombres_mujer)
        sexo = 'Mujer'
    apellido = random.choice(apellidos)
    apellido2 = random.choice(apellidos)

    nombre_completo = nombre + ' ' + nombre2 + ', ' + apellido + ' ' + apellido2
   
    # Selección de la edad
    edad = random.randint(18, 30)

    # Selección de la universidad
    u = random.randint(0, 100)
    if u < 20:
        universidad = 'Universidad de Chile'
    elif u < 40:
        universidad = 'Pontificia Universidad Católica de Chile'
    elif u < 50:
        universidad = 'Universidad de Concepción'
    else:
        universidad = random.choice(universidades_chilenas)

    # Creación del Correo
    correo = nombre.lower() + '.' + apellido.lower() + '@' + correos_universidades[universidad].lower()

    # creación del RUT
    if edad < 20:
        rut = '2' + str(random.randint(0,1)) + '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '-' + random.choice(indice)
    elif edad < 24:
        rut = '20' + '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '-' + random.choice(indice)
    elif edad < 28:
        rut = '19'+ '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '-' + random.choice(indice)
    else:
        rut = '1' + str(random.randint(8,9)) + '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '.' + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + '-' + random.choice(indice)

    estudiantes.loc[i] = [nombre_completo, sexo,edad,rut,correo,universidad]


estudiantes.to_csv('estudiantes.csv', index=False)

