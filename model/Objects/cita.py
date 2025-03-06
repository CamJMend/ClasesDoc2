

class Cita:
    def __init__(self, id, fecha, hora, motivo, estado='Pendiente'):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.curr_status = curr_status
        self.idc = idc
        self.medico = medico
        self.paciente = paciente
    
    #def crear_cita(self, fecha, hora, motivo):
    #def cancelar_cita(self, motivo):
    #def actualizar_cita(self, params):
    def create_dictionary(self):
            return {
                "fecha_hora": self.fecha_hora,
                "motivo": self.motivo,
                "curr_status": self.curr_status,
                "idc": self.idc,
                "medico": self.medico.create_dictionary(),
                "paciente": self.paciente.create_dictionary()
            }

