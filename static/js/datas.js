var datas = document.getElementsByClassName('date');

for (let i = 0;  i < datas.length; i++){
    var data_errada = datas[i].getAttribute('data-variavel');

    const data = new Date(`${data_errada}T00:00:00`);

    const dataFormatada = data.toLocaleDateString("pt-BR");

    datas[i].innerHTML = dataFormatada;
};