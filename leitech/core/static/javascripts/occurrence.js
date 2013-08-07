/* ---------- Custom JS ---------- */
$('.add-formset').on("click", function(){
	var regex = new RegExp('(-\\d+-)');
	var elemt_filters = 'input, select';

	var new_index = "-" + $("#id_travelers-TOTAL_FORMS").val() + "-";
	
	var tbody = $(".table-formset").children('tbody');
	var tr_base = tbody.children('tr:first');

	var tr_cloned = tr_base.clone();
	var tds_cloned = tr_cloned.children('td');
	for (var i = tds_cloned.length - 1; i >= 0; i--) {
		var element = $(tds_cloned[i]).children('input, select');

		if (element.attr('id')){
			var new_name = element.attr('name').replace(regex, new_index);
			element.attr('name', new_name);

			var new_id = element.attr('id').replace(regex, new_index);
			element.attr('id', new_id);
			element.attr('value', '');
		}
	}

	tr_cloned.insertBefore('tr.actions-formset');
	var new_total = $("#id_travelers-TOTAL_FORMS").val();
	$("#id_travelers-TOTAL_FORMS").val(parseInt(new_total) + 1);
});

$(".del-formset").on("click", function(){
	if ($(".table-formset tr").length > 3){
		$(this).parents('tr').remove();
		var old_total = $("#id_travelers-TOTAL_FORMS").val();
		var new_total = parseInt(old_total) - 1;
		$("#id_travelers-TOTAL_FORMS").val(new_total);
	};
});