const carregarMensagem=()=>{
    const section_mensagem=document.getElementById("section_mensagem");
    const url_mensagem=section_mensagem.dataset.url_mensagem;

    fetch(url_mensagem).then(response=>response.json()).then(data=>{
        const paragrafo=document.getElementById("mensagem");
        paragrafo.innerText=data.texto;
    })
}