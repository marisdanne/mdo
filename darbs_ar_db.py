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

def atlasit(vaicajums):
    try:
        with sqlite3.connect("mdo.db") as savienojums:
            kursors = savienojums.cursor()
            kursors.execute(vaicajums)
             
            # Ielasam datus mainīgajā
            data = kursors.fetchall()
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
            
    finally:    
        savienojums.commit()
        kursors.close()
        savienojums.close()    
        return jsonData

def registret(dati):
    vaicajums = f"INSERT INTO lietotaji (vards, uzvards, loma, klase, lietotajvards, parole) VALUES ('{dati['vards']}', '{dati['uzvards']}', '{dati['loma']}', '{dati['klase']}', '{dati['lietotajs']}', '{dati['parole']}')"
    return ievietot(vaicajums)

def lietotaji():
    vaicajums = f"SELECT * from lietotaji"
    dati = atlasit(vaicajums)
    return dati

