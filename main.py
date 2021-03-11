from flask import Flask, render_template, jsonify, request
import json
from darbs_ar_failu import nolasitDatus, ierakstitDatus
from darbs_ar_db import registret, atlasit, lietotaji

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
    dati = lietotaji()
    print(dati)
    #dati = atlasit("SELECT * FROM lietotaji WHERE loma = 'skolēns'")
    dati = jsonify(dati)
   
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
@app.route('/skolenu_sniegums/get')
def skolenu_sniegums_get():
    dati = nolasitDatus('skolens_noteikt_limeni.txt')
    return render_template('skolenu_sniegums_get.html', dati = dati)  
  #  return json.dumps(dati)
  
@app.route('/skolenu_sniegums/post')
def skolenu_sniegums_post():
    return render_template('skolenu_sniegums_post.html') 

@app.route('/skolenu_sniegums/post', methods=['POST'])
def skolenu_sniegums_post_dati():
    dati = request.json
   
    ierakstitDatus('skolens_noteikt_limeni.txt', json.dumps(dati))

    return "1"
@app.route('/skolotajs_snieguma/post')
def skolotajs_snieguma_post():
    return render_template('skolotajs_snieguma_post.html')

@app.route('/skolotajs_snieguma/post/dati', methods=['POST'])
def skolotajs_snieguma_post_dati():
    dati = request.json
   
    ierakstitDatus('skolens_noteikt_limeni.txt', json.dumps(dati))

    return "1"
@app.route('/skolotajs_snieguma/get')
def skolotajs_snieguma_get():
    dati = nolasitDatus('skolens_noteikt_limeni.txt')
    return json.dumps(dati)
  #  return render_template('skolotajs_snieguma_get.html', dati = dati) 


@app.route('/api/registracija', methods=['POST'])
def api_registracija():
    dati = request.json
    registret(dati)
    
    return "1"

    
app.run(debug=True)