from flask import Flask, render_template, request
from data import Employe
app=Flask(__name__)
getemploye = Employe()
@app.route('/employe')
def emp():
    return render_template('employe.html',myemployelist=getemploye)

@app.route('/')
def index():
    return render_template('home.html')    

if(__name__=='__main__'):
    app.run(debug=True)