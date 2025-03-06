from model.Objects.cita import Cita

class Medico:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita):
        if isinstance(cita, Cita):
            self.citas.append(cita)
            return True
        return False

    def obtener_citas(self):
        return self.citas

    def aceptar_cita(self, cita_id):
        for cita in self.citas:
            if cita.id == cita_id:
                cita.estado = 'Aceptada'
                return True
        return False