$('#logout').click(function(){
    $(this).parent('form').submit();
});

var loader=$('#preloader');
loader.fadeOut();


$('#add_datetime').datepicker({dateFormat: 'yy-mm-dd T'}).timePicker();

var text='';
for(var i=0;i<18;i++){
    text+='<div class="shadow"></div>';
}
$('#icon_panel').html(text);

if (String(window.location.href).includes('archive')){
     $('#archive').addClass('active');
}

