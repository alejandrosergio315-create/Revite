import sqlite3
import os


os.makedirs("base", exist_ok=True)


nombre_db = "base/Revite.db"



def conectar():
    return sqlite3.connect(nombre_db)


def crear_base_de_datos():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT UNIQUE NOT NULL,
                cedula TEXT UNIQUE NOT NULL,
                celular TEXT NOT NULL,
                password TEXT NOT NULL,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conexion.commit()
        print("✅ Tabla usuarios creada correctamente")

    except sqlite3.Error as e:
        print(f"❌ Error: {e}")

    finally:
        conexion.close()


def crear_tabla_reservas():
    try:
        conexion = conectar()
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
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        """)

        conexion.commit()
        print("✅ Tabla reservas creada correctamente")

    except sqlite3.Error as e:
        print(f"❌ Error: {e}")

    finally:
        conexion.close()


def insertar_usuario(nombre, correo, cedula, celular, password):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, cedula, celular, password) VALUES (?, ?, ?, ?, ?)",
            (nombre, correo, cedula, celular, password)
        )

        conexion.commit()
        print("✅ Usuario registrado correctamente")

    except sqlite3.IntegrityError:
        print("❌ Usuario ya existe (correo o cédula duplicada)")

    finally:
        conexion.close()

def buscar_usuario_cedula(cedula):
    conexion = sqlite3.connect(nombre_db)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM usuarios
        WHERE cedula = ?
    """, (cedula,))

    usuario = cursor.fetchone()
    conexion.close()

    return usuario

def login_usuario(cedula, password):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE cedula = ? AND password = ?
    """, (cedula, password))

    usuario = cursor.fetchone()
    conexion.close()

    return usuario



def consultar_usuarios():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre, correo, cedula, celular FROM usuarios")

        for usuario in cursor.fetchall():
            print(usuario)

    finally:
        conexion.close()



def insertar_reserva(usuario_id, destino, horario, fecha, carro):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO reservas (usuario_id, destino, horario, fecha, carro)
            VALUES (?, ?, ?, ?, ?)
        """, (usuario_id, destino, horario, fecha, carro))

        conexion.commit()
        print("✅ Reserva creada")

    finally:
        conexion.close()



def actualizar_reserva(id_reserva, destino, horario, fecha, carro):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE reservas
            SET destino = ?, horario = ?, fecha = ?, carro = ?
            WHERE id = ?
        """, (destino, horario, fecha, carro, id_reserva))

        conexion.commit()
        print("✅ Reserva actualizada")

    finally:
        conexion.close()



def eliminar_reserva(id_reserva):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM reservas WHERE id = ?", (id_reserva,))

    conexion.commit()
    conexion.close()



def actualizar_usuario(cedula, nombre, celular):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE usuarios
        SET nombre = ?, celular = ?
        WHERE cedula = ?
    """, (nombre, celular, cedula))

    conexion.commit()
    conexion.close()



def obtener_reservas_usuario(usuario_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, destino, horario, fecha, carro, estado
        FROM reservas
        WHERE usuario_id = ?
    """, (usuario_id,))

    reservas = cursor.fetchall()
    conexion.close()

    return reservas

def crear_tabla_carros():

    conexion = sqlite3.connect(nombre_db)

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carros(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            placa TEXT NOT NULL,

            marca TEXT NOT NULL,

            modelo TEXT NOT NULL,

            ciudad TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()

def insertar_carro(
    placa,
    marca,
    modelo,
    ciudad
):

    conexion = sqlite3.connect(nombre_db)

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO carros(
            placa,
            marca,
            modelo,
            ciudad
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            placa,
            marca,
            modelo,
            ciudad
        )
    )

    conexion.commit()
    conexion.close()

def obtener_reservas():

    conexion = sqlite3.connect(nombre_db)

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM reservas
    """)

    reservas = cursor.fetchall()

    conexion.close()

    return reservas

def confirmar_reserva(id_reserva):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE reservas
        SET estado = 'Confirmada'
        WHERE id = ?
    """, (id_reserva,))

    conexion.commit()
    conexion.close()

def crear_tabla_conductores():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conductores(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            cedula TEXT UNIQUE NOT NULL,

            celular TEXT NOT NULL,

            placa TEXT,
            
            ciudad TEXT NOT NULL,

            password TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()

def insertar_conductor(
    nombre,
    cedula,
    celular,
    placa,
    ciudad,
    password
):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO conductores(
            nombre,
            cedula,
            celular,
            placa,
            ciudad,
            password
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        nombre,
        cedula,
        celular,
        placa,
        ciudad,
        password
    ))

    conexion.commit()
    conexion.close()

def login_conductor(
    cedula,
    password
):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM conductores
        WHERE cedula = ?
        AND password = ?
    """,
    (
        cedula,
        password
    ))

    conductor = cursor.fetchone()

    conexion.close()

    return conductor

def obtener_reservas_ciudad(ciudad):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM reservas
        WHERE destino = ?
    """, (ciudad,))

    reservas = cursor.fetchall()

    conexion.close()

    return reservas

def buscar_conductor(cedula):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM conductores
        WHERE cedula = ?
    """, (cedula,))

    conductor = cursor.fetchone()

    conexion.close()

    return conductor

def obtener_carros_por_ciudad(ciudad):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT placa
        FROM carros
        WHERE ciudad = ?
    """, (ciudad,))

    carros = cursor.fetchall()

    conexion.close()

    return carros


if __name__ == "__main__":

    crear_base_de_datos()
    crear_tabla_reservas()

    # 🔥 Usuarios con contraseña
    insertar_usuario("Alejandro", "alejo@test.com", "1234", "300123", "1234")

    usuario = login_usuario("1234", "1234")

    insertar_conductor(
        "Carlos Perez",
        "123456",
        "3001111111",
        "ABC123",
        "Bogota",
        "1234"
    )

    if usuario:
        print("✅ Login correcto:", usuario)
    else:
        print("❌ Login incorrecto")

    

    