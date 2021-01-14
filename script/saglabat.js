function saglabat() {
var table= document.getElementById("snieguma_limenu_tabula"),summa=0;

for(var i=1; i<table.rows.length;i++){
   console.log('es pārbaudu'+i+"rindu");
  for (var j=1; j<table.rows[i].cells.length;j++){
     
         if((table.rows[i].cells[j].bgColor=="yellow")&&( j==1)) {
            summa=summa+ 1;
            console.log("kolonna "+j);
            console.log(summa);
         } else if((table.rows[i].cells[j].bgColor=="yellow")&&( j==2)) {
               summa=summa+ 2; 
               console.log("kolonna "+j);
               console.log(summa);
            } else if((table.rows[i].cells[j].bgColor=="yellow")&&( j==3)) {
               summa=summa+ 3;
               console.log("kolonna "+j);
               console.log(summa);

            } else if((table.rows[i].cells[j].bgColor=="yellow")&&( j==4)) {
               summa=summa+ 4;
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