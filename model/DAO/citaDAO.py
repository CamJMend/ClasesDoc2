from model.Objects.cita import Cita
from dbConnection.FirebaseConnection import FirebaseConnection
import uuid
class AddCitaDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise ConnectionError("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")

    def agregar_cita(self, fecha, hora, motivo, id_paciente):
        try:
            cita = Cita(
                id_cita = str(uuid.uuid4()),
                fecha=fecha,
                hora=hora,
                motivo=motivo,
                estado='Pendiente',
                id_paciente=id_paciente,
                id_medico=None,
            )
            self.citas_ref.add(cita.create_dictionary())
            print("Cita agregada correctamente")
            return True
        except Exception as e:
            print(f"Error al agregar cita: {e}")
            return False

    def obtener_todas_citas(self):
        try:
            citas = self.citas_ref.stream()
            return [cita.to_dict() for cita in citas]
        except Exception as e:
            print(f"Error al obtener citas: {e}")
            return []
    
    def obtener_citas_por_medico(self, medico_id):
        try:
            citas = self.citas_ref.where("id_medico", "==", medico_id).stream()
            return [cita.to_dict() for cita in citas]
        except Exception as e:
            print(f"Error al obtener citas por médico: {e}")
            return []
    
    def actualizar_estado(self, cita_id, estado):
        try:
            # Query documents where the "id_cita" field equals the provided cita_id
            query = self.citas_ref.where("id_cita", "==", cita_id).stream()
            updated = False
            for doc in query:
                # Update each matching document
                self.citas_ref.document(doc.id).update({"estado": estado})
                updated = True
                print(f"Estado de la cita con id_cita {cita_id} actualizado a {estado}.")
            if not updated:
                print(f"No se encontró ninguna cita con id_cita {cita_id}.")
            return updated
        except Exception as e:
            print(f"Error al actualizar estado de la cita: {e}")
            return False