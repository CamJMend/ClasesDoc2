from model.Objects.cita import Cita
from dbConnection.FirebaseConnection import FirebaseConnection

class AddCitaDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise Exception("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")

    def agregar_cita(self, cita):
        if self.citas_ref is None:
            print("Error de conexión a la base de datos")
            return
        try:
            if not isinstance(cita, Cita):
                raise Exception("El objeto no es una cita")
            self.citas_ref.add(cita.create_dictionary())
            print("Cita agregada correctamente")
        except Exception as e:
            print(f"Error al agregar cita: {e}")

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
            cita_ref = self.citas_ref.document(cita_id)
            cita_ref.update({"estado": estado})
            print(f"Estado de la cita {cita_id} actualizado a {estado}.")
            return True
        except Exception as e:
            print(f"Error al actualizar estado de la cita: {e}")
            return False