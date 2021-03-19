import sqlite3
import json

DATUBAZE = "mdo.db"

def ievietot(vaicajums):
    savienojums = sqlite3.connect(DATUBAZE)
    dati = savienojums.execute(vaicajums)
    savienojums.commit()
    savienojums.close()
    return dati

def atjaunot(vaicajums):
    return ievietot(vaicajums)

def atlasit_lietotajus(loma):
    data = atlasit(f"SELECT * FROM lietotaji WHERE loma =  '{loma}'")
    jsonData = kolonnas_json(data, ['id','vards','uzvards','klase'])
    msg = "Ieraksti veiksmīgi saņemti un apstrādāti"
    print(msg)
    return jsonData

def kolonnas_json(data,column_names):
    jsonData = ''
    for row in data:
        # Savienojam kolonu nosaukums ar datiem no tabulas
        info = dict(zip(column_names, row))
        # Pa vienai rindiņai papildimām jsonData mainīgo, līdz visi dati ir nolasīti no tabulas. Aiz katra ieraksta pieliekam komatu, lai atdalītu ierakstus.
        jsonData = jsonData + json.dumps(info) + ','
    # Noņemam pēdējo lieko komatu
    jsonData = jsonData[:-1]
    # Ieliekam visus datus kvadrātiekavās
    jsonData = '[' + jsonData + ']'
    return jsonData

def atlasit(vaicajums):
    try:
        with sqlite3.connect("mdo.db") as savienojums:
            kursors = savienojums.cursor()
            kursors.execute(vaicajums)
            # Ielasam datus mainīgajā
            data = kursors.fetchall()
    finally:    
        savienojums.commit()
        kursors.close()
        savienojums.close()    
        return data

def registret(dati):
    vaicajums = f"INSERT INTO lietotaji (vards, uzvards, loma, klase, lietotajvards, parole) VALUES ('{dati['vards']}', '{dati['uzvards']}', '{dati['loma']}', '{dati['klase']}', '{dati['lietotajs']}', '{dati['parole']}')"
    return ievietot(vaicajums)

def lietotaji():
    vaicajums = f"SELECT * from lietotaji"
    dati = atlasit(vaicajums)
    return dati

def pieteikties(lietotajvards, parole):
    vaicajums= f"SELECT loma FROM lietotaji WHERE lietotajvards = '{lietotajvards}' AND parole = '{parole}'"
    savienojums = sqlite3.connect(DATUBAZE)
    dati = savienojums.execute(vaicajums).fetchall()
    savienojums.commit()
    savienojums.close()
    if len(dati) == 1:
        return dati[0][0]
    else:
        return False

def nolasit(vaicajums):
    try:
        with sqlite3.connect("mdo.db") as savienojums:
            kursors = savienojums.cursor()
            kursors.execute(vaicajums)
             
            # Ielasam datus mainīgajā
            data = kursors.fetchall()
            jsonData = ''
            # Kolonu nosaukumi, kādi tiks izmantoti JSON failā. Tiem ir jābūt tādā pašā secībā, kā kolonas lasām no tabulas SELECT izsaukumā
            column_names = ['id','prasme','snieguma_limenis_1', 'snieguma_limenis_2', 'snieguma_limenis_3', 'snieguma_limenis_4','temati_id']
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
            
    finally:    
        savienojums.commit()
        kursors.close()
        savienojums.close()    
        return jsonData    