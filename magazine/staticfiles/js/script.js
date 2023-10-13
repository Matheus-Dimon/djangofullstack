function trocaeletro() {
    var dataCompra = new Date(document.getElementById('prazotroca').value);
    var dataAtual = new Date();
    var diferencaDias = Math.ceil((dataAtual - dataCompra) / (1000 * 60 * 60 * 24)); 
    
    if (diferencaDias <= 7) {
        alert('Você pode trocar o produto, pois a compra foi feita há menos de 7 dias.');
        
    } else {
        alert('Você não pode trocar o produto, pois a compra foi feita há mais de 7 dias.');
        alert('Porém você ainda tem 3 meses de garantia para fazer o envio para garantia direto para loja');
    }
}    
function trocautili() {
    var dataCompra = new Date(document.getElementById('prazotroca').value);
    var dataAtual = new Date();
    var diferencaDias = Math.ceil((dataAtual - dataCompra) / (1000 * 60 * 60 * 24)); 
    if (diferencaDias <= 7) {
        alert('Você pode trocar o produto, pois a compra foi feita há menos de 7 dias.');
        
    } else {
        alert('Você não pode trocar o produto, pois a compra foi feita há mais de 7 dias.');
    }   
}    
window.onload = function() {
    var botaoeletro = document.getElementById('elet');
    botaoeletro.onclick = trocaeletro;
    var botaoutili = document.getElementById('util');
    botaoutili.onclick = trocautili;
}


