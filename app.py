from flask import Flask, render_template, request, redirect, url_for, session
from modelos import db, Discos

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_segura'

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/productos')
def vista_productos():
    discos = Discos.query.all()
    return render_template('productos.html', discos=discos)

@app.route('/disco', methods=['GET', 'POST'])
def agg_disco():
    producto = Discos.query.all()
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        artista = request.form.get('artista')
        precio = request.form.get('precio')
        imagen_url = request.form.get('imagen_url')
        disco = Discos(nombre=nombre, artista=artista, precio=precio, imagen_url=imagen_url)
        db.session.add(disco)
        db.session.commit()
        return redirect('productos')
    return render_template('disco.html')

@app.route('/eliminar/<id>')
def eliminar(id):
    disco = Discos.query.get(id)
    db.session.delete(disco)
    db.session.commit()
    return redirect(url_for('vista_productos'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    disco = Discos.query.get_or_404(id)
    if request.method == 'POST':
        disco.nombre = request.form['nombre']
        disco.artista = request.form['artista']
        disco.precio = request.form['precio']
        disco.imagen_url = request.form['imagen_url']
        db.session.commit()
        if 'carrito' in session:
            for item in session['carrito']:
                if item['id'] == id:
                    item['nombre'] = disco.nombre
                    item['artista'] = disco.artista
                    item['precio'] = disco.precio
                    item['imagen_url'] = disco.imagen_url
            session.modified = True
        return redirect(url_for('vista_productos'))
    return render_template('editar.html', disco=disco)

@app.route('/carrito')
def ver_carrito():
    total = sum(item['precio'] * item['cantidad'] for item in session.get('carrito', []))
    return render_template('carrito.html', carrito=session.get('carrito', []), total=total)

@app.route('/compra')
def compra():
    return render_template('compra.html')

@app.route('/add_carrito/<int:id>')
def add_carrito(id):
    if 'carrito' not in session:
        session['carrito'] = []
    disco = Discos.query.get(id)
    if not disco:
        return redirect(url_for('vista_productos'))
    item_existente = None
    for item in session['carrito']:
        if item['id'] == id:
            item_existente = item
            break
    if item_existente:
        item_existente['cantidad'] += 1
    else:
        session['carrito'].append({
            'id': disco.id,
            'nombre': disco.nombre,
            'artista': disco.artista,
            'precio': disco.precio,
            'imagen_url': disco.imagen_url,
            'cantidad': 1
        })
    session.modified = True
    return redirect(url_for('ver_carrito'))

@app.route('/eliminar_del_carrito/<int:id>')
def eliminar_del_carrito(id):
    if 'carrito' in session and session['carrito']:
        for item in session['carrito']:
            if item['id'] == id:
                if item['cantidad'] > 1:
                    item['cantidad'] -= 1
                else:
                    session['carrito'] = [item for item in session['carrito'] if item['id'] != id]
                break
        session.modified = True
    return redirect(url_for('ver_carrito'))

@app.template_filter('format_price_pt')
def format_price_pt(value):
    formatted_price = "{:,.0f}".format(value)
    return formatted_price.replace(',', '.')

if __name__ == '__main__':
    app.run(debug=True)