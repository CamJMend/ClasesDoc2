class Cita:
    def __init__(self, fecha_hora, motivo, curr_status, idc, medico, paciente):
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.curr_status = curr_status
        self.idc = idc
        self.medico = medico
        self.paciente = paciente
    
    #Getters
    def get_fecha_hora(self):
        return self.fecha_hora
    
    def get_motivo(self):
        return self.motivo

    def get_curr_status(self):
        return self.curr_status

    def get_idc(self):
        return self.idc
    
    def get_medico(self):
        return self.medico

    def get_paciente(self):
        return self.paciente

    #Setters
    def set_fecha_hora(self, _fecha_hora):
        self.fecha_hora = _fecha_hora
    
    def set_motivo(self, _motivo):
        self.motivo = motivo
    
    def set_curr_status(self, _curr_status):
        self.curr_status = _curr_status

    def set_idc(self, _idc):
        self.idc = _idc
    
    def set_medico(self, _medico):
        self.medico = _medico

    def set_paciente(self, _paciente):
        self.paciente = _paciente

    def create_dictionary(self):
            return {
                "fecha_hora": self.fecha_hora,
                "motivo": self.motivo,
                "curr_status": self.curr_status,
                "idc": self.idc,
                "medico": self.medico.create_dictionary(),
                "paciente": self.paciente.create_dictionary()
            }

