from flask import Flask, render_template, jsonify, request, redirect
import json
import sqlite3
from darbs_ar_failu import nolasitDatus, ierakstitDatus
from darbs_ar_db import registret, atlasit, lietotaji, pieteikties, atlasit_lietotajus, atlasit_prasmes, pievienot_prasmi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registracija')
def users():
    return render_template('registracija.html')

@app.route('/api/registracija', methods=['POST'])
def api_registracija():
    dati = request.json
    registret(dati)
    
    return "1"

@app.route('/skoleni')
def skoleni():
    return render_template('admin_skolenu_saraksts.html')

@app.route('/api/v1/skoleni')
def apiskoleni():
    return atlasit_lietotajus('Skolēns')

@app.route('/skolotaji')
def skolotaji():
    return render_template('admin_skolotaju_saraksts.html')

@app.route('/api/v1/skolotaji')
def api_skolotaji():
    return atlasit_lietotajus('Skolotājs')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        lietotajvards = request.form.get('lietotajvards')
        parole = request.form.get('parole')
        loma = pieteikties(lietotajvards, parole)
        if loma == "Skolotājs":
            return redirect('/izvelneskolotajs')
        elif loma == "Skolēns":
            return redirect('/izvelneskolens')
        else:
            return render_template('login.html')

@app.route('/izvelneskolens')
def izvelneskolens():
    return render_template ('izvelne_skolens.html')

@app.route('/izvelneskolotajs')
def izvelneskolotajs():
    return render_template('izvelne_skolotajs.html')


@app.route('/prasmju_limenis')
def prasmju_limenis():
    return render_template('prasmju_limenis.html')

@app.route('/prasmes')
def prasmes():
    return render_template('prasmes.html')

@app.route('/prasmes', methods=['POST'])
def prasmes_post():
    return pievienot_prasmi(request.json)

@app.route('/api/v1/prasmes/<id>')
def prasmes_api(id):
    return atlasit_prasmes(id)
    
app.run(debug=True)