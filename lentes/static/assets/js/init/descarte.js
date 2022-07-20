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
     caja1 = parseInt(this.Caja1.value);
     var cant1;
     cant1 = parseInt(this.Cant1.value);
     var caja2;
     caja2 = parseInt(this.Caja2.value);
     var cant2;
     cant2 = parseInt(this.Cant2.value);
     var cantpiezas;
     cantpiezas = parseInt(this.Piezasxcaja.value);
     var grs;
     grs = parseInt(this.Grs.value);
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
    let resultado = caja2 - caja1;
    let resultado1 = resultado * cantpiezas;
    let buenas = resultado1 - cant1 + cant2;
    // Calculo de piezas malas
    if (tipolente == "Ecoline") {
        pesomalas = grs - buenas;
        piezasmalas = pesomalas / 15.5;
    }
    if (tipolente == "Neon") {
        pesocolada = buenas * 0.5;
        pesomalas = grs - pesocolada;
        piezasmalas = pesomalas / 15.5;
    }
    if (tipolente == "Argon") {
        pesocolada = buenas * 0.5;
        pesomalas = grs - pesocolada;
        piezasmalas = pesomalas / 23;
    }
    if (tipolente == "Mig") {
        pesocolada = buenas * 2;
        pesomalas = grs - pesocolada;
        piezasmalas = pesomalas / 16.5;
    }
    // Calculo de porcentaje de scrap
    produccion = buenas + piezasmalas;
    resultadofinal = piezasmalas * 100 / produccion;
    // Mostrar datos en pagina
    this.piezasBuenas = document.getElementById('buenas');
    this.piezasMalas = document.getElementById('malas');
    this.Scrap = document.getElementById('scrap');
    return this.piezasBuenas.innerHTML = buenas,this.Scrap.innerHTML = resultadofinal.toFixed(1),this.piezasMalas.innerHTML = piezasmalas.toFixed(0);
    }
    }