from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Configurazione per il laboratorio
# Il DB vive nella VLAN 30 (o Bridge lab-db) all'indirizzo 10.10.3.10
DB_HOST = os.getenv('DB_HOST', '10.10.3.10')
DB_NAME = os.getenv('DB_NAME', 'postgres') # Database di default di Alpine Postgres
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', '') # Nessuna password di default in questo setup lab

@app.route('/')
def home():
    return """
    <h1>Benvenuti nel Laboratorio di Networking!</h1>
    <p>Questa applicazione Flask vive nella <b>DMZ (VLAN 10)</b>.</p>
    <p>Prova a testare la connessione al Database visitando <a href='/health'>/health</a>.</p>
    """

@app.route('/health')
def health():
    try:
        # Tentativo di connessione al Database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            connect_timeout=3
        )
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({
            "status": "CONNESSO",
            "message": "L'app DMZ è riuscita a parlare con il DB nascosto!",
            "db_version": db_version[0]
        })
    except Exception as e:
        return jsonify({
            "status": "ERRORE",
            "message": "Impossibile connettersi al database. Il firewall o la rete sono configurati male?",
            "error_detail": str(e)
        }), 500

if __name__ == '__main__':
    # Ascolta su tutte le interfacce sulla porta 80
    app.run(host='0.0.0.0', port=80)
