function kriterijs ()
{
var tabula = document.getElementById ("snieguma_limenu_tabula");                
var rinda = tabula.rows;                                          
var pedeja = rinda [rinda.length - 1];                              
var suna = pedeja.cells.length;                                    
 
var rindina = tabula.insertRow (tabula.rows.length);  
rindina.innerHTML=`<td> <input type="text"   ></td>
<td> <input type="text"   ></td>
<td> <input type="text"   ></td>
<td> <input type="text"  ></td>
<td> <input type="text"   ></td>`


var cedit = rindina.insertCell (-1);
cedit.innerHTML = `<button onclick="dzestKriteriju(this)">Dzēst</button> 
<button onclick="LabotKriteriju()">Labot</button> </td>`;
}
