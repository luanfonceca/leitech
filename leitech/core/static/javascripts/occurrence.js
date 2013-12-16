/* ---------- Custom JS ---------- */
$('.add-formset').on("click", function(){
	var regex = new RegExp('(-\\d+-)');
	var elemt_filters = 'input, select';

	var new_index = "-" + $("#id_occurrence_seized_material-TOTAL_FORMS").val() + "-";
	
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
	var new_total = $("#id_occurrence_seized_material-TOTAL_FORMS").val();
	$("#id_occurrence_seized_material-TOTAL_FORMS").val(parseInt(new_total) + 1);
});

$(".del-formset").on("click", function(){
	if ($(".table-formset tr").length > 3){
		$(this).parents('tr').remove();
		var old_total = $("#id_occurrence_seized_material-TOTAL_FORMS").val();
		var new_total = parseInt(old_total) - 1;
		$("#id_occurrence_seized_material-TOTAL_FORMS").val(new_total);
	};
});

// var address_fields = [
// 	"#id_state", "#id_city", "#id_neighborhood", 
// 	"#id_zipcode", "#id_street", "#id_complement", 
// 	"#id_number", "#id_region"
// ];
// for (var i = address_fields.length - 1; i >= 0; i--) {
// 	$(address_fields[i]).parents('.control-group').hide()
// };

// $("#id_attended_public").change(function() {
// 	var choice = $(this).find(
// 		'option[value="'+ $(this).val() + '"]'
// 	).text().toLowerCase();

// 	if (choice == "via pública" && !$("#id_school").val()) {
// 		for (var i = address_fields.length - 1; i >= 0; i--) {
// 			$(address_fields[i]).parents('.control-group').show()
// 		};
// 	} else {
// 		for (var i = address_fields.length - 1; i >= 0; i--) {
// 			$(address_fields[i]).parents('.control-group').hide()
// 		};
// 	};
// });