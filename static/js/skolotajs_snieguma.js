sanemtDatus()

async function sutitDatus(){
   // console.log ("Mēģinām sūtīt datus")
    let criteria = document.getElementById('Kriterijs')
    let one = document.getElementById('pirmais')
    let two = document.getElementById('otrais')
    let three = document.getElementById('tresais')
    let four = document.getElementById('ceturtais')
    


    let kriterijs = criteria.value
    let viens = one.value
    let divi = two.value
    let tris = three.value
    let cetri = four.value
    
    //Nodzēš ievades laukus
    criteria.value = ''
    one.value = ''
    two.value = ''
    three.value = ''
    four.value = ''


    const atbilde = await fetch('/skolotajs_snieguma/post/dati', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "Kriterijs": kriterijs, "pirmais":viens,"otrais": divi, "tresais": tris, "ceturtais": cetri })
    });

  sanemtDatus()

}


async function sanemtDatus(){
    const atbilde = await fetch('/skolotajs_snieguma/get')
    const datuObjekts = await atbilde.json()
    let tabulaDatiem = document.getElementById('tabula')
    tabulaDatiem.innerHTML = ""

    for(let rinda of datuObjekts){
        tabulaDatiem.innerHTML = "<p>Kriterijs:" + rinda.kriterijs + "</p>"
       // tabulaDatiem.innerHTML =tabulaDatiem.innerHTML+"<p>Kritērijs:" + rinda.kriterijs + "1 punkts: " + rinda.pirmais  + "2 punkti: " + rinda.otrais + "3 punkti: " + rinda.tresais + "4 punkti: " + rinda.ceturtais+ "</p>"
    }
    
} 