function draw_report02() {
    $.getJSON("/occurrences/report02", function(json_data){
        data = {
            cols: [{label: 'Ocorências', type: 'string'}],
            rows: [{c: [{v: 'Público Atendido'}]}]
        };
        for (var i = json_data.length - 1; i >= 0; i--) {
            data.cols.push({
                label: json_data[i][0], 
                type: 'number'
            });
            data.rows[0].c.push({
                v: json_data[i][1]
            });
        };
        data = new google.visualization.DataTable(data);

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.BarChart(
            document.getElementById('id_report02')
        );
        chart.draw(data);
    });
}

// Load the Visualization API and the piechart package.
google.load('visualization', '1.0', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.setOnLoadCallback(draw_report02);

/*-------------------------------*/

   var data;
   var chart;

      // Load the Visualization API and the piechart package.
      google.load('visualization', '1', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
   //   google.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
//OBS.: os valores podem serem passados como valores ja da porcetagem :D hehe
function drawChart() {
        // Create the data table.
        var json = {
           cols: [
                {id: 'local', label: 'Local Só Deus Sabe', type: 'string'},
                {id: 'local', label: 'Valor', type: 'number'}],
           rows: [{c:[{v: 'Local A'}, {v: 11}]},
              {c:[{v: 'Local B'}, {v: 2}]},
              {c:[{v: 'Local C'}, {v: 2}]},
              {c:[{v: 'Local D'}, {v:2}]},
              {c:[{v: 'Local E'}, {v:7}]}
             ]
            } ;
            
    var data = new google.visualization.DataTable(json);
        
        /*data.addColumn('string');
        data.addColumn('number');
        data.addRows([
          ['Local A', 25],
          ['Local B', 10],
          ['Local C', 30],
          ['Local N', 35]
        ]);*/

        // Set chart options
        var options = {'title':'Grafico modo pizza',
                       'width':600,
                       'height':400,
                        is3D: true
           };

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);
        
        // Instantiate and draw our chart, passing in some options.
        /*var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        google.visualization.events.addListener(chart, 'select', selectHandler);
        chart.draw(data, options);*/
        
}
function selectHandler() {
    var selectedItem = chart.getSelection()[0];
    var value = data.getValue(selectedItem.row, 0);
    alert('The user selected ' + value);
}          
 

 function drawVisualization() {
  /*  var data = new google.visualization.DataTable();
     data.addColumn('string','Bairro');
     data.addColumn('number','Ocorrências');
     data.addRows([
         ['Via Pública',39],
         ['Federal',0],
         ['Particular',13],
         ['Municipal',6],
         ['Estadual',32]
   
     ]);*/
       
     
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
                 
     
     
     var data31 = new google.visualization.DataTable(json31);
     

     /*
     var data3 = google.visualization.arrayToDataTable([
          ['Ocorrência', 'Via Pública', 'Federal', 'Particular', 'Municipal', 'Estadual'],
          ['Ocorrência', 39, 0, 13, 6, 32]
          ]);*/
         var options = {
                  title:"Assaltos registrados",
                  width:800, height:400,
                  vAxis: {title: ""},
                  hAxis: {title: "Número de assaltos"}
           };
        // Create and draw the visualization.
        
           
         var chart31 = new google.visualization.BarChart(document.getElementById('bar_G031'));
           chart31.draw(data31,options);
    
      }
      
//Executa chamada para execução da função drawVisualization e carregamento dos graficos 
google.setOnLoadCallback(drawVisualization);

