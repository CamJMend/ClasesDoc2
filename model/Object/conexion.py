import sqlite3

class Conexion:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
    
    def conectar(self):
        return sqlite3.connect(self.db_name)
    
    def crear_tablas(self):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT,
                                fecha_nacimiento TEXT,
                                role TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS citas (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                fecha_hora TEXT,
                                motivo TEXT,
                                curr_status TEXT,
                                medico_id INTEGER,
                                paciente_id INTEGER)''')
            conn.commit()
