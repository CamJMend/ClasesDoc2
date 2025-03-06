from model.Objects.admin import Admin
from model.Objects.UsuarioModel import UsuarioModel

class ControllerAdmin:
    def __init__(self):
        self.modelo = Admin()
        self.usuario_model = UsuarioModel()

    def autenticar_admin(self, nombre, contrasena):
        usuario = self.usuario_model.autenticar_usuario(nombre, contrasena)
        if usuario and usuario.rol == "Admin":
            return True
        return False

    def gestionar_citas(self):
        print("Fetching citas from Admin model")  # Debugging
        citas = self.modelo.obtener_citas()
        print(f"Citas fetched: {citas}")  # Debugging
        return citas

    def agregar_cita(self, fecha, hora, motivo):
        nueva_cita = {
            'id': len(self.modelo.obtener_citas()) + 1,
            'fecha': fecha,
            'hora': hora,
            'motivo': motivo,
            'estado': 'Pendiente'
        }
        return self.modelo.agregar_cita(nueva_cita)

    def buscar_cita_por_id(self, cita_id):
        return self.modelo.buscar_cita_por_id(cita_id)