var table =document.getElementById("prasmju_tabula"), rIndex, cIndex;
for (var i=1; i<table.rows.length;i++) {
    for (var j=0; j<table.rows[i].cells.length;j++) {
        table.rows[i].cells[j].onclick=function() {
            cell=this.cellIndex+1;
            document.getElementById("snieguma_limenis_1").value=this.cells[cell].innerHTML;
            document.getElementById("snieguma_limenis_2").value=this.cells[cell].innerHTML;
            document.getElementById("snieguma_limenis_3").value=this.cells[cell].innerHTML;
            document.getElementById("snieguma_limenis_4").value=this.cells[cell].innerHTML;
        }  ;
    }
}
