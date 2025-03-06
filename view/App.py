from flask import Flask, render_template, request, redirect, url_for
from controllers.con_admin import ControllerAdmin
from controllers.con_medico import ControllerMedico
from controllers.con_paciente import ControllerPaciente
from controllers.con_enfermera import ControllerEnfermera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

ADMIN_TEMPLATE = 'admin.html'

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    print("Admin route accessed")  # Debugging
    controller = ControllerAdmin()
    
    if request.method == 'POST':
        print("POST request received")  # Debugging
        if 'gestionar_citas' in request.form:
            print("Gestionar citas form submitted")  # Debugging
            citas = controller.gestionar_citas()
            print(f"Citas retrieved: {citas}")  # Debugging
            return render_template(ADMIN_TEMPLATE, citas=citas)
        
        elif 'agregar_cita' in request.form:
            print("Agregar cita form submitted")  # Debugging
            fecha = request.form['fecha']
            hora = request.form['hora']
            motivo = request.form['motivo']
            controller.agregar_cita(fecha, hora, motivo)
            return redirect(url_for('admin'))
        
        elif 'buscar_cita' in request.form:
            print("Buscar cita form submitted")  # Debugging
            cita_id = int(request.form['cita_id'])
            cita = controller.buscar_cita_por_id(cita_id)
            return render_template(ADMIN_TEMPLATE, cita=cita)
    
    return render_template(ADMIN_TEMPLATE)

@app.route('/medico', methods=['GET', 'POST'])
def medico():
    print("Medico route accessed")  # Debugging
    controller = ControllerMedico()
    
    if request.method == 'POST':
        if 'agregar_cita' in request.form:
            fecha = request.form['fecha']
            hora = request.form['hora']
            motivo = request.form['motivo']
            controller.agregar_cita(fecha, hora, motivo)
            return redirect(url_for('medico'))
        
        elif 'aceptar_cita' in request.form:
            print("Aceptar cita form submitted")  # Debugging
            cita_id = int(request.form['cita_id'])
            controller.aceptar_cita(cita_id)
            return redirect(url_for('medico'))
    
    citas = controller.obtener_citas()
    return render_template('medico.html', citas=citas)

PACIENTE_TEMPLATE = 'paciente.html'

@app.route('/paciente', methods=['GET', 'POST'])
def paciente():
    print("Paciente route accessed")  # Debugging
    controller = ControllerPaciente()
    
    if request.method == 'POST':
        if 'agendar_cita' in request.form:
            print("Agendar cita form submitted")  # Debugging
            fecha = request.form['fecha']
            hora = request.form['hora']
            motivo = request.form['motivo']
            cita = controller.agendar_cita(fecha, hora, motivo)
            return render_template(PACIENTE_TEMPLATE, cita=cita)
        
        elif 'ver_estado_cita' in request.form:
            print("Ver estado cita form submitted")  # Debugging
            cita_id = int(request.form['cita_id'])
            estado = controller.obtener_estado_cita(cita_id)
            return render_template(PACIENTE_TEMPLATE, estado=estado, cita_id=cita_id)
    
    return render_template(PACIENTE_TEMPLATE)

@app.route('/enfermera', methods=['GET', 'POST'])
def enfermera():
    print("Enfermera route accessed")  # Debugging
    controller = ControllerEnfermera()
    
    if request.method == 'POST':
        print("POST request received")  # Debugging
        if 'agregar_cita' in request.form:
            print("Agregar cita form submitted")  # Debugging
            fecha = request.form['fecha']
            hora = request.form['hora']
            motivo = request.form['motivo']
            controller.agregar_cita(fecha, hora, motivo)
            return redirect(url_for('enfermera'))
        
        elif 'actualizar_estado_cita' in request.form:
            print("Actualizar estado cita form submitted")  # Debugging
            cita_id = int(request.form['cita_id'])
            estado = request.form['estado']
            controller.actualizar_estado_cita(cita_id, estado)
            return redirect(url_for('enfermera'))
    
    citas = controller.obtener_citas()
    return render_template('enfermera.html', citas=citas)

if __name__ == '__main__':
    app.run(debug=True)