var t = document.getElementsById('snieguma_limenu_tabula');
var rows = t.getElementsByTagName("tr");
for ( var i = 1; i < rows.length; i += 2 )
rows[i].className = "kriteriji";