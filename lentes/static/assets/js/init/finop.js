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
	if (tipoproceso == "af") {
		if (tipolente == "argon") {
		piezascarro = 12 * 24;
		}
	else if (tipolente == "ecoline" | tipolente == "neon" | tipolente == "elite" | tipolente == "new classic" | tipolente == "aviator") {
		piezascarro = 22 * 24;
		}
	else if (tipolente == "mig" | tipolente == "dual") {
		piezascarro = 11 * 24;
		}
	}
	if (tipoproceso == "hc") {
		if (tipolente == "argon") {
		piezascarro = 30 * 12;
		}
	else if (tipolente == "ecoline" | tipolente == "neon" | tipolente == "elite" | tipolente == "aviator") {
		piezascarro = 55 * 12;
		}
	else if (tipolente == "mig" | tipolente == "dual") {
		piezascarro = 33 * 12;
		}
	else if (tipolente == "new classic") {
		piezascarro = 44 * 12;
		}
	}
	resultadofinal = parseInt(rotulos) * parseInt(piezas) / piezascarro;
	// Mostrar datos en pagina
	this.Resultado = document.getElementById("resultado");
	var Myelement = document.forms['formFinOp']['carros']
	Myelement.setAttribute('value',resultadofinal.toFixed(1))
	return this.Resultado.innerHTML = resultadofinal.toFixed(1);
}
}