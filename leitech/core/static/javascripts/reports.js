

//Carrega a API
google.load('visualization', '1', {'packages':['corechart']});


var json1 = {
        cols: [
                {id: '', label: 'Mês', type: 'string'},
                {id: '', label: 'Ocorrências', type: 'number'}],
           rows: [
              {c:[{v: 'Fevereiro'}, {v: 3}]},
              {c:[{v: 'Março'}, {v: 14}]},
              {c:[{v: 'Abril'}, {v: 15}]},
              {c:[{v: 'Maio'}, {v: 15}]},
              {c:[{v: 'Junho'}, {v: 4}]},
              {c:[{v: 'Julho'}, {v: 9}]},
              {c:[{v: 'Agosto'}, {v: 17}]},
              {c:[{v: 'Setembro'}, {v: 10}]},
              {c:[{v: 'Outubro'}, {v: 3}]},
              {c:[{v: 'Novembro'}, {v: 0}]},
              {c:[{v: 'Dezembro'}, {v: 0}]},

          ]       
 };

var json2 = {
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
         
                 
     } ;

var json3 = {
         cols: [
                
                {id: '', label: 'Ocorências', type: 'string'},
                {id: '', label: 'Oeste', type: 'number'},
                {id: '', label: 'Leste', type: 'number'},                
                {id: '', label: 'Sul', type: 'number'},
                {id: '', label: 'Norte', type: 'number'}
                ],
         rows: [
               {
                   c:[{v:''},{v:18},{v:36},{v:16},{v:20}]} 
               ]
         
                 
     } ;
     var json4 = {
         cols:[
             {id: '', label: 'Ocorrências', type: 'string'},
             {id: '', label: 'Tirol', type: 'number'},
             {id: '', label: 'Satélite', type: 'number'},
             {id: '', label: 'Santos Reis', type: 'number'},
             {id: '', label: 'Salinas', type: 'number'},
             {id: '', label: 'Rocas', type: 'number'},
             {id: '', label: 'Ribeira', type: 'number'},
             {id: '', label: 'Redinha', type: 'number'},
             {id: '', label: 'Quintas', type: 'number'},
             {id: '', label: 'Praia do Meio', type: 'number'},
             {id: '', label: 'Potengi', type: 'number'},
             {id: '', label: 'Ponta Negra', type: 'number'},
             {id: '', label: 'Planalto', type: 'number'},
             {id: '', label: 'Pitimbu', type: 'number'},
             {id: '', label: 'Pirangi', type: 'number'},
             {id: '', label: 'Petrópolis', type: 'number'},
             {id: '', label: 'Pajuçara', type: 'number'},
             {id: '', label: 'Nova Descoberta', type: 'number'},
             {id: '', label: 'Nossa Senhora de Nazaré', type: 'number'},
             {id: '', label: 'Nossa Senhora da Apresentação', type: 'number'},
             {id: '', label: 'Neópolis', type: 'number'},
             {id: '', label: 'Mirassol', type: 'number'},
             {id: '', label: 'Mãe Luíza', type: 'number'},
             {id: '', label: 'Lagoa Seca', type: 'number'},
             {id: '', label: 'Lagoa Nova', type: 'number'},
             {id: '', label: 'Lagoa Azul', type: 'number'},
             {id: '', label: 'Igapó', type: 'number'},
             {id: '', label: 'Guarapes', type: 'number'},
             {id: '', label: 'Felipe Camarão', type: 'number'},
             {id: '', label: 'Dix-Sept Rosado', type: 'number'},
             {id: '', label: 'Cidade Nova', type: 'number'},
             {id: '', label: 'Cidade da Esperança', type: 'number'},
             {id: '', label: 'Cidade Alta', type: 'number'},
             {id: '', label: 'Capim Macio', type: 'number'},
             {id: '', label: 'Candelária', type: 'number'},
             {id: '', label: 'Bom Pastor', type: 'number'},
             {id: '', label: 'Barro Vermelho', type: 'number'},
             {id: '', label: 'Bairro Nordeste', type: 'number'},
             {id: '', label: 'Areia Preta', type: 'number'},
             {id: '', label: 'Alecrim', type: 'number'}

             
         ],
         rows:[
                 { c:[{v:'Quantidade de Ocorrências'}
                    ,{v:2},{v:1},{v:1},{v:0},{v:1},{v:0},{v:1},{v:2},{v:0},{v:5},{v:3}
                    ,{v:2},{v:5},{v:0},{v:6},{v:1},{v:2},{v:0},{v:6},{v:2},{v:0},{v:2}
                    ,{v:3},{v:6},{v:4},{v:3},{v:0},{v:3},{v:4},{v:3},{v:3},{v:3},{v:1}
                    ,{v:3},{v:1},{v:3},{v:1},{v:0},{v:7}
                    ]
                } 
         ]
     } ;  


  google.setOnLoadCallback(_graph2);    
  google.setOnLoadCallback(_graph3);    
     

function _graph1(){
    GeraGraph(json1,'id_report01','title','tituloV','tituloH',500,400,2,'');
}

function _graph2(){
    GerarGraph(json2,'id_report02','','','',500,400,1);
}

function _graph3(){
    GeraGraph(json3,'id_report03','','','',500,400,1);
}     
function _graph4(){
    GeraGraph(json4,'id_report04','','Bairros','Quantidade de Ocorrências',600,500,1,'bottom');
}


//Função genérica onde recebe como parametros os dados a serem gerados as options/conf
// para o gráfico e qual local será exibido o gráfico
function GerarGraph(dados,divGera,title,titleVAxis,titlehAxis,width,heigth,modExibicao,legend,tridimensional){
       var options = {
                  title: title,
                  width:width, height:heigth,
                  vAxis: {title: titleVAxis},
                  hAxis: {title: titlehAxis},
                  legend: legend,//posicionamento das colunas
                  is3D: tridimensional
           };

    var dataJSON = new google.visualization.DataTable(dados);

   if(modExibicao == 1){//exibi o gráfico em barra lateral        
    var chart = new google.visualization.BarChart(document.getElementById(divGera));
            chart.draw(dataJSON,options);
   }
   else if(modExibicao==2){//exibi o gráfico em modelo linear
        var chart = new google.visualization.LineChart(document.getElementById(divGera));
            chart.draw(dataJSON,options);
   }
   else if(modExibicao==3){//exibi o gráfico em modelo de pizza
        var chart = new google.visualization.PieChart(document.getElementById(divGera));
            chart.draw(dataJSON,options);
   }
   
}
