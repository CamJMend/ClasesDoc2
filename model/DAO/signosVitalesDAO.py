from dbConnection.FirebaseConnection import FirebaseConnection
from google.cloud import firestore

class SignosVitalesDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise Exception("Error de conexión a la base de datos")
        else:
            self.signos_ref = self.firebase.db.collection("signos_vitales")

    def agregar_signos(self, paciente_id, signos):
        try:
            self.signos_ref.add({
                "paciente_id": paciente_id,
                "signos": signos,
                "fecha": firestore.SERVER_TIMESTAMP
            })
            print("Signos vitales registrados correctamente.")
            return True
        except Exception as e:
            print(f"Error al registrar signos vitales: {e}")
            return False