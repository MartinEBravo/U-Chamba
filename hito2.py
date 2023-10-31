
import psycopg2
import psycopg2.extras
import csv
import re

schema = "u_chamba."
 
# Tablas de entidades
tabla_postulantes = schema + "Postulante"
tabla_universidad = schema + "Universidad"
tabla_compannia   = schema + "Compannia"
tabla_pais        = schema + "Pais"
tabla_ofertas_trabajo = schema + "OfertasTrabajo"

# Tablas de relaciones
tabla_estudia_en = schema + "Estudia_en"
tabla_postula    = schema + "Postula"
tabla_ubicado    = schema + "Ubicado"


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


# Funcion para buscar o insertar en una tabla
def findOrInsert(table, name):
    cur.execute("select id from "+ table +" where name=%s limit 1", [name]) # Buscar
    r = cur.fetchone()
    if(r):
        return r[0]
    cur.execute("insert into "+ table +" (name) values (%s) returning id", [name])
    return cur.fetchone()[0] 


with open("DataSets/estudiantes.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            #indice personas
            nombre_index      = row.index("nombre")
            sexo_index        = row.index("sexo")
            edad_index        = row.index("edad")
            rut_index         = row.index("RUT")
            correo_index      = row.index("correo")
            universidad_index = row.index("universidad")
            telefono_index    = row.index("telefono")
            sector_index      = row.index("sector")
            carrera_index     = row.index("carrera")
            anno_index        = row.index("año")
            postulacion_index = row.index("postulacion")
            empresa_index    = row.index("empresa") 
            continue


with open("DataSets/universidad.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            #indice
            universidad_index       = row.index("Universidad")
            anno_index              = row.index("Año")
            Tipo_index              = row.index("Tipo")
            Estudiantes_index       = row.index("Estudiantes")
            Rankingnacional_index   = row.index("Ranking nacional")
            Rankingmundial_index    = row.index("Ranking mundial")
            Acreditacion_index      = row.index("Acreditación (años)")
            Academicos_index        = row.index("Académicos (número)")
            Infraestructura_index   = row.index("Infraestructura (m2)") 
            Regioncasacentral_index = row.index("Región casa central")
            continue

with open("DataSets/empresas.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            name_index       = row.index("Nombre Empresa")
            direccion_index  = row.index("Dirección")
            ciudad_e_index   = row.index("Ciudad Empresa")
            pais_e_index     = row.index("País Empresa")
            Pib_index        = row.index("PIB País")
            poblacion_index  = row.index("Población País")
            Esperanza_index  = row.index("Esperanza de Vida País")
            continue


with open("DataSets/countries.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            #indice
            Country_index    = row.index("Country")
            Region_index     = row.index("Region")
            Population_index = row.index("Population")

            Area (sq. mi.)_index = row.index("Area (sq. mi.)")
            Pop. Density (per sq. mi.)_index = row.index("Pop. Density (per sq. mi.)")
            Coastline (coast/area ratio)_index = row.index("Coastline (coast/area ratio)")
            Net migration_index = row.index("Net migration")
            Infant mortality (per 1000 births)_index = row.index("Infant mortality (per 1000 births)")
            GDP ($ per capita)_index = row.index("GDP ($ per capita)")
            Literacy (%)_index = row.index("Literacy (%)")
            Phones (per 1000)_index = row.index("Phones (per 1000)")
            Arable (%)_index = row.index("Arable (%)")
            Crops (%)_index = row.index("Crops (%)")
            Other (%)_index = row.index("Other (%)")

            Climate_index     = row.index("Climate")
            Birthrate_index   = row.index("Birthrate")
            Deathrate_index   = row.index("Deathrate")
            Agriculture_index = row.index("Agriculture")
            Industry_index    = row.index("Industry")
            Service_index     = row.index("Service")
            continue

conn.commit()
conn.close()
