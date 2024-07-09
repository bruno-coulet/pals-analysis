import mysql.connector
from dotenv import load_dotenv
import os

# Loads variables from .env to connect to database
load_dotenv()

def connect():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port= int(os.getenv('DB_PORT')),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        print(conn)

        if conn.is_connected():
            print("Connexion reussie a la base de donnees")
            return conn
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")

def close(conn):
    if conn.is_connected():
        conn.close()
        print("La connexion a la base de donnees a ete fermee")


##############################################
if __name__ == "__main__":
    conn = connect()
    close(conn)
