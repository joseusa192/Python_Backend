from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 

app = Flask(__name__)
conn = psycopg2.connect("dbname=python user=postgres password=******* host=localhost port=defauld")
app.secret_key = 'mysecretkey'

@app.route('/')
def home():
    conn = psycopg2.connect("dbname=python user=postgres password=******* host=localhost port=defauld")
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts_1')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', contacts_1 = data)

@app.route('/new_contact', methods=['POST'])
def new_contact():
    if request.method == 'POST':
        Nombres = request.form['Nombres']
        Apellidos = request.form['Apellidos']
        email = request.form['e-mail']
        telefono = request.form['telefono']

        conn = psycopg2.connect("dbname=python user=postgres password=******* host=localhost port=defauld")      
        cur = conn.cursor()
        query = """INSERT INTO contacts_1 (nombres, apellidos, telefono, email) VALUES (%s, %s, %s, %s)"""
        cur.execute(query,(Nombres, Apellidos, email, telefono))
        conn.commit()
        flash('Contacto Agregado Satifactoriamente')
        cur.close()
        conn.close() 
            
        return redirect(url_for('home'))
    

@app.route('/edit_contact/<string:id>')
def edit_contact(id):
    conn = psycopg2.connect("dbname=python user=postgres password=******* host=localhost port=defauld")
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts_1 WHERE id={0}'.format(id))
    data = cur.fetchall()
    return render_template('edit.html', contacts_1 = data[0])

@app.route('/update/<string:id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        Nombres = request.form['Nombres']
        Apellidos = request.form['Apellidos']
        email = request.form['e-mail']
        telefono = request.form['telefono']

        conn = psycopg2.connect("dbname=python user=postgres password=******* host=localhost port=defauld")
        cur = conn.cursor()
        cur.execute("""
        UPDATE contacts_1
        SET nombres = %s,
            apellidos = %s,
            telefono = %s,
            email = %s
        WHERE id = %s
        """, (Nombres, Apellidos, email, telefono,id))
        conn.commit()
        flash('Contacto Actualizado Satifactoriamente')
        cur.close()
        conn.close()
        return redirect(url_for('home'))

@app.route('/delete_contact/<string:id>')
def delete_contact(id):
    conn = psycopg2.connect("dbname=python user=postgres password=******* host=localhost port=defauld")
    cur = conn.cursor()
    cur.execute('DELETE FROM contacts_1 WHERE id={0}'.format(id))
    conn.commit()
    flash('Contacto Removido Satifactoriamente')
    cur.close()
    conn.close()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)



