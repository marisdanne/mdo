from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

    @app.route('/')
def home():
    return render_template('admin_lietotajs_saraksts.html')

    @app.route('/')
def home():
    return render_template('admin_skolenu_saraksts.html')

    @app.route('/')
def home():
    return render_template('admin_skolotaju_saraksts.html')

@app.route('/maris')
def maris():
    return "<h1>Tu atradi Māri!!!!!!</h1>"

@app.route('/login')
def login():
    return "Šeit būs login lapa!"



app.run(debug=True)
