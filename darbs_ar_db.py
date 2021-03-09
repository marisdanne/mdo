import sqlite3

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
    savienojums = sqlite3.connect(DATUBAZE)
    dati = savienojums.execute(vaicajums)
    savienojums.close()
    return dati

def registret(dati):
    vaicajums = f"INSERT INTO lietotaji (vards, uzvards, loma, klase, lietotajvards, parole) VALUES ('{dati['vards']}', '{dati['uzvards']}', 'skolēns', '{dati['klase']}', '{dati['lietotajs']}', '{dati['parole']}')"
    return ievietot(vaicajums)

def lietotaji():
    vaicajums = f"SELECT * from lietotaji"
    dati = atlasit(vaicajums)
    for rinda in dati:
        print(rinda)

