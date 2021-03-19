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
        print (loma)
        if loma == "Skolotājs":
            return redirect('/izvelneskolotajs')
        elif loma == "Skolēns":
            return redirect('/izvelneskolens')
        else:
            return render_template('login.html')




    #salt = 'm@d@o'
#    parole = "skola"
   
#    parole_hash = hashlib.md5(bytes(parole, 'utf-8'))
#    parole_encode = parole_hash.hexdigest()
#    paroles_ievads = input('Ievadi paroli: ')
#    paroles_ievads_hash = hashlib.md5(bytes(paroles_ievads, 'utf-8'))
#    print(paroles_ievads_hash)
#    paroles_ievads_encode = paroles_ievads_hash.hexdigest()
#    print(paroles_ievads_encode)
#    if parole_encode == paroles_ievads_encode:
#       print("Parole ievadīta pareizi")
#    else:
#      print("Parole ievadīta nepareizi")
#    return "0"
 

    

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

@app.route('/prasmes')
def prasmes():
    return render_template('prasmes.html')

@app.route('/prasmes', methods=['POST'])
def prasmes_post():
    return pievienot_prasmi(request.json)

@app.route('/api/v1/prasmes')
def prasmes_api():
    return atlasit_prasmes()
    
app.run(debug=True)