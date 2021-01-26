from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/above')
def above():
    return render_template('admin_lietotajs_saraksts.html')

@app.route('/pan')
def pan():
    return render_template('admin_skolenu_saraksts.html')

@app.route('/lot')
def lot():
    return render_template('admin_skolotaju_saraksts.html')

@app.route('/maris')
def maris():
    return "<h1>Tu atradi Māri!!!!!!</h1>"

@app.route('/login')
def login():
    return "Šeit būs login lapa!"
@app.route('/skolens')
def skolens():
    return render_template('skolens_noteikt_limeni.html')


app.run(debug=True)
