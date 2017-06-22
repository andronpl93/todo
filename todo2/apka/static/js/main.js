$('#logout').click(function(){
    $(this).parent('form').submit();
});

var loader=$('#preloader');
loader.fadeOut();


$('#add_datetime').datepicker({dateFormat: 'yy-mm-dd T'}).timePicker();
