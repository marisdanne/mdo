sanemtDatus()

async function sutitDatus(){
    console.log ("Mēģinām sūtīt datus")
    let criteria = document.getElementById('prasmes')
    let one = document.getElementById('snieguma_limenis_1')
    let two = document.getElementById('snieguma_limenis_2')
    let three = document.getElementById('snieguma_limenis_3')
    let four = document.getElementById('snieguma_limenis_4')
   
    const atbilde = await fetch('/skolenu_sniegums/post', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "prasmes": criteria.value, "snieguma_limenis_1":one.value,"snieguma_limenis_2": two.value, "tresnieguma_limenis_3": three.value, "snieguma_limenis_4": four.value })
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
    let tabulaDatiem = document.getElementById('prasmju_tabula')
        tabulaDatiem.innerHTML = ""

    for(let rinda of datuObjekts){
        tabulaDatiem.innerHTML = tabulaDatiem.innerHTML +
            "<tr><td>" + rinda.prasme + "</td>" + 
            "<td onclick='krasot_sunas(this)'>" + rinda.snieguma_limenis_1  + "</td>" +
            "<td onclick='krasot_sunas(this)'>" + rinda.snieguma_limenis_2  + "</td>" +
            "<td onclick='krasot_sunas(this)'>" + rinda.snieguma_limenis_3  + "</td>" +
            "<td onclick='krasot_sunas(this)'>" + rinda.snieguma_limenis_4  + "</td>" +
            "</tr>"
    }
    
} 
function krasot_sunas(suna){
    if (suna.bgColor == "yellow"){
        suna.bgColor = ""
    } else {
        suna.bgColor = "yellow"
    }
}