        //Carrega o pacote da API 
        google.load('visualization', '1', {'packages':['corechart']},{'packages':['linechart']});
//JSON      

 var json11 ={
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
         
                 
     } ;
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
                   c:[{v:''},{v:18},{v:36},{v:16},{v:20}]} 
               ]
         
                 
     } ;
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
 var json41 = {
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
 var json42 = {
        cols: [
                {id: '', label: 'Bairro', type: 'string'},
                {id: '', label: 'Ocorrências', type: 'number'}],
           rows: [
              {c:[{v: 'Tirol'}, {v: 2}]},
              {c:[{v: 'Satélite'}, {v: 1}]},
              {c:[{v: 'Santos Reis'}, {v: 1}]},
              {c:[{v: 'Salinas'}, {v: 0}]},
              {c:[{v: 'Rocas'}, {v: 1}]},
              {c:[{v: 'Ribeira'}, {v: 0}]},
              {c:[{v: 'Redinha'}, {v: 1}]},
              {c:[{v: 'Quintas'}, {v: 2}]},
              {c:[{v: 'Praia do Meio'}, {v: 0}]},
              {c:[{v: 'Potengi'}, {v: 5}]},
              {c:[{v: 'Ponta Negra'}, {v: 3}]},
              {c:[{v: 'Planalto'}, {v: 2}]},
              {c:[{v: 'Pitimbu'}, {v: 5}]},
              {c:[{v: 'Petrópoles'}, {v: 0}]},
              {c:[{v: 'Pajuçara'}, {v: 6}]},
              {c:[{v: 'Nova Descoberta'}, {v: 1}]},
              {c:[{v: 'Nossa Senhora de Nazaré'}, {v: 2}]},
              {c:[{v: 'Nossa Senhora da Apresentação'}, {v: 0}]},
              {c:[{v: 'Neópolis'}, {v: 6}]},
              {c:[{v: 'Mirassol'}, {v: 2}]},
              {c:[{v: 'Mãe Luíza'}, {v: 0}]},
              {c:[{v: 'Lagoa Seca'}, {v: 2}]},
              {c:[{v: 'Lagoa Nova'}, {v: 3}]},
              {c:[{v: 'Lagoa Azul'}, {v: 6}]},
              {c:[{v: 'Igapó'}, {v: 4}]},
              {c:[{v: 'Guarapes'}, {v: 3}]},
              {c:[{v: 'Felipe Camarão'}, {v: 0}]},
              {c:[{v: 'Dix-Sept Rosado'}, {v: 3}]},
              {c:[{v: 'Cidade Nova'}, {v: 4}]},
              {c:[{v: 'Cidade da Esperança'}, {v: 3}]},
              {c:[{v: 'Cidade Alta'}, {v: 3}]},
              {c:[{v: 'Capim Macio'}, {v: 3}]},
              {c:[{v: 'Candelária'}, {v: 1}]},
              {c:[{v: 'Bom Pastor'}, {v: 3}]},
              {c:[{v: 'Barro Vermelho'}, {v: 1}]},
              {c:[{v: 'Bairro Nordeste'}, {v: 3}]},
              {c:[{v: 'Areia Preta'}, {v: 0}]},
              {c:[{v: 'Alecrim'}, {v: 7}]}
             ]
            } ;
 var json51 = {
     cols:[
          {id: '', label: 'Ocorrência', type: 'string'},
          {id: '', label: 'Vias de Fato', type: 'number'},
          {id: '', label: 'Vandalismo', type: 'number'},
          {id: '', label: 'Tráfico', type: 'number'},
          {id: '', label: 'Tentativa de Homicídio', type: 'number'},
          {id: '', label: 'Tentativa de Estrupro', type: 'number'},
          {id: '', label: 'Tentativa de Assalto', type: 'number'},
          {id: '', label: 'Solicitação de Policiamento', type: 'number'},
          {id: '', label: 'Roubo', type: 'number'},
          {id: '', label: 'Prestação de Socorro', type: 'number'},
          {id: '', label: 'Porte Ilegal de Arma', type: 'number'},
          {id: '', label: 'Ocorrência de Trânsito', type: 'number'},
          {id: '', label: 'Lesão Corporal', type: 'number'},
          {id: '', label: 'Homicídio', type: 'number'},
          {id: '', label: 'Furto', type: 'number'},
          {id: '', label: 'Falsidade Ideológica', type: 'number'},
          {id: '', label: 'Estrupo', type: 'number'},
          {id: '', label: 'Desordem', type: 'number'},
          {id: '', label: 'Danos ao Patrimônio Público', type: 'number'},
          {id: '', label: 'Consumo de Entorpecentes', type: 'number'},
          {id: '', label: 'Condução de Aluno até a Residência', type: 'number'},
          {id: '', label: 'Atrito Verbal', type: 'number'},
          {id: '', label: 'Atos Libidinosos', type: 'number'},
          {id: '', label: 'Ato de Suspeição', type: 'number'},
          {id: '', label: 'Assistência Policial', type: 'number'},
          {id: '', label: 'Apoio Policial', type: 'number'},
          {id: '', label: 'Ameaça', type: 'number'},
          {id: '', label: 'Aliciamento de Menor', type: 'number'},
          {id: '', label: 'Agressão', type: 'number'},
          {id: '', label: 'Abordagem à Veículo', type: 'number'}

     ],
     rows:[
        {c:[{v:'Ocorrências'},{v:5},{v:0},{v:4},{v:0},{v:0},{v:0},{v:2},{v:16},{v:1},{v:4}
           ,{v:0},{v:3},{v:1},{v:6},{v:0},{v:1},{v:6},{v:3},{v:7},{v:0}
           ,{v:1},{v:1},{v:10},{v:4},{v:2},{v:11},{v:0},{v:0},{v:1}
           ]}
     ]        
     
 } ;  
 
 var json52 = {
     cols:[
            {id: '', label: 'Bairro', type: 'string'},
            {id: '', label: 'Ocorrências', type: 'number'}

          ],
     rows:[
          {c: [{v:'Vias de Fato'}, {v:5}]},
          {c: [{v:'Vandalismo'}, {v:0}]},
          {c: [{v:'Tráfico'}, {v:4}]},
          {c: [{v:'Tentativa de Homicídio'}, {v:0}]},
          {c: [{v:'Tentativa de Estrupro'},{v:0} ]},
          {c: [{v:'Tentativa de Assalto'}, {v:0}]},
          {c: [{v: 'Solicitação de Policiamento'}, {v:2}]},
          {c: [{v: 'Roubo'}, {v:16}]},
          {c: [{v: 'Prestação de Socorro'}, {v:1}]},
          {c: [{v:'Porte Ilegal de Arma'},{v:4}]},
          {c: [{v:'Ocorrência de Trânsito'},{v:0}]},
          {c: [{v:'Lesão Corporal'},{v:3}]},
          {c: [{v:'Homicídio'},{v:1}]},
          {c: [{v:'Furto'},{v:6}]},
          {c: [{v:'Falsidade Ideológica'},{v:0}]},
          {c: [{v:'Estrupo'},{v:1}]},
          {c: [{v:'Desordem'},{v:6}]},
          {c: [{v:'Danos ao Patrimônio Público'},{v:3}]},
          {c: [{v:'Consumo de Entorpecentes'},{v:7}]},
          {c: [{v:'Condução de Aluno até a Residência'},{v:0}]},
          {c: [{v:'Atrito Verbal'},{v:1}]},
          {c: [{v:'Atos Libidinosos'},{v:1}]},
          {c: [{v:'Ato de Suspeição'},{v:10}]},
          {c: [{v:'Assistência Policial'},{v:4}]},
          {c: [{v:'Apoio Policial'},{v:2}]},
          {c: [{v:'Ameaça'},{v:11}]},
          {c: [{v:'Aliciamento de Menor'},{v:0}]},
          {c: [{v:'Agressão'},{v:0}]},
          {c: [{v:'Abordagem à Veículo'},{v:1}]}      
     ]     
 }

 var json61 ={
         cols:[
            {id: '', label: 'Dias da Semana', type: 'string'},
            {id: '', label: 'Segunda-feira', type: 'number'},
            {id: '', label: 'Terça-feira', type: 'number'},
            {id: '', label: 'Quarta-feira', type: 'number'},
            {id: '', label: 'Quinta-feira', type: 'number'},
            {id: '', label: 'Sexta-feira', type: 'number'},
            {id: '', label: 'Sábado', type: 'number'},
            {id: '', label: 'Domingo', type: 'number'}

   
         ],
         rows:[
           {c:[{v:'Ocorrências'},{v:14},{v:16},{v:19},{v:20},{v:21},{v:0}
               ,{v:0}]} 
         ]
 };
 var json62 ={
    cols:[
          {id: '', label: 'Dias da Semana', type: 'string'},
          {id: '', label: 'Ocorrências', type: 'number'}          
    ],
    rows:[
          {c:[{v:'Segunda-feira'},{v:14}]},
          {c:[{v:'Terça-feira'},{v:16}]},
          {c:[{v:'Quarta-feira'},{v:19}]},
          {c:[{v:'Quinta-feira'},{v:20}]},
          {c:[{v:'Sexta-feira'},{v:21}]},
          {c:[{v:'Sábado'},{v:0}]},
          {c:[{v:'Domingo'},{v:0}]}
    ]
};
 
 var json71 = {
    cols:[
        {id: '', label: 'Horário da Ocorrência', type: 'string'},
        {id: '', label: '23h', type: 'number'},
        {id: '', label: '22h', type: 'number'},
        {id: '', label: '21h', type: 'number'},
        {id: '', label: '20h', type: 'number'},
        {id: '', label: '19h', type: 'number'},
        {id: '', label: '18h', type: 'number'},
        {id: '', label: '17h', type: 'number'},
        {id: '', label: '16h', type: 'number'},
        {id: '', label: '15h', type: 'number'},
        {id: '', label: '14h', type: 'number'},
        {id: '', label: '13h', type: 'number'},
        {id: '', label: '12h', type: 'number'},
        {id: '', label: '11h', type: 'number'},
        {id: '', label: '10h', type: 'number'},
        {id: '', label: '9h', type: 'number'},
        {id: '', label: '8h', type: 'number'},
        {id: '', label: '7h', type: 'number'},
        {id: '', label: '6h', type: 'number'},
        {id: '', label: '5h', type: 'number'},
        {id: '', label: '4h', type: 'number'},
        {id: '', label: '3h', type: 'number'},
        {id: '', label: '2h', type: 'number'},
        {id: '', label: '1h', type: 'number'},
        {id: '', label: '0h', type: 'number'}

    ],
    rows:[
        {c:[{v:''},{v:0},{v:4},{v:2},{v:6},{v:9},{v:4},{v:8},{v:7},{v:10}
            ,{v:9},{v:7},{v:4},{v:4},{v:11},{v:1},{v:4},{v:0},{v:0},{v:0}
        ,{v:0},{v:0},{v:0},{v:0},{v:0}]}
    ]
}; 
 
 var json72 ={
    cols:[
       {id: '', label: 'Horário da Ocorrência', type: 'string'},
       {id: '', label: 'Ocorrência', type: 'number'},
    ],
    rows:[
       {c:[{v:'23h'},{v:0}]},
       {c:[{v:'22h'},{v:4}]},
       {c:[{v:'21h'},{v:2}]},
       {c:[{v:'20h'},{v:6}]},
       {c:[{v:'19h'},{v:9}]},
       {c:[{v:'18h'},{v:4}]},
       {c:[{v:'17h'},{v:8}]},
       {c:[{v:'16h'},{v:7}]},
       {c:[{v:'15h'},{v:10}]},
       {c:[{v:'14h'},{v:9}]},
       {c:[{v:'13h'},{v:7}]},
       {c:[{v:'12h'},{v:4}]},
       {c:[{v:'11h'},{v:4}]},
       {c:[{v:'10h'},{v:11}]},
       {c:[{v:'9h'},{v:1}]},
       {c:[{v:'8h'},{v:4}]},
       {c:[{v:'7h'},{v:0}]},
       {c:[{v:'6h'},{v:0}]},
       {c:[{v:'5h'},{v:0}]},
       {c:[{v:'4h'},{v:0}]},
       {c:[{v:'3h'},{v:0}]},
       {c:[{v:'2h'},{v:0}]},
       {c:[{v:'1h'},{v:0}]},
       {c:[{v:'0h'},{v:0}]}


    ]
}; 

 var jsonE01 = {
     cols: [
             {id: 'local', label: 'Público Alvo', type: 'string'},
             {id: 'local', label: 'Ocorrências', type: 'number'}
         ],
     rows: [
               {c:[{v: 'Estadual'}, {v: 129}]},
               {c:[{v: 'Municipal'}, {v: 36}]},
               {c:[{v: 'Via Pública'}, {v: 102}]},
               {c:[{v: 'Particular'}, {v:52}]},
               {c:[{v: 'Federal'}, {v:1}]}
       ]
            
};

 var jsonE02 = {
     cols: [
             {id: 'local', label: 'Área Ocorrência', type: 'string'},
             {id: 'local', label: 'Ocorrências', type: 'number'}
         ],
     rows: [
               {c:[{v: 'Norte'}, {v: 65}]},
               {c:[{v: 'Sul'}, {v: 62}]},
               {c:[{v: 'Leste'}, {v: 119}]},
               {c:[{v: 'Oeste'}, {v:74}]}
       ]
            
};

//FIM MODELO JSON 
 
function graph1(){
    GeraGraph(json11,'bar_G011','title','tituloV','tituloH',800,400,2,'');
}
function graph21(){
    GeraGraph(json21,'bar_G021','','','',800,400,1);
}
function graph22(){
    GeraGraph(json22,'bar_G022','','','',800,400,1);
}
function graph31(){
    GeraGraph(json31,'bar_G031','','','',800,400,1);
}
function graph32(){
    GeraGraph(json32,'bar_G032','','','',800,400,1);
}
function graph41(){
    GeraGraph(json41,'bar_G041','','Bairros','Quantidade de Ocorrências',1200,1000,1,'bottom');
}
function graph42(){
    GeraGraph(json42,'bar_G042','','Bairros','Quantidade de Ocorrências',1200,1300,1);
}
function graph51(){
    GeraGraph(json51,'bar_G051','Tipos de Ocorrências','','Quantidade de Ocorrências',1200,1300,1);
}
function graph52(){
    GeraGraph(json52,'bar_G052','Tipos de Ocorrências','','Quantidade de Ocorrências',1200,1300,1);
}
function graph61(){
    GeraGraph(json61,'bar_G061','Ocorrências','Dias da Semana','Ocorrências',800,400,1);
}
function graph62(){
    GeraGraph(json62,'bar_G062','Ocorrências','Dias da Semana','Ocorrências',800,400,1);
}
function graph71(){
    GeraGraph(json71,'bar_G071','Ocorrências','Horário do dia','Ocorrências',900,600,1);
}
function graph72(){
    GeraGraph(json72,'bar_G072','Ocorrências','Horário do dia','Ocorrências',900,600,1);
}
function graphE01(){
    GeraGraph(jsonE01,'bar_GE01','Ocorrências','','',800,400,3,'',true);           
}
function graphE02(){
    GeraGraph(jsonE02,'bar_GE02','Ocorrências','','',800,400,3);           
}


function carregaTodos(){
    graph1();
    graph21();
    graph22();
    graph31();
    graph32();
    graph41();
    graph42();
    graph51();
    graph52();
    graph61();
    graph62();
    graph71();
    graph72();
    graphE01();
    graphE02();

}

//Função genérica onde recebe como parametros os dados a serem gerados as options/conf
// para o gráfico e qual local será exibido o gráfico
function GeraGraph(dados,divGera,title,titleVAxis,titlehAxis,width,heigth,modExibicao,legend,tridimensional){
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

