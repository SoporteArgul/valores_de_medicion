var Fin = new function(){
	//Tomar datos ingresados en los campos
	this.tipoProceso = document.getElementById("proceso");
	this.tipoLente = document.getElementById("tipo");
	this.cantRotulos = document.getElementById("rotulos");
	this.CantPiezas = document.getElementById("piezas");
	
this.OP = function(){
	//Declaracion de variables
	 var tipoproceso;
	 tipoproceso = this.tipoProceso.value;
	 var tipolente;
	 tipolente = this.tipoLente.value;
	 var rotulos;
	 rotulos = this.cantRotulos.value;
	 var piezas;
	 piezas = this.CantPiezas.value;
	 var resultadofinal;
	// Calculo de finalizacion de orden
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
	resultadofinal = parseInt(rotulos) * parseInt(piezas) / piezascarro;
	// Mostrar datos en pagina
	this.Resultado = document.getElementById("resultado");
	return this.Resultado.innerHTML = resultadofinal.toFixed(1);
}
}