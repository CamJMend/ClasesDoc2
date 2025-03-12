import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for
from controllers.adminController import AdminController
from controllers.pacienteController import PacienteController
from controllers.medicoController import MedicoController
from controllers.enfermeraController import EnfermeraController

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    controller = AdminController()
    if request.method == 'POST':
        if 'gestionar_citas' in request.form:
            citas = controller.gestionar_citas()
            return render_template('admin.html', citas=citas)
    return render_template('admin.html')

@app.route('/paciente', methods=['GET', 'POST'])
def paciente():
    controller = PacienteController()
    if request.method == 'POST':
        if 'agendar_cita' in request.form:
            fecha = request.form['fecha']
            hora = request.form['hora']
            motivo = request.form['motivo']
            id_paciente = request.form['id_paciente']
            controller.agendar_cita(fecha, hora, motivo, id_paciente)
            return redirect(url_for('paciente'))
    return render_template('paciente.html')

@app.route('/medico', methods=['GET', 'POST'])
def medico():
    controller = MedicoController()
    if request.method == 'POST':
        if 'revisar_citas' in request.form:
            medico_id = request.form['medico_id']
            citas = controller.revisar_citas(medico_id)
            return render_template('medico.html', citas=citas)
    return render_template('medico.html')

@app.route('/enfermera', methods=['GET', 'POST'])
def enfermera():
    controller = EnfermeraController()
    if request.method == 'POST':
        if 'actualizar_estado_cita' in request.form:
            cita_id = request.form['cita_id']
            estado = request.form['estado']
            controller.actualizar_estado_cita(cita_id, estado)
            return redirect(url_for('enfermera'))
        if 'registrar_signos' in request.form:
            paciente_id = request.form['paciente_id']
            signos = request.form['signos']
            controller.registrar_signos(paciente_id, signos)
            return redirect(url_for('enfermera'))
    return render_template('enfermera.html')

if __name__ == '__main__':
    app.run(debug=True)