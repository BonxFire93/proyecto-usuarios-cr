from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="esquema_usuario"
    )


@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario")
    lista_usuarios = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("listar_usuarios.html", usuarios=lista_usuarios)


@app.route("/crear")
def crear_usuario_form():
    return render_template("crear_usuario.html")


@app.route("/crear")
def crear_usuario():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]
    edad = request.form["edad"]

    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO usuarios (nombre, apellido, correo, edad) VALUES ('%s', '%s', '%s', '%s')" % (
        nombre, apellido, email, edad
    )
    cursor.execute(query)
    conn.close()
    cursor.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=500)
