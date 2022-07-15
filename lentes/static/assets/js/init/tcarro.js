let tipoproceso;
let tipolente;
let ciclo;
let tiempocarro;

window.addEventListener("keypress", function(event){
    if (event.keyCode == 13){
        event.preventDefault();
    }
}, false);
const selectElement1 = document.querySelector('proceso');
selectElement1.addEventListener('change', (event) => {
const proceso = document.querySelector('.resultado');
proceso.textContent = `${event.target.value}`;
tipoproceso = proceso.textContent;
lentes();
});

const selectElement2 = document.querySelector('tipo');
selectElement2.addEventListener('change', (event) => {
const tipo = document.querySelector('.resultado2');
tipo.textContent = `${event.target.value}`;
tipolente = tipo.textContent;
lentes();
});
const input = document.querySelector('input');
const log = document.getElementById('log');

input.addEventListener('change', updateValue);

function updateValue(e){
	log.textContent = e.target.value;
	ciclo = log.textContent;
	lentes();
}

function lentes(){
if (tipoproceso == "Af") {
	if (tipolente == "Argon") {
	tiempocarro = 3 * ciclo * 24 / 60;
	}
else if (tipolente == "Ecoline" | tipolente == "Mig" | tipolente == "Dual") {
	tiempocarro = 5.5 * ciclo * 24 / 60;
	}
else if (tipolente == "Neon" | tipolente == "Elite" | tipolente == "New" | tipolente == "Aviator") {
	tiempocarro = 11 * ciclo * 24 / 60;
	}
}
if (tipoproceso == "Hc") {
	if (tipolente == "Argon") {
	tiempocarro = 7.5 * ciclo * 12 / 60;
	}
else if (tipolente == "Ecoline") {
	tiempocarro = 13.75 * ciclo * 12 / 60;
	}
else if (tipolente == "Mig" | tipolente == "Dual") {
	tiempocarro = 16.5 * ciclo * 12 / 60;
	}
else if (tipolente == "Neon" | tipolente == "Elite" | tipolente == "Aviator") {
	tiempocarro = 27.5 * ciclo * 12 / 60;
	}
else if (tipolente == "New") {
	tiempocarro = 22 * ciclo * 12 / 60;
	}
}
const log1 = document.getElementById('log1');
log1.textContent = tiempocarro;
}