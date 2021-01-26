function labotKriteriju(id, row, cell, content) {
    var x = document.getElementById(id).rows[row].cells;
    x[cell].innerHTML = content;
  }