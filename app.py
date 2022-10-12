#_*_ coding:utf-8 _*_
    



"""
autor: Carlos Encina
fecha: 12-10-2022
Fecha de ultima edicion: 
descripción: Formulario WEB simple. 


"""


from flask import Flask, render_template, json, request
import sqlite3 as sql 

app=Flask(__name__)

nombre_db="base_datos3.db"   

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showHome')
def showHome():
    return render_template('index.html')


@app.route('/formulario')
def formulario():
    js=lista()    #llamamos a la funcion para retornar del lado del cliente datos par el formulario
    return render_template('registro.html',dato=js)

@app.route('/registro', methods=['POST','GET'])      # Ingreso de datos
def registro():
    if request.method=='POST':   
        try:
            nombre=request.form['Nombre']              
            email=request.form['email']
            ciudad=request.form['ciudad']
            datos=[nombre,email,ciudad]  # esto es para meter en la db luego
            with sql.connect(nombre_db) as con:        
                cur = con.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS registro_form (
                                        Nombre text,                                        
                                        email text,
                                        ciudad text,
                                    );'''
                       )
                cur.execute('''INSERT INTO registro_form (Nombre,email,ciudad) VALUES (?,?,?);''', datos )
            
                con.commit()   
             
        except:
            con.rollback()

        finally:
            con.close()# cerramos la conexion de la base de datos 
            js=lista()   #retornamos datos de la db para el form del lado del cliente
            return render_template('registro.html',dato=js)
            

    

@app.route('/list')
def list():
   con = sql.connect(nombre_db)   
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from registro_form")
  
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)
    



if __name__ == "__main__":
    app.run(debug=True)
