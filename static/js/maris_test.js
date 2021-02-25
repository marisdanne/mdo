sanemtDatus()

async function sutitDatus(){
    let vardsElem = document.getElementById('vards')
    let uzvardsElem = document.getElementById('uzvards')

    let vards = vardsElem.value
    let uzvards = uzvardsElem.value
    
    // Nodzēš ievades laukus
    vardsElem.value = ''
    uzvardsElem.value = ''


    const atbilde = await fetch('/maris/test/post/dati', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "vards": vards, "uzvards":uzvards })
    });

    sanemtDatus()
}


async function sanemtDatus(){
    const atbilde = await fetch('/maris/test/get')
    const datuObjekts = await atbilde.json()
    
    let divTabula = document.getElementById('tabula')
    divTabula.innerHTML = ""

    for(let rinda of datuObjekts){
        divTabula.innerHTML = divTabula.innerHTML + "<p>Vārds:" + rinda.vards + " Uzvārds:" + rinda.uzvards + "</p>"
    }
    
}