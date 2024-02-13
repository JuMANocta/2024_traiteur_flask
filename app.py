from flask import Flask, request, jsonify
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connexion():
    try:
        connexion = mysql.connector.connect(**DB_CONFIG)
        print("Connexion BDD réussie")
        return connexion
    except mysql.connector.Error as e:
        print(f"Erreur de connexion BDD : {e}")
        return None

@app.route('/api/clients', methods=['GET'])
def get_clients():
    connexion = get_db_connexion()
    if connexion is not None:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM client")
        clients = cursor.fetchall()
        cursor.close()
        connexion.close()
        return jsonify(clients)
    else:
        return jsonify([])

app.run(debug=True, port=5000)