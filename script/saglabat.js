function saglabat() {
var table= document.getElementById("snieguma_limenu_tabula"),summa=0;

for(var i=1; i<table.rows.length;i++){
   console.log('es pārbaudu'+i+"rindu");
  for (var j=1; j<table.rows[i].cells.length;j++){
     
         if(table.rows[i].cells[j].bgColor=="yellow") {
            summa=summa+ j;
            console.log("kolonna "+j);
            console.log(summa);
         } 
         } 
      
   
    document.getElementById("vertiba").innerHTML="Tavs snieguma līmenis "+summa+ " punkti ";
    maksimalais=((table.rows.length-1)*4);
    procenti=(summa/maksimalais)*100;
    document.getElementById("procenti").innerHTML=procenti+" %";
    console.log("Beidzu pārbaudīt "+i+" rindu")
    
   }
   

}