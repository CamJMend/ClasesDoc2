from flask import Flask, render_template, request, redirect, url_for
from vista_medico import VistaMedico
from vista_paciente import VistaPaciente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/medico')
def medico():
    vista = VistaMedico()
    opcion = vista.mostrar_menu()
    if opcion == "1":
        citas = [{'fecha': '2023-10-01', 'hora': '10:00', 'motivo': 'Consulta general', 'estado': 'Pendiente'}]
        vista.revisar_citas(citas)
    return render_template('medico.html')

@app.route('/paciente')
def paciente():
    vista = VistaPaciente()
    opcion = vista.mostrar_menu()
    if opcion == "1":
        vista.agendar_cita()
        # Here you would save the cita to the model
    return render_template('paciente.html')

if __name__ == '__main__':
    app.run(debug=True)