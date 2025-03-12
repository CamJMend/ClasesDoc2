from model.Objects.medico import Medico
from dbConnection.FirebaseConnection import FirebaseConnection

class MedicoDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise ConnectionError("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")
            self.medicos_ref = self.firebase.db.collection("medicos") 


    def aceptar_cita(self, cita_id):
        try:
            docs = self.citas_ref.where("idc", "==", cita_id).get()
            for doc in docs:
                doc.reference.update({"curr_status": "aceptada"})
                print("Cita aceptada correctamente")
                return
            print("Cita no encontrada")
        except Exception as e:
            print(f"Error al aceptar cita: {e}")

    def ver_citas_agendadas(self, medico_id):
        try:
            docs = self.citas_ref.where("medico", "==", medico_id).get()
            citas = [doc.to_dict() for doc in docs]
            return citas if citas else "No hay citas agendadas"
        except Exception as e:
            print(f"Error al obtener citas: {e}")

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
    
    def add_medico(self, medico):
        if self.medicos_ref is None:
            print("❌ No se puede conectar a Firebase (medicos)")
            return

        try:
            if not isinstance(medico, Medico):
                raise ValueError("❌ El objeto no es una instancia de Medico")
            self.medicos_ref.add(medico.create_dictionary())
            print("✅ Médico agregado correctamente")
        except Exception as e:
            print(f"❌ Error al agregar médico: {e}")
