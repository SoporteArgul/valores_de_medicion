let tipoproceso;
let tipolente;
let rotulos;
let piezas;
let piezascarro;

window.addEventListener("keypress", function(event){
    if (event.keyCode == 13){
        event.preventDefault();
    }
}, false);

		const selectElement1 = document.querySelector('.proceso');
		selectElement1.addEventListener('change', (event) => {
    	const proceso = document.querySelector('.resultado');
    	proceso.textContent = `${event.target.value}`;
    	tipoproceso = proceso.textContent;
    	lentes();
		});

		const selectElement2 = document.querySelector('.tipo');
		selectElement2.addEventListener('change', (event) => {
    	const tipo = document.querySelector('.resultado2');
    	tipo.textContent = `${event.target.value}`;
    	tipolente = tipo.textContent;
    	lentes();
		});

		const input = document.getElementById('rotulos');
		const log = document.getElementById('log');

		input.addEventListener('change', updateValue);


		function updateValue(e){
			log.textContent = e.target.value;
			rotulos = log.textContent;
			lentes();
		}

		const input1 = document.getElementById('piezas');
		const log1 = document.getElementById('log1');

		input1.addEventListener('change', updateValue1);


		function updateValue1(a){
			log1.textContent = a.target.value;
			piezas = log1.textContent;
			lentes();
		}

	function lentes(){
	if (tipoproceso == "Af") {
		if (tipolente == "Argon") {
		piezascarro = 12 * 24;
		}
	else if (tipolente == "Ecoline" | tipolente == "Neon" | tipolente == "Elite" | tipolente == "New" | tipolente == "Aviator") {
		piezascarro = 22 * 24;
		}
	else if (tipolente == "Mig" | tipolente == "Dual") {
		piezascarro = 11 * 24;
		}
	}
	if (tipoproceso == "Hc") {
		if (tipolente == "Argon") {
		piezascarro = 30 * 12;
		}
	else if (tipolente == "Ecoline" | tipolente == "Neon" | tipolente == "Elite" | tipolente == "Aviator") {
		piezascarro = 55 * 12;
		}
	else if (tipolente == "Mig" | tipolente == "Dual") {
		piezascarro = 33 * 12;
		}
	else if (tipolente == "New") {
		piezascarro = 44 * 12;
	}
	}
    const log2 = document.getElementById('log2');
    log2.textContent = rotulos * piezas / piezascarro;
}