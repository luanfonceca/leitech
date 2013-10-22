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