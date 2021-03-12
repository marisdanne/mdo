function registreties(){
    let lietotajsInput = document.getElementById('lietotajs')
    let paroleInput = document.getElementById('parole')
    let paroleAtkInput = document.getElementById('parole_atk')
    let vardsInput = document.getElementById('vards')
    let uzvardsInput = document.getElementById('uzvards')
    let lomaInput=document.getElementById('loma')
    let klaseInput = document.getElementById('klase')

    let lietotajs = lietotajsInput.value
    let parole = paroleInput.value
    let paroleAtk = paroleAtkInput.value
    let vards = vardsInput.value
    let uzvards = uzvardsInput.value
    let loma = lomaInput.value
    let klase = klaseInput.value

    if(lietotajs.length < 3){
        alert("Lietotājvārdam jābūt garākam par 2 simboliem")
        return
    }

    if(parole != paroleAtk){
        alert("Ievadītās parole nesakrīt!")
        return        
    }


    // console.log(lietotajs)
    // console.log(parole)
    // console.log(paroleAtk)
    // console.log(vards)
    // console.log(uzvards)
    // console.log(klase)
    let dati = JSON.stringify({"lietotajs": lietotajs, "parole":parole, "vards":vards, "uzvards":uzvards,"loma":loma, "klase":klase })
    sutitDatus(dati)

    alert("Jūs esat reģistrēts!")
    lietotajsInput.value = ""
    paroleInput.value = ""
    paroleAtkInput.value = ""
    vardsInput.value = ""
    lomaInput.value = ""
    uzvardsInput.value = ""
    klaseInput.value = ""
}

async function sutitDatus(dati){
    const atbilde = await fetch('/api/registracija', {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json'
        },
        body: dati
    });
}