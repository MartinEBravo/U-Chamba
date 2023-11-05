from info_bdd import *
from conn import get_conn

def insert_regiones(regiones):
    conn = get_conn()
    cursor = conn.cursor()
    total = len(regiones)//5
    consulta = f""" insert into {tabla_region}
                    (id, nombre, pib, esperanza_vida, poblacion)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s, %s, %s) "
        if i<total-1: consulta+=", "

    cursor.execute(consulta, regiones)
    conn.commit()
    conn.close()

def insert_comunas(comunas):
    conn = get_conn()
    cursor = conn.cursor()
    total = len(comunas)//3
    consulta = f""" insert into {tabla_comuna}
                    (id, nombre, region_id)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s) "
        if i<total-1: consulta+=", "
    cursor.execute(consulta, comunas)

    conn.commit()
    conn.close()

def insert_postulantes(postulantes):
    conn = get_conn()
    cursor = conn.cursor()
    total = len(postulantes)//6
    consulta = f""" insert into {tabla_postulante}
                    (rut, nombre, telefono, email, genero, edad)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s, %s, %s, %s) "
        if i<total-1: consulta+=", "
    cursor.execute(consulta, postulantes)
    conn.commit()
    conn.close()

def insert_universidades(universidades):
    conn = get_conn()
    cursor = conn.cursor()
    total = len(universidades)//9
    consulta = f""" insert into {tabla_universidad}
                    (nombre, tipo, anho, estudiantes, acreditacion, academicos, ranking, infraestructura, region_id)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        if i<total-1: consulta+=", "
    cursor.execute(consulta, universidades)
    conn.commit()
    conn.close()

def insert_companhias(companhias):
    conn = get_conn()
    cursor = conn.cursor()
    total = len(companhias)//5
    consulta = f""" insert into {tabla_companhia}
                    (rut, nombre, registro, capital, comuna_id)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s, %s, %s) "
        if i<total-1: consulta+=", "
    cursor.execute(consulta, companhias)
    conn.commit()
    conn.close()

def insert_estudian_en(estudian_en):
    conn = get_conn()
    cursor = conn.cursor()
    total = len(estudian_en)//5
    consulta = f""" insert into {tabla_estudia_en}
                    (post_rut, uni_nombre, sector, carrera, anho)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s, %s, %s) "
        if i<total-1: consulta+=", "
    cursor.execute(consulta, estudian_en)
    conn.commit()
    conn.close()

def insert_ofertas(ofertas):
    conn = get_conn()
    cursor = conn.cursor()
    total = len(ofertas)//6
    consulta = f""" insert into {tabla_ofertas_trabajo}
                    (id, titulo, comp_rut, sueldo, modalidad, formato)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s, %s, %s, %s) "
        if i<total-1: consulta+=", "
    cursor.execute(consulta, ofertas)
    conn.commit()
    conn.close()

def insert_postulaciones(postulaciones):
    conn = get_conn()
    cursor = conn.cursor()

    total = len(postulaciones)//3
    consulta = f""" insert into {tabla_postula}
                    (oferta_id, comp_rut, post_rut)
                    values """
    for i in range(total):
        consulta += " (%s, %s, %s) "
        if i<total-1: consulta+=", "
    cursor.execute(consulta, postulaciones)

    conn.commit()
    conn.close()

#######    GET ID's    #######
def get_id_region(region):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(f"""
                    select id from {tabla_region}
                    where nombre=%s
                    """, [region])
    r = cursor.fetchone()
    conn.close()
    if r: return r[0]
    else: return None

def get_id_comuna(comuna):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(f"""
                    select id from {tabla_comuna}
                    where nombre=%s
                    """, [comuna])
    r = cursor.fetchone()
    conn.close()
    if r: return r[0]
    else: return None

def get_comunas_and_id():
    comunas = {}
    conn   = get_conn()
    cursor =  conn.cursor()
    cursor.execute(f"""
                    select id, nombre
                    from {tabla_comuna};
                    """)
    comuna = cursor.fetchone()
    while comuna:
        id_comuna, nombre_comuna = comuna
        comunas[nombre_comuna] = id_comuna
        comuna = cursor.fetchone()
    conn.close()
    return comunas