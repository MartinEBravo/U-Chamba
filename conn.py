import psycopg2
import psycopg2.extras

def get_conn():
    # Conexion a la base de datos
    return psycopg2.connect (
        host     = "cc3201.dcc.uchile.cl",
        database = "cc3201",
        user     = "cc3201",
        password = "contrasenna",
        port     = "5512"
    )
    # Cursor