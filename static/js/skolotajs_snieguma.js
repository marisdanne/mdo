sanemtDatus()

async function sutitDatus(){
    let criteria = document.getElementById('prasmes')
    let one = document.getElementById('snieguma_limenis_1')
    let two = document.getElementById('snieguma_limenis_2')
    let three = document.getElementById('snieguma_limenis_3')
    let four = document.getElementById('snieguma_limenis_4')
   
    const atbilde = await fetch('/prasmes', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "prasmes": criteria.value, "snieguma_limenis_1":one.value,"snieguma_limenis_2": two.value, "snieguma_limenis_3": three.value, "snieguma_limenis_4": four.value })
    });
    criteria.value = ''
    one.value = ''
    two.value = ''
    three.value = ''
    four.value = ''
    sanemtDatus()
}

async function sanemtDatus(){
    const atbilde = await fetch('/api/v1/prasmes')
    const datuObjekts = await atbilde.json()
    let tabula = document.getElementById('snieguma_limenu_tabula')
    
    for(let dati of datuObjekts){
       let rinda = tabula.insertRow(1)
       let suna1=rinda.insertCell(0)
       let suna2=rinda.insertCell(1)
       let suna3=rinda.insertCell(2)
       let suna4=rinda.insertCell(3)
       let suna5=rinda.insertCell(4)
       let suna6= rinda.insertCell(5)
       
       suna1.innerHTML = dati.prasme
       suna2.innerHTML = dati.snieguma_limenis_1
       suna3.innerHTML = dati.snieguma_limenis_2
       suna4.innerHTML = dati.snieguma_limenis_3
       suna5.innerHTML = dati.snieguma_limenis_4
       suna6.innerHTML= `<button onclick="dzestKriteriju(this)">Dzēst</button>
      <button onclick="LabotKriteriju()">Labot</button>`
      
    }
    
} 