from model.Objects.cita import Cita

class Admin:
    def __init__(self):
        self.citas = [
            Cita(id=1, fecha="2023-10-01", hora="10:00", motivo="Consulta general", estado="Pendiente"),
            Cita(id=2, fecha="2023-10-02", hora="11:00", motivo="Revisión", estado="Aceptada")
        ]
        print("Admin model initialized with sample data")  # Debugging

    def agregar_cita(self, cita):
        if isinstance(cita, Cita):
            self.citas.append(cita)
            print(f"Cita added: {cita.__dict__}")  # Debugging
            return True
        return False

    def obtener_citas(self):
        print("Fetching all citas")  # Debugging
        return self.citas
    
    def buscar_cita_por_id(self, cita_id):
        for cita in self.citas:
            if cita.id == cita_id:
                return cita
        return None