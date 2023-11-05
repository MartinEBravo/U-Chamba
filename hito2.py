import csv
from unidecode import unidecode
from consultas import *
from conn import get_conn

# para limpiar
def to_ascii(s: str):
    return unidecode(s.replace("ñ","nh")).strip()


conn = get_conn()
cur  = conn.cursor()
#################################################
### Solo para ahorrar un poco de trabajo
## Borra todas las tablas
cur.execute("DROP SCHEMA uchamba CASCADE;")
## Crear todas las tablas
cur.execute("CREATE SCHEMA uchamba;")
with open("bdd.sql", "r") as consultas: 
    cur.execute(to_ascii(consultas.read()))
##################################################
conn.commit()
conn.close()

########## Region ##########
print("########## Region ##########")
with open("DataSets/regiones.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    regiones = []
    for i, row in enumerate(reader):
        if i==0:
            id_index      = row.index("Reg")
            nombre_index  = row.index("Descripción series")
            PIB_index     = row.index("2022")
            desocupacion_index = row.index("Desocupacion")
            poblacion_index = row.index("Poblacion")
            continue
        id_reg  = to_ascii(row[id_index])
        nombre  = to_ascii(row[nombre_index]).lower()
        pib     = int(float(row[PIB_index].replace(",","")))
        desocupacion = int(float(row[desocupacion_index]))
        poblacion = int(row[poblacion_index].replace(".",""))

        regiones += [id_reg, nombre, pib, desocupacion, poblacion]

    insert_regiones(regiones)

########## Comuna ##########
print("########## Comuna ##########")
with open("DataSets/comunas.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    comunas = []
    for i, row in enumerate(reader):
        if i==0:
            id_index        = row.index("ID")
            nombre_index    = row.index("Nombre")
            id_region_index = row.index("ID Region")
            continue
        id_com  = to_ascii(row[id_index])
        nombre  = to_ascii(row[nombre_index]).lower()
        id_reg  = to_ascii(row[id_region_index])

        comunas += [id_com, nombre, id_reg]


    insert_comunas(comunas)



########## Postulante ##########
print("########## Postulante ##########")
with open("DataSets/estudiantes.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    postulantes = []
    for i, row in enumerate(reader):
        if i==0:
            correo_index      = row.index("correo")
            rut_index         = row.index("RUT")
            telefono_index    = row.index("telefono")
            nombre_index      = row.index("nombre")
            sexo_index        = row.index("sexo")
            edad_index        = row.index("edad")
            continue

        correo   = to_ascii(row[correo_index])
        rut      = to_ascii(row[rut_index])
        telefono = to_ascii(row[telefono_index])
        nombre   = to_ascii(row[nombre_index])
        genero   = to_ascii(row[sexo_index])
        edad     = to_ascii(row[edad_index])

        if i%25_000 == 0:
            insert_postulantes(postulantes)
            postulantes = []

        postulantes += [rut, nombre, telefono, correo, genero, edad]

    insert_postulantes(postulantes)



########## Universidad ##########
########## Ubicacion_Universidad ##########
print("########## Universidad y Ubi ##########")
with open("DataSets/universidad.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    universidades = []
    for i, row in enumerate(reader):
        if i==0:
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
        region_id       = get_id_region(to_ascii(row[Regioncasacentral_index]).lower())

        if i%25_000 == 0:
            insert_universidades(universidades)
            universidades = []

        universidades += [universidad, tipo, anho, estudiantes, acreditacion, academicos, ranking, infraestructura, region_id]
    insert_universidades(universidades)


comunas = get_comunas_and_id()
rut_companhias = []
########## Companhia ##########
########## Ubicado ##########
print("########## Companhia y Ubi ##########")
with open("DataSets/companhias.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    companhias=[]
    for i, row in enumerate(reader):
        if i==0:
            rut_index     = row.index("RUT")
            nombre_index  = row.index("Razon Social")
            comuna_index  = row.index("Comuna Social")
            registr_index = row.index("Fecha de registro (ultima firma)")
            capital_index = row.index("Capital")
            continue
        rut      = to_ascii(row[rut_index])
        rut      = f"{rut[:2]}.{rut[2:5]}.{rut[5:10]}"
        nombre   = to_ascii(row[nombre_index])
        registro = to_ascii(row[registr_index])
        registro = registro if registro[2]=="-" else None
        capital = to_ascii(row[capital_index])
        capital = int(capital) if capital.isdigit() else None
        comuna  = to_ascii(row[comuna_index]).lower()
        if comuna not in comunas: continue
        rut_companhias += [rut]
        comuna_id = comunas[comuna]

        if i%25_000 == 0:
            insert_companhias(companhias)
            companhias = []

        companhias += [rut, nombre, registro, capital, comuna_id]
    insert_companhias(companhias)



########## Estudia_en ##########
print("########## Estudia_en ##########") 
with open("DataSets/estudiantes.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    estudian_en = []
    for i, row in enumerate(reader):
        if i==0:
            rut_index         = row.index("RUT")
            universidad_index = row.index("universidad")
            sector_index      = row.index("sector")
            carrera_index     = row.index("carrera")
            anho_index        = row.index("año")        
            continue
        rut         = to_ascii(row[rut_index])
        universidad = to_ascii(row[universidad_index])
        sector      = to_ascii(row[sector_index])
        carrera     = to_ascii(row[carrera_index])
        anho        = to_ascii(row[anho_index])

        if i%25_000 == 0:
            insert_estudian_en(estudian_en)
            estudian_en = []

        estudian_en += [rut, universidad, sector, carrera, anho]
    insert_estudian_en(estudian_en)


########## Ofertas ##########
print("########## Ofertas ##########")
with open("DataSets/ofertas.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    ofertas = []
    for i, row in enumerate(reader):
        if i==0:
            id_index        = row.index("ID")
            titulo_index    = row.index("titulo practica")
            rut_index       = row.index("RUT Companhia")
            sueldo_index    = row.index("sueldo")
            modalidad_index = row.index("modalidad")
            formato_index   = row.index("formato")
            continue
        id_oferta = row[id_index]
        titulo    = to_ascii(row[titulo_index])
        rut       = row[rut_index]
        rut       = f"{rut[:2]}.{rut[2:5]}.{rut[5:10]}"
        sueldo    = row[sueldo_index]
        modalidad = to_ascii(row[modalidad_index])
        formato   = to_ascii(row[formato_index])
        if rut not in rut_companhias: continue

        if i%25_000 == 0:
            insert_ofertas(ofertas)
            ofertas = []

        ofertas += [id_oferta, titulo, rut, sueldo, modalidad, formato]
    insert_ofertas(ofertas)


########## Postula ##########
print("########## Postula ##########")
with open("DataSets/postulaciones.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    postulaciones = []
    for i, row in enumerate(reader):
        if i==0:
            id_index        = row.index("ID oferta")
            rut_comp_index  = row.index("Rut compañia")
            rut_post_index  = row.index("Rut postulante")
            continue
        id_oferta = row[id_index]
        rut_comp  = row[rut_comp_index]
        rut_comp  = f"{rut_comp[:2]}.{rut_comp[2:5]}.{rut_comp[5:10]}"
        rut_post  = row[rut_post_index]
        if rut_comp not in rut_companhias: continue

        if i%25_000 == 0:
            insert_postulaciones(postulaciones)
            postulaciones = []

        postulaciones += [id_oferta, rut_comp, rut_post]
    insert_postulaciones(postulaciones)