from model.usuario import Usuario

class Paciente(Usuario):
    def __init__(self, id, nombre, fecha_nacimiento):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def agendar_cita(self, fecha_hora, motivo, medico_id):
        conn = Conexion().conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO citas (fecha_hora, motivo, curr_status, medico_id, paciente_id) VALUES (?, ?, ?, ?, ?)",
            (fecha_hora, motivo, "pendiente", medico_id, self.id)
        )
        conn.commit()
        conn.close()
        return "Cita agendada correctamente"

    def cancelar_cita(self, idc):
        conn = Conexion().conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE citas SET curr_status = 'cancelada' WHERE id = ? AND paciente_id = ?",
            (idc, self.id)
        )
        conn.commit()
        conn.close()
        return "Cita cancelada correctamente"