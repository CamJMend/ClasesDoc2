from model.Objects.enfermera import Enfermera
from dbConnection.FirebaseConnection import FirebaseConnection

class EnfermeraDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise ConnectionError("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")
            self.pacientes_ref = self.firebase.db.collection("pacientes")
            self.enfermeras_ref = self.firebase.db.collection("enfermeras")

    def actualizar_cita(self, cita_id, nuevos_datos):
        try:
            docs = self.citas_ref.where("idc", "==", cita_id).get()
            for doc in docs:
                doc.reference.update(nuevos_datos)
                print("Cita actualizada correctamente")
                return
            print("Cita no encontrada")
        except Exception as e:
            print(f"Error al actualizar cita: {e}")

    def registrar_signos_vitales(self, paciente_id, signos):
        try:
            paciente_doc = self.pacientes_ref.document(paciente_id)
            paciente_doc.update({"signos_vitales": signos})
            print("Signos vitales registrados correctamente")
        except Exception as e:
            print(f"Error al registrar signos vitales: {e}")

    def actualizar_consulta(self, cita_id, nuevos_datos):
        try:
            docs = self.citas_ref.where("idc", "==", cita_id).get()
            for doc in docs:
                doc.reference.update(nuevos_datos)
                print("Consulta actualizada correctamente")
                return
            print("Consulta no encontrada")
        except Exception as e:
            print(f"Error al actualizar consulta: {e}")

    def add_admin(self, enfermera):
        try:
            if not isinstance(enfermera, Enfermera):
                raise ValueError("❌ El objeto no es una instancia de Enfermera")
            self.pacientes_ref.add(paciente.create_dictionary())
            print("✅ Paciente agregado correctamente")
        except Exception as e:
            print(f"❌ Error al agregar paciente: {e}")