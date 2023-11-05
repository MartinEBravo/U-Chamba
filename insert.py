from info_bdd import *

# Funcion para buscar o insertar en una tabla
def findOrInsert(cur, table, name):
    cur.execute("select id from "+ table +" where name=%s limit 1", [name]) # Buscar
    r = cur.fetchone()
    if(r):
        return r[0]
    cur.execute("insert into "+ table +" (name) values (%s) returning id", [name])
    return cur.fetchone()[0] 

def insertRegion(cur, id_reg, nombre, pib, esperanza_vida):
    cur.execute(" select id from"+tabla_region+
                " where id=%s limit 1;",
                [id_reg])
    r = cur.fetchone()
    if not r:
        cur.execute(" insert into"+tabla_region+
                    " (id, nombre, pib, esperanza_vida)"+
                    " values (%s,%s,%s,%s)",
                    [id_reg, nombre, pib, esperanza_vida])
    elif esperanza_vida:
        cur.execute(" update"+tabla_region+
                    " set esperanza_vida=%s"+
                    " where nombre=%s;",
                    [esperanza_vida, nombre])

def insertComuna(cur, id_com, nombre, id_reg):
    cur.execute(" insert into"+tabla_comuna+
                " (id, nombre, region_id)"+
                " values (%s,%s,%s)",
                [id_com, nombre, id_reg])

def insertPostulante(cur, rut, nombre, tel, email, genero, edad):
    cur.execute(" insert into"+tabla_postulantes+
                " (rut, nombre, telefono, email, genero, edad)"+
                " values (%s, %s, %s, %s, %s, %s)",
                [rut, nombre, tel, email, genero, edad])

def insertUniversidad(cur, nombre, tipo, anho, estudiantes, acreditacion, academicos, ranking, infraestructura, region_id):
    cur.execute(f"""
                insert into {tabla_universidad}
                (nombre, tipo, anho, estudiantes, acreditacion, academicos, ranking, infraestructura, region_id)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                [nombre, tipo, anho, estudiantes, acreditacion, academicos, ranking, infraestructura, region_id])

def insertCompanhia(cur, rut, nombre, registro, capital, comuna_id):
    cur.execute(f"""
                insert into {tabla_companhia}
                (rut, nombre, registro, capital, comuna_id)
                values (%s, %s, %s, %s, %s);
                """, [rut, nombre, registro, capital, comuna_id])

def insert_Estudia_en(cur, rut, univerdidad, sector, carrera, anho):
    cur.execute(" insert into"+tabla_estudia_en+
                " (post_rut, uni_nombre, sector, carrera, anho)"+
                " values (%s, %s, %s, %s, %s)",
                [rut, univerdidad, sector, carrera, anho])

def get_id_region(cur, region):
    cur.execute(" select id from"+tabla_region+
                " where nombre like %s",
                ['%'+region+'%'])
    r = cur.fetchone()
    if r: return r[0]
    else: None

def get_id_comuna(cur, comuna):
    cur.execute(" select id from"+tabla_comuna+
                " where nombre=%s",
                [comuna])
    r = cur.fetchone()
    if r: return r[0]
    else: return None

def insert_oferta(cur, id_oferta, titulo, rut, sueldo, modalidad, formato):
    cur.execute(f"""
                select rut from {tabla_companhia} 
                where rut=%s limit 1;
                """,[rut])
    r = cur.fetchone()
    if r:
        cur.execute(f"""
                insert into {tabla_ofertas_trabajo}
                (id, titulo, comp_rut, sueldo, modalidad, formato)
                values (%s, %s, %s, %s, %s, %s)
                """, [id_oferta, titulo, rut, sueldo, modalidad, formato])

def insert_postulacion(cur, id_oferta, rut_comp, rut_post):
    cur.execute(f"""
                select rut from {tabla_companhia} 
                where rut=%s limit 1;
                """,[rut_comp])
    r = cur.fetchone()
    if r:
        cur.execute(f"""
                insert into {tabla_postula}
                (oferta_id, comp_rut, post_rut)
                values (%s, %s, %s)
                """, [id_oferta, rut_comp, rut_post])