from model.Objects.cita import Cita
from model.Objects.paciente import Paciente
from dbConnection.FirebaseConnection import FirebaseConnection

class PacienteDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise ConnectionError("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")
            self.pacientes_ref = self.firebase.db.collection("pacientes")

    def agendar_cita(self, cita):
        if not isinstance(cita, Cita):
            raise TypeError("El objeto proporcionado no es una instancia de Cita")
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
    
    def add_paciente(self, paciente):
        if self.pacientes_ref is None:
            print("❌ No se puede conectar a Firebase (pacientes)")
            return

        try:
            if not isinstance(paciente, Paciente):
                raise ValueError("❌ El objeto no es una instancia de Paciente")
            self.pacientes_ref.add(paciente.create_dictionary())
            print("✅ Paciente agregado correctamente")
        except Exception as e:
            print(f"❌ Error al agregar paciente: {e}")
