function tipo_select() {
    var choseele = document.getElementById('ele').value;
    var chosemov = document.getElementById('mov').value;
    var choseuti = document.getElementById('uti').value;
 }
 
 window.onload = function() {
     var botao_chose_ele = document.getElementById('botao_chose_ele');
     botao_chose_ele.onclick = tipo_select;
 
     var botao_chose_mov = document.getElementById('botao_chose_mov');
     botao_chose_mov.onclick = tipo_select;
 
     var botao_chose_uti = document.getElementById('botao_chose_uti');
     botao_chose_uti.onclick = tipo_select;
 }
 