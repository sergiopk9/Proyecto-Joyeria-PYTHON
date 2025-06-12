# Aqui vamos a centralizar las operaciones 
# con bases de datos de la tienda
# import modelo.repositorio_tienda
import modelo.conexion

def obtener_joyas():
    conexion = modelo.conexion.conectar()
    sql = "select * from joyas order by id desc"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)  # Se agregó la ejecución de la consulta
    joyas = cur.fetchall()
    conexion.close()  # Se cierra la conexión
    return joyas
    
def borrar_joya(id):
    conexion = modelo.conexion.conectar()
    sql = "delete from joyas where id = %s"
    cur = conexion.cursor()
    # para crear una tupla en python de dos elementos seria asi: ("uno","dos")
    # para crear una tupla de un elemento es asi: ("uno",)
    cur.execute(sql, (id,) )
    conexion.commit()
    cur.close()
    conexion.close()

def registrar_joya(nombre,material,tipo,color,diametro,talla,precio,foto):
    conexion = modelo.conexion.conectar()
    sql = "insert into joyas (nombre,material,tipo,color,diametro,talla,precio,foto) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cur = conexion.cursor()
    cur.execute(sql, (nombre,material,tipo,color,diametro,talla,precio,foto))
    conexion.commit()
    cur.close()
    conexion.close()
    return cur.lastrowid 