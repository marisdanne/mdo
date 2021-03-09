import sqlite3

savienojums = sqlite3.connect("mdo.db") 

dati=savienojums.execute("SELECT * FROM lietotaji")
print(dati)

#for rinda in dati:
#    print(rinda)

for rinda in dati:
    print(rinda[1])




savienojums.close()