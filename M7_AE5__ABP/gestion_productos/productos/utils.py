from django.db import connection

def llamar_procedimiento_baratos():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos_baratos")
        filas = cursor.fetchall()
    return filas