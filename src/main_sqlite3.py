import sqlite3
import os

nombre_db = "base/Revite.db"

def crear_base_de_datos():
    try:
        
        conexion = sqlite3.connect(nombre_db)

        cursor = conexion.cursor()

        cursor.execute("""
                    
                       CREATE TABLE IF NOT EXISTS usuarios (
                       
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       
                       nombre TEXT NOT NULL,
                       
                       correo TEXT UNIQUE NOT NULL,
                       
                       cedula TEXT UNIQUE NOT NULL,
                       
                       celular TEXT NOT NULL,
                       
                       fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)

        conexion.commit()
        print(f"Base de datos '{nombre_db}' y tabla 'usuarios' creadas con éxito.")

    except sqlite3.Error as e:
        print(f"Error al conectar o crear la base de datos: {e}")

    finally:
        if conexion:
            conexion.close()


def crear_tabla_reservas():
    try:
        conexion = sqlite3.connect(nombre_db)
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER NOT NULL,
                destino TEXT NOT NULL,
                horario TEXT NOT NULL,
                fecha TEXT NOT NULL,
                carro TEXT NOT NULL,
                estado TEXT DEFAULT 'Pendiente',
                       
                FOREIGN KEY (usuario_id)
                REFERENCES usuario(id)
            )
        """)

        conexion.commit()

        print("Tabla 'reservas' creada correctamente.")
    
    except sqlite3.Error as e:
        print(f"Error: {e}")
    
    finally:

        if conexion:
            conexion.close()

def insertar_usuario(nombre, correo, cedula, celular):
    
    try:
        conexion = sqlite3.connect(nombre_db)
        
        cursor = conexion.cursor()

        sql = "INSERT INTO usuarios (nombre, correo, cedula, celular) VALUES (?, ?, ?, ?)"
        
        valores = (nombre, correo, cedula, celular)
        
        cursor.execute(sql, valores)
        
        conexion.commit()
        print("Usuario insertado exitosamente.")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: el correo {correo} ya está registrado. {e}")

    
    except sqlite3.Error as e:
        print(f"Error al insertar el usuario: {e}")
    
    finally:
        if conexion:
            conexion.close()

def consultar_usuarios():
    
    try:
        
        conexion = sqlite3.connect(nombre_db)
        
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre, correo, cedula, celular, fecha_registro FROM usuarios")
        
        usuarios = cursor.fetchall()
        
        for usuario in usuarios:
            print(*usuario)

    except sqlite3.Error as e:
        print(f"Error al consultar los usuarios: {e}")
    
    finally:
        if conexion:
            conexion.close()


def insertar_reserva(usuario_id, destino, horario, fecha, carro):

    try:

        conexion = sqlite3.connect(nombre_db)

        cursor = conexion.cursor()

        sql = """
        
        INSERT INTO reservas (usuario_id, destino, horario, fecha, carro ) VALUES (?, ?, ?, ?, ?)"""

        valores = (usuario_id, destino, horario, fecha, carro)

        cursor.execute(sql, valores)

        conexion.commit()

        print("Reserva insertada correctamente. ")
    
    except sqlite3.Error as e:

        print(f"Error al insertar reserva: {e}")

    finally:
        if conexion:
            conexion.close()


if __name__ == "__main__":
    
    crear_base_de_datos()

    crear_tabla_reservas()

    insertar_usuario("Alejandro Villalobos", "alejo@example.com", "12345", "678910")
    
    insertar_usuario("Ana Cortes", "cortes@example.com", "678910", "12345")
    
    insertar_reserva(1, "Bogota", "6:00", "10-05-2026", "ABC123")
    insertar_reserva(2, "Ibague", "7:00", "11-05-2026", "DEF456")
    
    consultar_usuarios()
    

    