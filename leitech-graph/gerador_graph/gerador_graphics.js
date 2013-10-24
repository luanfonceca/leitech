        //Carrega o pacote da API 
        google.load('visualization', '1', {'packages':['corechart']});
//JSON      
       var json21 = {
         cols: [
                
                {id: '', label: 'Ocorências', type: 'string'},
                {id: '', label: 'Via Pública', type: 'number'},
                {id: '', label: 'Federal', type: 'number'},                
                {id: '', label: 'Particular', type: 'number'},
                {id: '', label: 'Municipal', type: 'number'},
                {id: '', label: 'Estadual', type: 'number'}
                ],
         rows: [
               {
                   c:[{v:'Público Atendido'},{v:39},{v:0},{v:13},{v:6},{v:32}]} 
               ]
         
                 
     };
     var json22 = {
        cols: [
                {id: '', label: 'Público Atendido', type: 'string'},
                {id: '', label: 'Ocorrências', type: 'number'}],
           rows: [
              {c:[{v: 'Via Pública'}, {v: 39}]},
              {c:[{v: 'Federal'}, {v: 0}]},
              {c:[{v: 'Particular'}, {v: 13}]},
              {c:[{v: 'Municipal'}, {v: 6}]},
              {c:[{v: 'Estadual'}, {v: 32}]}
             ]
            } ;
     
     var json31 = {
         cols: [
                
                {id: '', label: 'Ocorências', type: 'string'},
                {id: '', label: 'Oeste', type: 'number'},
                {id: '', label: 'Leste', type: 'number'},                
                {id: '', label: 'Sul', type: 'number'},
                {id: '', label: 'Norte', type: 'number'}
                ],
         rows: [
               {
                   c:[{v:'Ocorrências'},{v:18},{v:36},{v:16},{v:20}]} 
               ]
         
                 
     };
     var json32 = {
        cols: [
                {id: '', label: 'Região', type: 'string'},
                {id: '', label: 'Ocorrências', type: 'number'}],
           rows: [
              {c:[{v: 'Oeste'}, {v: 18}]},
              {c:[{v: 'Leste'}, {v: 36}]},
              {c:[{v: 'Sul'}, {v: 16}]},
              {c:[{v: 'Norte'}, {v: 20}]}
             ]
            } ;
//FIM MODELO JSON 
 
google.setOnLoadCallback(carrega);//se colocar a função com paramentro
// não roda!(isso especificamente para o setOnLoadCallback) 

//Essa função carrega pode ficar mais orientada vai depender da maneira que vcs queiram
function carrega(){
    
   var option = {
                  title:"Assaltos registrados",
                  width:800, height:400,
                  vAxis: {title: ""},
                  hAxis: {title: "Número de assaltos"}
           };           
           
GeraGraph(json21,option,'bar_G021');
GeraGraph(json22,option,'bar_G022');
GeraGraph(json31,option,'bar_G031');
GeraGraph(json32,option,'bar_G032');


}

//Função genérica onde recebe como parametros os dados a serem gerados as options/conf
// para o gráfico e qual local será exibido o gráfico
function GeraGraph(dados,options,divGera){

    var dataJSON = new google.visualization.DataTable(dados);
    var chart = new google.visualization.BarChart(document.getElementById(divGera));
            chart.draw(dataJSON,options);

}

