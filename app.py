from flask import Flask, jsonify, send_from_directory
import mysql.connector
import os
from mysql.connector import Error
from flask_cors import CORS


app = Flask(__name__)

CORS(app)
# Configuración de la base de datos usando variables de entorno
db_config = {
    'host': os.getenv('DB_HOST', 'db'),
    'user': os.getenv('DB_USER', 'user'),
    'password': os.getenv('DB_PASSWORD', 'password'),
    'database': os.getenv('DB_NAME', 'paises')
}


def get_db_connection():
    """Establece una conexión con la base de datos."""
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None


@app.route('/countries', methods=['GET'])
def get_countries():
    """Endpoint para obtener todos los países y sus habitantes."""
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "Error de conexión a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM countries")
        countries = cursor.fetchall()
        print(f"Se encontraron {len(countries)} registros.")
        cursor.close()
    except Error as e:
        return jsonify({"error": f"Error al ejecutar la consulta: {e}"}), 500
    finally:
        connection.close()

    return jsonify(countries)


@app.route('/')
def serve_index():
    """Sirve el archivo index.html del frontend."""
    return send_from_directory('frontend', 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
