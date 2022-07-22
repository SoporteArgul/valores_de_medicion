var Control = new function(){
    //Tomar datos ingresados en los campos
    this.Caja1 = document.getElementById("caja1");
    this.Cant1 = document.getElementById("cant1");
    this.Caja2 = document.getElementById("caja2");
    this.Cant2 = document.getElementById("cant2");
    this.Piezasxcaja = document.getElementById("piezasxcaja");
    this.tipoLente = document.getElementById("tipolente");
    this.Grs = document.getElementById("grs");
    
this.Descarte = function(){
    //Declaracion de variables
     var caja1;
     caja1 = this.Caja1.value;
     var cant1;
     cant1 = this.Cant1.value;
     var caja2;
     caja2 = this.Caja2.value;
     var cant2;
     cant2 = this.Cant2.value;
     var cantpiezas;
     cantpiezas = this.Piezasxcaja.value;
     var grs;
     grs = this.Grs.value;
     var tipoLente;
     tipolente = this.tipoLente.value;
     var resultado;
     var resultado1;
     var buenas;
     var pesomalas;
     var piezasmalas;
     var pesocolada;
     var produccion;
     var resultadofinal;
    // Calculo de piezas buenas
    resultado = parseInt(caja2) - parseInt(caja1);
    resultado1 = resultado * parseInt(cantpiezas);
    buenas = resultado1 - parseInt(cant1) + parseInt(cant2);
    // Calculo de piezas malas
    if (tipolente == "ecoline") {
        pesomalas = parseInt(grs) - buenas;
        piezasmalas = pesomalas / 15.5;
    }
    if (tipolente == "neon") {
        pesocolada = buenas * 0.5;
        pesomalas = parseInt(grs) - pesocolada;
        piezasmalas = pesomalas / 15.5;
    }
    if (tipolente == "argon") {
        pesocolada = buenas * 0.5;
        pesomalas = parseInt(grs) - pesocolada;
        piezasmalas = pesomalas / 23;
    }
    if (tipolente == "mig") {
        pesocolada = buenas * 2;
        pesomalas = parseInt(grs) - pesocolada;
        piezasmalas = pesomalas / 16.5;
    }
    
    // Calculo de porcentaje de scrap
    produccion = buenas + piezasmalas;
    resultadofinal = piezasmalas * 100 / produccion;
    
    // Mostrar datos en pagina
    this.piezasBuenas = document.getElementById('buenas');
    this.piezasMalas = document.getElementById('malas');
    this.Scrap = document.getElementById('scrap');
    
    var Myelement1 = document.forms['formControlDescartes']['piezas_buenas']
	Myelement1.setAttribute('value', buenas.toFixed(1))

    var Myelement2 = document.forms['formControlDescartes']['piezas_malas']
	Myelement2.setAttribute('value', piezasmalas.toFixed(1))

    var Myelement3 = document.forms['formControlDescartes']['piezas_descartadas']
	Myelement3.setAttribute('value', resultadofinal.toFixed(1))

    return this.piezasBuenas.innerHTML = buenas, this.Scrap.innerHTML = resultadofinal.toFixed(1), this.piezasMalas.innerHTML = piezasmalas.toFixed(0);
    }
    }