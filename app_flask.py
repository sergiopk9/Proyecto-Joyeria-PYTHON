from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import modelo.repositorio_tienda


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')
@app.route("/admin/")
def admin():
    return render_template('index-admin.html')

@app.route("/admin/listar-productos/")
def listar_productos():
    joyas=[]
    return render_template('listar-productos.html', joyas = modelo.repositorio_tienda.obtener_joyas())
@app.route("/admin/borrar-joya/<int:id>")
def borrar_joya(id):
    print(f"id borrar: {id}")
    modelo.repositorio_tienda.borrar_joya(id)
    return redirect(url_for('listar_productos'))

@app.route("/admin/registrar-joya")
def registrar_joya():
    return render_template('registrar-joya.html')

@app.route("/admin/guardar-nueva-joya")
def guardar_nueva_joya():
    nombre=request.form['nombre']
    material=request.form['material']
    tipo=request.form['tipo']
    color=request.form['color']
    diametro=request.form['diametro']
    talla=request.form['talla']
    precio=request.form['precio']
    foto = request.files["foto"]
    id_generada = modelo.repositorio_tienda.registrar_joya(nombre,material,tipo,color,diametro,talla,precio)
    
    return render_template('registrar-joya-ok.html')  

app.config['DEBUG'] = True
app.run()
