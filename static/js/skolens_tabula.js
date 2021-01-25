var table =document.getElementById("tabula"), rIndex, cIndex;
for (var i=1; i<table.rows.length;i++) {
    for (var j=0; j<table.rows[i].cells.length;j++) {
        table.rows[i].cells[j].onclick=function() {
            cell=this.cellIndex+1;
            document.getElementById("1").value=this.cells[cell].innerHTML;
            document.getElementById("2").value=this.cells[cell].innerHTML;
            document.getElementById("3").value=this.cells[cell].innerHTML;
            document.getElementById("4").value=this.cells[cell].innerHTML;
        }  ;
    }
}
