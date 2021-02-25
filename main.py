from flask import Flask, render_template, jsonify, request
import json
from darbs_ar_failu import nolasitDatus, ierakstitDatus

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registracija')
def users():
    return render_template('registracija.html')

@app.route('/skoleni')
def skoleni():
    return render_template('admin_skolenu_saraksts.html')

@app.route('/api/skoleni')
def apiskoleni():
    dati = nolasitDatus('skoleni.txt')
    #dati = jsonify(dati)
    #print(dati)
    return dati

@app.route('/skolotaji')
def skolotaji():
    return render_template('admin_skolotaju_saraksts.html')

@app.route('/maris')
def maris():
    return "<h1>Tu atradi Māri!!!!!!</h1>"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/izvelneskolens')
def izvelneskolens():
    return render_template ('izvelne_skolens.html')

@app.route('/izvelneskolotajs')
def izvelneskolotajs():
    return render_template('izvelne_skolotajs.html')


@app.route('/skolens')
def skolens():
    return render_template('skolens_noteikt_limeni.html')


@app.route('/skolotajs_snieguma_apraksts')
def skolotajs_snieguma_apraksts():
    return render_template('skolotajs_snieguma_apraksts.html')


@app.route('/maris/test/get')
def maris_test_get():
    dati = nolasitDatus('maris.txt')
    return json.dumps(dati)

@app.route('/maris/test/post')
def maris_test_post():
    return render_template('maris_test_post.html') 

@app.route('/maris/test/post/dati', methods=['POST'])
def maris_test_post_dati():
    dati = request.json
    
    ierakstitDatus('maris.txt', json.dumps(dati))

    return "1"

app.run(debug=True)