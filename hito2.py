import psycopg2
import psycopg2.extras
import csv
import re
from unidecode import unidecode
from insert import *

# Conexion a la base de datos
conn = psycopg2.connect (
    host     = "cc3201.dcc.uchile.cl",
    database = "cc3201",
    user     = "cc3201",
    password = "contrasenna",
    port     = "5512"
)
# Cursor
cur = conn.cursor()

# para limpiar
def to_ascii(s: str):
    return unidecode(s.replace("ñ","nh")).strip()

#################################################
### Solo para ahorrar un poco de trabajo
## Borra todas las tablas
cur.execute("DROP SCHEMA uchamba CASCADE;")
## Crear todas las tablas
cur.execute("CREATE SCHEMA uchamba;")
with open("bdd.sql", "r") as consultas: 
    cur.execute(to_ascii(consultas.read()))
##################################################

########## Region ##########
with open("DataSets/regiones.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(reader):
        if i==0:
            id_index      = row.index("Reg")
            nombre_index  = row.index("Descripción series")
            PIB_index     = row.index("2022")
            desocupacion_index = row.index("Desocupacion")
            continue
        id_reg  = to_ascii(row[id_index])
        nombre  = to_ascii(row[nombre_index]).lower()
        pib     = int(float(row[PIB_index].replace(",","")))
        desocupacion = int(float(row[desocupacion_index]))
        print(id_reg, nombre, pib, desocupacion)
        insertRegion(cur, id_reg, nombre, pib, desocupacion)

########## Comuna ##########
with open("DataSets/comunas.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            id_index        = row.index("ID")
            nombre_index    = row.index("Nombre")
            id_region_index = row.index("ID Region")
            continue
        id_com  = to_ascii(row[id_index])
        nombre  = to_ascii(row[nombre_index]).lower()
        id_reg  = to_ascii(row[id_region_index])
        insertComuna(cur, id_com, nombre, id_reg)


########## Postulante ##########
with open("DataSets/estudiantes.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            #indice personas
            correo_index      = row.index("correo")
            rut_index         = row.index("RUT")
            telefono_index    = row.index("telefono")
            nombre_index      = row.index("nombre")
            sexo_index        = row.index("sexo")
            edad_index        = row.index("edad")

            continue
        if i>100: break
        correo   = to_ascii(row[correo_index])
        rut      = to_ascii(row[rut_index])
        telefono = to_ascii(row[telefono_index])
        nombre   = to_ascii(row[nombre_index])
        genero   = to_ascii(row[sexo_index])
        edad     = to_ascii(row[edad_index])
        insertPostulante(cur, rut, nombre, telefono, correo, genero, edad)



########## Universidad ##########
########## Ubicacion_Universidad ##########
with open("DataSets/universidad.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            Tipo_index              = row.index("Tipo")
            universidad_index       = row.index("Universidad")
            Regioncasacentral_index = row.index("Región casa central")
            Acreditacion_index      = row.index("Acreditación (años)")
            Academicos_index        = row.index("Académicos (número)")
            Rankingnacional_index   = row.index("Ranking nacional")
            Rankingmundial_index    = row.index("Ranking mundial")
            Infraestructura_index   = row.index("Infraestructura (m2)") 
            Estudiantes_index       = row.index("Estudiantes")
            anho_index              = row.index("Año")
            continue

        universidad     = to_ascii(row[universidad_index])
        tipo            = to_ascii(row[Tipo_index])
        anho            = to_ascii(row[anho_index])
        estudiantes     = to_ascii(row[Estudiantes_index])
        acreditacion    = to_ascii(row[Acreditacion_index]) 
        academicos      = to_ascii(row[Academicos_index]) 
        ranking         = to_ascii(row[Rankingnacional_index]) 
        infraestructura = to_ascii(row[Infraestructura_index])

        region_id       = get_id_region(cur, to_ascii(row[Regioncasacentral_index]).lower())

        if region_id:
            insertUniversidad(cur, universidad, tipo, anho, estudiantes, acreditacion, academicos, ranking, infraestructura)
            insertUbicacionUniversidad(cur, universidad, region_id)


########## Companhia ##########
########## Ubicado ##########
with open("DataSets/companhias.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            rut_index     = row.index("RUT")
            nombre_index  = row.index("Razon Social")
            comuna_index  = row.index("Comuna Social")
            registr_index = row.index("Fecha de registro (ultima firma)")
            capital_index = row.index("Capital")
            continue

        if i>100: break
        rut      = to_ascii(row[rut_index])
        rut      = f"{rut[:2]}.{rut[2:5]}.{rut[5:10]}"
        nombre   = to_ascii(row[nombre_index])
        registro = to_ascii(row[registr_index])
        capital  = to_ascii(row[capital_index])
        comuna   = get_id_comuna(cur, to_ascii(row[comuna_index]).lower().strip())
        if comuna:
            insertCompanhia(cur, rut, nombre, registro, capital)
            insert_Ubicacion_Companhia(cur, rut, comuna)


########## Estudia_en ##########
with open("DataSets/estudiantes.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            rut_index         = row.index("RUT")
            universidad_index = row.index("universidad")

            sector_index      = row.index("sector")
            carrera_index     = row.index("carrera")
            anho_index        = row.index("año")        
            continue

        if i>100: break
        rut         = to_ascii(row[rut_index])
        universidad = to_ascii(row[universidad_index])
        sector      = to_ascii(row[sector_index])
        carrera     = to_ascii(row[carrera_index])
        anho        = to_ascii(row[anho_index])

        insert_Estudia_en(cur, rut, universidad, sector, carrera, anho)


########## Ofertas ##########



########## Postula ##########



conn.commit()
conn.close()