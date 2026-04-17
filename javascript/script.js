 document.addEventListener("DOMContentLoaded", (event) => {
    const cursos=['Django','JavaScript','CSS'];
    const lista=document.getElementById("cursos")
    for (let indice=0;indice<cursos.length;indice++){
        let li=document.createElement("li");
        li.innerText=cursos[indice];
        lista.appendChild(li);
}
  });

const adicionarTexto=()=>{
    let texto=document.getElementById("conteudo").value.toString();
    if (texto.trim().length==0){
        alert("Informe um valor");
        return;
    }
    const list=document.getElementById("cursos")
    let item=document.createElement("li");
    item.innerText=texto;
    list.appendChild(item);
}