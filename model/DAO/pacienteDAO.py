from model.Objects.cita import Cita
from dbConnection.FirebaseConnection import FirebaseConnection

class PacienteDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise Exception("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")

    def agendar_cita(self, cita):
        if not isinstance(cita, Cita):
            raise ValueError("El objeto debe ser una instancia de Cita")
        try:
            self.citas_ref.add(cita.create_dictionary())
            print("Cita agendada correctamente")
        except Exception as e:
            print(f"Error al agendar cita: {e}")

    def cancelar_cita(self, cita_id):
        try:
            docs = self.citas_ref.where("idc", "==", cita_id).get()
            for doc in docs:
                doc.reference.delete()
                print("Cita cancelada correctamente")
                return
            print("Cita no encontrada")
        except Exception as e:
            print(f"Error al cancelar cita: {e}")
