# pip install mysql-connector
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import random
import string
import sqlite3

from sqlalchemy import null

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random string for production
bootstrap = Bootstrap(app)

database_path = "courier.db"

@app.route('/')
def index():
    # return ("abc")
    conn=sqlite3.connect(database_path) 
    data=conn.execute("SELECT * FROM pkg ")
    for n in data:
     return render_template('index.html',n=n)

@app.route('/track', methods=['POST'])
def track():
    tracking_id = request.form['tracking_id']
    conn=sqlite3.connect(database_path) 
    data=conn.execute("SELECT * FROM pkg WHERE id=?",(tracking_id,))
    for n in data:
     return render_template('tracking_result.html',n=n)
    return redirect(url_for('index'))


@app.route('/create_shipment', methods=['GET', 'POST'])
def create_shipment():
    if request.method == 'POST':
        tracking_id = ''.join(random.choices( string.digits, k=6))
        status = request.form['status']
        location = request.form['location']
        eta = request.form['eta']
        # Sqllite Connection   
        conn=sqlite3.connect(database_path) 
        c = conn.cursor()
        c.execute('INSERT INTO pkg (id,status,location,eta) VALUES (?,?,?,?)',(tracking_id,status,location,eta))
        conn.commit()
        #sqllite Connection End
        flash('Shipment created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_shipment.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
       abc = request.form['track_id']
       conn=sqlite3.connect(database_path) 
       data=conn.execute("SELECT * FROM pkg WHERE id=?",(abc,))
    for n in data:
         return render_template('update.html',n=n)
       
    return render_template('update.html')

@app.route('/update_shipment', methods=['GET','POST'])
def update_shipment():
   if request.method == 'POST':
        tracking_id = request.form['id']
        status = request.form['status']
        location = request.form['location']
        eta = request.form['eta']
        # Sqllite Connection   
        conn=sqlite3.connect(database_path) 
        c = conn.cursor()
        c.execute('update pkg set  status = ? , location = ? , eta = ?  where id = ?',
                  (status,location,eta,tracking_id))
        conn.commit()
        flash("Record successfully Added")
   return render_template('index.html')

@app.route('/delete', methods=['GET','POST'])
def delete():
   if request.method == 'POST':
        delete_id = request.form['delete_id']
        
        # Sqllite Connection   
        conn=sqlite3.connect(database_path) 
        c = conn.cursor()
        c.execute('DELETE FROM pkg where id = ?',
                  (delete_id,))
        conn.commit()
        flash("Record successfully Added")
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
