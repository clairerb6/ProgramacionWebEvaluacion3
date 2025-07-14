import sqlite3

def init_db():
    conn = sqlite3.connect('registros.db')
    cursor = conn.cursor()
    # Tabla ejercicio 1
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            rut TEXT NOT NULL,
            nota1 INTEGER NOT NULL,
            nota2 INTEGER NOT NULL,
            nota3 INTEGER NOT NULL,
            asistencia INTEGER NOT NULL,
            promedio REAL NOT NULL,
            estado TEXT NOT NULL
        )
    ''')

    # Tabla ejercicio 2
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comparaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre1 TEXT,
            nombre2 TEXT,
            nombre3 TEXT,
            nombre_mayor TEXT,
            longitud INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def insertar_registro(nombre, rut, n1, n2, n3, asistencia, promedio, estado):
    conn = sqlite3.connect('registros.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO notas (nombre, rut, nota1, nota2, nota3, asistencia, promedio, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, rut, n1, n2, n3, asistencia, promedio, estado))
    conn.commit()
    conn.close()

def obtener_registros():
    conn = sqlite3.connect('registros.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notas ORDER BY id DESC')
    registros = cursor.fetchall()
    conn.close()
    return registros

def insertar_comparacion(nombre1, nombre2, nombre3, nombre_mayor, longitud):
    conn = sqlite3.connect('registros.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO comparaciones (nombre1, nombre2, nombre3, nombre_mayor, longitud)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre1, nombre2, nombre3, nombre_mayor, longitud))
    conn.commit()
    conn.close()

def obtener_comparaciones():
    conn = sqlite3.connect('registros.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comparaciones ORDER BY id DESC')
    datos = cursor.fetchall()
    conn.close()
    return datos