import hashlib
def login():
   #salt = 'm@d@o'
   parole = "skola"
   
   parole_hash = hashlib.md5(bytes(parole, 'utf-8'))
   parole_encode = parole_hash.hexdigest()
   paroles_ievads = input('Ievadi paroli: ')
   paroles_ievads_hash = hashlib.md5(bytes(paroles_ievads, 'utf-8'))
   print(paroles_ievads_hash)
   paroles_ievads_encode = paroles_ievads_hash.hexdigest()
   print(paroles_ievads_encode)
   if parole_encode == paroles_ievads_encode:
      print("Parole ievadīta pareizi")
   else:
     print("Parole ievadīta nepareizi")
   return "0"
 
login()