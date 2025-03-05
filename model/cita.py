class Cita:
    def __init__(self, fecha_hora, motivo, curr_status, idc, medico, paciente):
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.curr_status = curr_status
        self.idc = idc
        self.medico = medico
        self.paciente = paciente
    
    #def crear_cita(self, fecha, hora, motivo):
    #def cancelar_cita(self, motivo):
    #def actualizar_cita(self, params):