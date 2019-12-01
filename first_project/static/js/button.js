
var tables = $('.charge-table');
$('input[name="group1"]').on('change', function() {
tables.hide();
$('#' + $(this).val()).show();
});
