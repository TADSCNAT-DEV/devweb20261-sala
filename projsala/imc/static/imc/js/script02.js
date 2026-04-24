const carregarMensagem=()=>{
    const section_mensagem=document.getElementById("section_mensagem");
    const url_mensagem=section_mensagem.dataset.url_mensagem;

    fetch(url_mensagem).then(response=>response.json()).then(data=>{
        const paragrafo=document.getElementById("mensagem");
        paragrafo.innerText=data.texto + data.mensagem_texto;
    })
}

const carregarResultadoIMC = (event) => {
    event.preventDefault(); // Impede o envio do formulário padrão, senão ele geraria um reload da página
    const url_requisicao_post = document.getElementById('url_requisicao').dataset.url_post //Captura qual é a URL que deve ser requisitada
    fetch(url_requisicao_post,{ // Usando a API fetch para fazer a requisição POST, colocando o cabecalho correto e o corpo da requisição
        method: 'POST',
        headers: { //Cabeçalho da requisição com o tipo de conteúdo e o token CSRF para segurança
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
        },
        body: JSON.stringify({ //O JSON.stringify converte o objeto JavaScript em uma string JSON, a partir dos valores dos campos do formulário
            peso: document.getElementById('peso').value,
            altura: document.getElementById('altura').value
        })
    })
        .then(response => response.text()) // O then espera a resposta do servidor e converte para texto
        .then(data => { // O segundo then recebe o texto retornado e atualiza o conteúdo do elemento com id 'resultado_imc'
            document.getElementById('resultado_imc').innerHTML = data;
            const div=document.getElementById("classificacao");
            const msg=div.dataset.classificacao;
            window.alert(msg);
            console.log(data);
        })
        .catch(error => { //Caso ocorra algum erro na requisição, ele será capturado aqui
            console.error('Erro ao carregar resultado IMC:', error);
            window.alert("Ocorreu um erro ao calcular o IMC. Por favor, tente novamente.",error);
        });
}