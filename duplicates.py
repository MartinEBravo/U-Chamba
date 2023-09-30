
import pandas as pd

estudiantes = pd.read_csv('estudiantes.csv')

# ver si hay duplicados en rut
print(estudiantes[estudiantes.duplicated(['RUT'])])
# ver si hay duplicados en correo
print(estudiantes[estudiantes.duplicated(['correo'])])

# ver en que lugares se repiten los ruts
print(estudiantes[estudiantes.duplicated(['RUT'], keep=False)])
# ver en que lugares se repiten los correos
print(estudiantes[estudiantes.duplicated(['correo'], keep=False)])