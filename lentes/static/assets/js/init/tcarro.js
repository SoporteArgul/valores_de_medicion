var Tiempos = new function(){
	//Tomar datos ingresados en los campos
	this.tipoProceso = document.getElementById("proceso");
	this.tipoLente = document.getElementById("tipo");
	this.tiempoCiclo = document.getElementById("ciclo");
	
	this.Carros = function(){
	// Declaracion de variables
	 var tipoproceso;
	 tipoproceso = this.tipoProceso.value;
	 var tipolente;
	 tipolente = this.tipoLente.value;
	 
	 var ciclo = parseInt(this.tiempoCiclo.value);
	 var tiempocarro;
	 
	// Calculo de tiempo de carro
	if (tipoproceso == "af") {
		if (tipolente == "argon") {
		tiempocarro = 3 * ciclo * 24 / 60;
		}
	else if (tipolente == "ecoline" | tipolente == "mig" | tipolente == "dual") {
		tiempocarro = 5.5 * ciclo * 24 / 60;
		}
	else if (tipolente == "neon" | tipolente == "elite" | tipolente == "new" | tipolente == "aviator") {
		tiempocarro = 11 * ciclo * 24 / 60;
		}
	}
	if (tipoproceso == "hc") {
		if (tipolente == "argon") {
		tiempocarro = 7.5 * ciclo * 12 / 60;
		}
	else if (tipolente == "ecoline") {
		tiempocarro = 13.75 * ciclo * 12 / 60;
		}
	else if (tipolente == "mig" | tipolente == "dual") {
		tiempocarro = 16.5 * ciclo * 12 / 60;
		}
	else if (tipolente == "neon" | tipolente == "elite" | tipolente == "aviator") {
		tiempocarro = 27.5 * ciclo * 12 / 60;
		}
	else if (tipolente == "new") {
		tiempocarro = 22 * ciclo * 12 / 60;
		}
	}
	// Mostrar datos en pagina
	
	this.Resultado = document.getElementById("resultado");
	var Myelement = document.forms['formTiempoCarro']['tiempo_carro']
	Myelement.setAttribute('value',tiempocarro.toFixed(1))
	return this.Resultado.innerHTML = tiempocarro.toFixed(1);
	}
	}