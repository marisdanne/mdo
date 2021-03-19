from flask import Flask, render_template, jsonify, request, redirect
import json
import sqlite3
from darbs_ar_failu import nolasitDatus, ierakstitDatus
from darbs_ar_db import registret, atlasit, lietotaji, pieteikties, nolasit, atlasit_lietotajus

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

@app.route('/api/v1/skoleni')
def apiskoleni():
    return atlasit_lietotajus('Skolēns')

@app.route('/api/v2/skoleni', methods=['GET'])
def v2skoleni():
    try:
      # Izveidojam savienojumu ar Datubāzi
      with sqlite3.connect("mdo.db") as conn:
        # Izveidojam kursoru
        c = conn.cursor()
        # Izsaucam datu no Inventars tabulas. DAUDZUMS paņemam kā tukšu kolonu, lai rezultātos nebūtu Undefied
        c.execute("SELECT id, vards, uzvards, klase FROM lietotaji  WHERE loma= 'Skolēns'" )
        # Ielasam datus mainīgajā
        data = c.fetchall()
        jsonData = ''
        # Kolonu nosaukumi, kādi tiks izmantoti JSON failā. Tiem ir jābūt tādā pašā secībā, kā kolonas lasām no tabulas SELECT izsaukumā
        column_names = ['id','vards','uzvards','klase']
        for row in data:
          # Savienojam kolonu nosaukums ar datiem no tabulas
          info = dict(zip(column_names, row))
          # Pa vienai rindiņai papildimām jsonData mainīgo, līdz visi dati ir nolasīti no tabulas. Aiz katra ieraksta pieliekam komatu, lai atdalītu ierakstus.
          jsonData = jsonData + json.dumps(info) + ','
        # Noņemam pēdējo lieko komatu
        jsonData = jsonData[:-1]
        # Ieliekam visus datus kvadrātiekavās
        jsonData = '[' + jsonData + ']'
        msg = "Ieraksti veiksmīgi saņemti un apstrādāti"
        print(msg)
    except:
      conn.rollback()
      msg = "Ir notikusi kļūda datu saņemšanā un apstrādāšanā"
      print(msg)
    finally:
      conn.commit()
      c.close()
      conn.close()    
      return jsonData

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
# @app.route('/skolotajs_snieguma/get')
# def skolotajs_snieguma_get():
#     dati = nolasitDatus('skolens_noteikt_limeni.txt')
#     return json.dumps(dati)
#   #  return render_template('skolotajs_snieguma_get.html', dati = dati) 


@app.route('/api/registracija', methods=['POST'])
def api_registracija():
    dati = request.json
    registret(dati)
    
    return "1"

@app.route('/skolotajs_snieguma/get')
def skolotajs_snieguma_get():
    vaicajums = "SELECT * FROM prasmes "
    dati = nolasit(vaicajums)
    return dati
    
app.run(debug=True)