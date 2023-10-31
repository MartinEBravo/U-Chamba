
import psycopg2
import psycopg2.extras
import csv
import re

schemma = "u_chamba."
 
# Tablas de entidades

# Tablas de relaciones


# Conexion a la base de datos
conn = psycopg2.connect (
    host     = "cc3201.dcc.uchile.cl",
    database = "cc3201",
    user     = "cc3201",
    password = "j'<3_cc3201",
    port     = "5440"
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



with open("DataSets/estudiantes.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            #indices

            

            continue





conn.commit()
conn.close()
