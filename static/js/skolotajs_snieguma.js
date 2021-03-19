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
    const atbilde = await fetch('/api/v1/prasmes')
    const datuObjekts = await atbilde.json()
    console.log(datuObjekts)
    let tabula = document.getElementById('snieguma_limenu_tabula')
    //tabulaDatiem.innerHTML = ""

    for(let dati of datuObjekts){
       let rinda = tabula.insertRow(1)
       let suna1=rinda.insertCell(0)
       let suna2=rinda.insertCell(1)
       let suna3=rinda.insertCell(2)
       let suna4=rinda.insertCell(3)
       let suna5=rinda.insertCell(4)
       let suna6= rinda.insertCell(5)
       console.log(dati)
       suna1.innerHTML = dati.prasme
       suna2.innerHTML = dati.snieguma_limenis_1
       suna3.innerHTML = dati.snieguma_limenis_2
       suna4.innerHTML = dati.snieguma_limenis_3
       suna5.innerHTML = dati.snieguma_limenis_4
       suna6.innerHTML= `<button onclick="dzestKriteriju(this)">Dzēst</button>
      <button onclick="LabotKriteriju()">Labot</button>`
      // tabulaDatiem.innerHTML =innerHTML =tabulaDatiem.innerHTML+"<p>" + rinda.Kriterijs +  rinda.pirmais  + rinda.otrais  + rinda.tresais  + rinda.ceturtais+ "</p>"
    }
    
} 