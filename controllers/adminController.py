from model.DAO.adminDAO import AdminDAO

class AdminController:
    def __init__(self):
        self.admin_dao = AdminDAO()

    def actualizar_cita(self, cita_id, nuevos_datos):
        self.admin_dao.actualizar_cita(cita_id, nuevos_datos)

    def actualizar_usuario(self, usuario_id, nuevos_datos):
        self.admin_dao.actualizar_usuario(usuario_id, nuevos_datos)

    def ver_horarios_de_trabajo(self, usuario_id):
        return self.admin_dao.ver_horarios_de_trabajo(usuario_id)
