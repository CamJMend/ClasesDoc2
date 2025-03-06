from model.Objects.cita import Cita

class Enfermera:
    def __init__(self):
        self.citas = []  # This will store Cita objects

    def agregar_cita(self, cita):
        if isinstance(cita, Cita):  # Ensure the input is a Cita object
            self.citas.append(cita)
            return True
        return False

    def actualizar_estado_cita(self, cita_id, estado):
        for cita in self.citas:
            if cita.id == cita_id:
                cita.estado = estado
                return True
        return False