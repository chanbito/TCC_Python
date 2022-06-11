// var inputElement = document.getElementById('button-mensagem');
// inputElement.addEventListener('click', function(){
//     console.log("passei1")
//     new_txt = traduzir(result.name);
//     inputElement.textContent = new_text;
// });

function traduzir(mensagem){
   //a mensagem ta vindo então
      let call = "/translater/"
      fetch(call.concat(mensagem ,"/"),{method: "GET"})
      .then(r => r.json())
      .then(data => {alert(data.mensagem)})   
}