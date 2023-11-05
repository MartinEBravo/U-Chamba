import psycopg2
import psycopg2.extras

def get_conn():
    contrasenna = open("secret/contrasenna.txt", "r").read()
    return psycopg2.connect (
        host     = "cc3201.dcc.uchile.cl",
        database = "cc3201",
        user     = "cc3201",
        password = contrasenna,
        port     = "5512"
    )

if __name__=="__main__":
    try:
        conn = get_conn()
        cursor = conn.cursor()
        conn.close()
    except:
        print("Error al intentar conexión con el servidor...")