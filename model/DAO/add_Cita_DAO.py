from model.Object.Cita import Cita
from dbConnection.FirebaseConnection import FirebaseConnection

class AddCitaDAO:
    def __init__(self):
        self.firebase = FirebaseConnection()
        if not self.firebase.db:
            raise ConnectionError("Error de conexión a la base de datos")
        else:
            self.citas_ref = self.firebase.db.collection("citas")
    def add_cita(self, cita):
        if self.citas_ref is None:
            print("Error de conexión a la base de datos")
            return
        try:
            if not isinstance(cita, Cita):
                raise TypeError("El objeto proporcionado no es una instancia de Cita")
            self.citas_ref.add(cita.create_dictionary())
            print("added")
        except Exception as e:
            print(f"Error al agregar cita: {e}")
            return
        
# Using the class
add_cita_dao = AddCitaDAO()
cita = Cita("2021-10-10 10:00", "Consulta general", "pendiente", "idc", "idm", "idp")
add_cita_dao.add_cita(cita)
        