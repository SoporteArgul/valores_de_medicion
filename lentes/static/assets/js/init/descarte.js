let cajafin;
let cajaini;
let cantfin;
let cantini;
let produccion;
let cantpiezas;
let resultado;
let piezasmalas;
let resultado2;

let peso;
let tipolente;
let buenas;
let pesocolada;
let pesomalas;
let resultadofinal;

window.addEventListener("keypress", function(event){
    if (event.keyCode == 13){
        event.preventDefault();
    }
}, false);

const input = document.getElementById('caja1');
input.addEventListener('change', updateValue);
function updateValue(a){
cajaini = a.target.value;
}
const input1 = document.getElementById('cant1');
input1.addEventListener('change', updateValue1);
function updateValue1(b){
cantini = b.target.value;
}
const input2 = document.getElementById('caja2');
input2.addEventListener('change', updateValue2);
function updateValue2(c){
cajafin = c.target.value;
}
const input3 = document.getElementById('cant2');
input3.addEventListener('change', updateValue3);
function updateValue3(d){
cantfin = d.target.value;

}

const input4 = document.getElementById('piezasxcaja');
input4.addEventListener('change', updateValue4);
function updateValue4(e){
cantpiezas = e.target.value;
funcionBuenas();
}

const selectElement = document.querySelector('.lentes');
selectElement.addEventListener('change', (event) => {
const proceso = document.querySelector('.resultado');
proceso.textContent = `${event.target.value}`;
tipolente = proceso.textContent;
});

const input5 = document.getElementById('kg');
const log1 = document.getElementById('log');
input5.addEventListener('change', updateValue5);
function updateValue5(f){
    log1.textContent = f.target.value;
    peso = log1.textContent;
    funcionMalas();
}

function funcionBuenas(){
// Piezas buenas
resultado = parseInt(cajafin) - parseInt(cajaini);
resultado1 = resultado * parseInt(cantpiezas);
const piezasbuenas = document.getElementById('resultado2');
buenas = resultado1 - parseInt(cantini) + parseInt(cantfin);
piezasbuenas.textContent = buenas;
}

function funcionMalas(){
if (tipolente == "Ecoline") {
    pesomalas = parseInt(peso) - parseInt(buenas);
    piezasmalas = pesomalas / 15.5;
    const log2 = document.getElementById('log1');
    log2.textContent = piezasmalas;
    funcionScrap();
    }
if (tipolente == "Neon") {
    pesocolada = parseInt(buenas) * 0.5;
    pesomalas = parseInt(peso) - parseInt(pesocolada);
    piezasmalas = pesomalas / 15.5;
    const log2 = document.getElementById('log1');
    log2.textContent = piezasmalas;
    funcionScrap()
    }
if (tipolente == "Argon") {
    pesocolada = parseInt(buenas) * 0.5;
    pesomalas = parseInt(peso) - parseInt(pesocolada);
    piezasmalas = pesomalas / 23;
    const log2 = document.getElementById('log1');
    log2.textContent = piezasmalas;
    funcionScrap()
    }
if (tipolente == "Mig") {
    pesocolada = parseInt(buenas) * 2;
    pesomalas = parseInt(peso) - parseInt(pesocolada);
    piezasmalas = pesomalas / 16.5;
    const log2 = document.getElementById('log1');
    log2.textContent = piezasmalas;
    funcionScrap()
    }
}
function funcionScrap(){
// porcentaje de scrap
produccion = parseInt(buenas) + parseInt(piezasmalas);
const scrap = document.getElementById('scrap');
resultadofinal = parseInt(piezasmalas) * 100 / parseInt(produccion);
scrap.textContent = resultadofinal;
}