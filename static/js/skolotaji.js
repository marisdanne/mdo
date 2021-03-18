async function getData(){
    let atbilde = await fetch("/api/v1/skolotaji");
    let datiJson = await atbilde.json();
     console.log(datiJson)
    let tabula = document.getElementById('skolotaji')

    for(let i = 0; i < datiJson.length; i++){
        let rindina = tabula.insertRow()
        let suna1 = rindina.insertCell()
        let suna2 = rindina.insertCell()
       
        suna1.innerHTML = datiJson[i].vards
        suna2.innerHTML = datiJson[i].uzvards
        
    }
}
window.addEventListener('load', function(){
    getData()
})
