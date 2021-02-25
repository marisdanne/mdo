import json

def nolasitDatus(datne):
    with open(datne, 'r', encoding='utf-8') as d:
        rindas = d.readlines()
        dati = []
        for rinda in rindas:
            dati.append(json.loads(rinda))

        return dati

def ierakstitDatus(datne, dati):
    with open(datne, 'a', encoding='utf-8') as f:
        f.write(dati + '\n')