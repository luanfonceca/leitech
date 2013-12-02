// Load the Visualization API and the piechart package.
google.load('visualization', '1.0', {'packages':['corechart']});

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

function draw_report03() {
    $.getJSON("/occurrences/report03", function(json_data){
        data = {
            cols: [{label: 'Ocorências', type: 'string'}],
            rows: [{c: [{v: 'Zonas'}]}]
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
            document.getElementById('id_report03')
        );

        chart.draw(data);
    });
}

function draw_report04() {
    $.getJSON("/occurrences/report04", function(json_data){
        data = {
            cols: [{label: 'Ocorências', type: 'string'}],
            rows: [{c: [{v: 'Bairros'}]}]
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
            document.getElementById('id_report04')
        );

        chart.draw(data);
    });
}

function draw_report05() {
    $.getJSON("/occurrences/report05", function(json_data){
        data = {
            cols: [{label: 'Ocorências', type: 'string'}],
            rows: [{c: [{v: 'Tipos'}]}]
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
        var options = {height: 1200};
        var chart = new google.visualization.BarChart(
            document.getElementById('id_report05')
        );

        chart.draw(data, options);
    });
}

function draw_report06() {
    $.getJSON("/occurrences/report06", function(json_data){
        data = {
            cols: [{label: 'Ocorências', type: 'string'}],
            rows: [{c: [{v: 'Dias da Semana'}]}]
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
        var options = {height: 400};
        var chart = new google.visualization.BarChart(
            document.getElementById('id_report06')
        );

        chart.draw(data, options);
    });
}

function draw_report07() {
    $.getJSON("/occurrences/report07", function(json_data){
        data = {
            cols: [{label: 'Ocorências', type: 'string'}],
            rows: [{c: [{v: 'Hora'}]}]
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
        var options = {height: 1000};
        var chart = new google.visualization.BarChart(
            document.getElementById('id_report07')
        );

        chart.draw(data, options);
    });
}

function draw_reports() {
    var reports = [
        draw_report02, 
        draw_report03,
        draw_report04,
        draw_report05,
        draw_report06,
        draw_report07,
    ];

    for (var i = reports.length - 1; i >= 0; i--) {
        // Set a callback to run when the Google Visualization API is loaded.
        google.setOnLoadCallback(reports[i]);
    };
}

draw_reports();