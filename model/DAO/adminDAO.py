from model.Objects.admin import Admin
from dbConnection.FirebaseConnection import FirebaseConnection

class AdminDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise ConnectionError("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")
            self.usuarios_ref = self.firebase.db.collection("usuarios")
            self.usuarios_ref = self.firebase.db.collection("admins")
            self.medicos_ref = self.firebase.db.collection("medicos")
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

    def actualizar_usuario(self, usuario_id, nuevos_datos):
        try:
            docs = self.usuarios_ref.where("id", "==", usuario_id).get()
            for doc in docs:
                doc.reference.update(nuevos_datos)
                print("Usuario actualizado correctamente")
                return
            print("Usuario no encontrado")
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")

    def ver_horarios_de_trabajo(self, usuario_id):
        """Busca los horarios en las colecciones de médicos y enfermeras."""
        try:
            horarios = []

            # Buscar en médicos
            medico_docs = self.medicos_ref.where("id", "==", usuario_id).get()
            for doc in medico_docs:
                data = doc.to_dict()
                if "horario_trabajo" in data:
                    horarios.append({"tipo": "medico", "horario_trabajo": data["horario_trabajo"]})

            # Buscar en enfermeras
            enfermera_docs = self.enfermeras_ref.where("id", "==", usuario_id).get()
            for doc in enfermera_docs:
                data = doc.to_dict()
                if "horario_trabajo" in data:
                    horarios.append({"tipo": "enfermera", "horario_trabajo": data["horario_trabajo"]})

            return horarios if horarios else "No hay horarios registrados para este usuario"
        except Exception as e:
            print(f"Error al obtener horarios: {e}")
    
    def add_admin(self, admin_usuario):
        try:
            if not isinstance(admin_usuario, Admin):
                raise ValueError("❌ El objeto no es una instancia de Adminn")
            data = admin_usuario.create_dictionary()
            data["rol"] = "admin"
            self.admins.add(data)
            print("✅ Admin agregado correctamente")
        except Exception as e:
            print(f"❌ Error al agregar admin: {e}")
