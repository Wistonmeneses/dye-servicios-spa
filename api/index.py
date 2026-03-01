from flask import Flask, request, jsonify

# Inicializamos la aplicación Flask
app = Flask(_name_)

# Creamos la ruta que recibirá los datos del formulario
@app.route('/api/contacto', methods=['POST'])
def recibir_contacto():
    # Recibimos los datos que envía la página web
    datos = request.json
    
    nombre = datos.get('nombre')
    telefono = datos.get('telefono')
    correo = datos.get('correo')
    mensaje = datos.get('mensaje')
    
    # Por ahora, solo imprimimos los datos en la consola del servidor
    # Más adelante, aquí agregaremos el código para que te llegue un correo real
    print(f"Nuevo mensaje de: {nombre}")
    print(f"Teléfono: {telefono} | Correo: {correo}")
    print(f"Mensaje: {mensaje}")
    
    # Le respondemos a la página web que todo salió bien
    return jsonify({
        "status": "exito",
        "mensaje": f"¡Gracias {nombre}! Hemos recibido tu solicitud. Nuestro equipo técnico te contactará pronto."
    })