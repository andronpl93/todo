var obj={
        type:'POST',
		timeout:5000,
		data:{},
		error:function(){loader.fadeOut();},
		success: undefined,
    };
var loader=$('#preloader');

///Прячет кнопку "добавить",выкатывает форму
$('#centr .add div').click({'sel':'#add_task'},hideBottom);   // для задания
$('#left .add div').click({'sel':'#add_project'},hideBottom);   // для прокта

////Кнопка Готово
$('#add_task  .end').click({'url':'shuban-add/','func':add_form,'cont':'.task','fF':fadeForm,'text': 'Задание успешно ','add':'добавленно','edit':'измененно'},end);
$('#add_project  .end').click({'url':'shuban-add_pr/','func':add_form_pr,'cont':'.project','fF':fadeForm_pr,'text': 'Проект успешно ','add':'добавлен','edit':'изменен'},end);


/// Кнопка Отмена
$('#add_task  .esc').click({'fF':fadeForm,'cont':'.tasks'},esc);
$('#add_project  .esc').click({'fF':fadeForm_pr,'cont':'.project'},esc);


 ///        выкатывает меню в шапке записи
$('#centr').on('click','.menu',{'fF':fadeForm,'contId':'#add_task'},men);
$('#left').on('click','.menu',{'fF':fadeForm_pr,'contId':'#add_project'},men);

////  закатывает меню обратно
$('#centr').on('click','.menu > span:last-child',{'fF':fadeForm,'contId':'#add_task','cont':'.tasks'},menu_esc);
$('#left').on('click','.menu > span:last-child',{'fF':fadeForm_pr,'contId':'#add_project','cont':'.project'},menu_esc);


$('#centr').on('click','.menu > span:first-child',function(e){  // Кнопка "изменить запись". Подтягивает форму для изменения. Отправлять форму будет кнопка на самой форме
        e.stopPropagation();
        var head=$(this).parents('.tasks > header');
        var form=$('#add_task');
        $(this).parents('.tasks').append(form);
        form.show();
        $('.taskName',$(this).parents('.tasks')).hide();
        //приоритет
        $('input[name=priority][value='+$('.priority',head).attr('data-prior')+"]").attr('checked','checked');
        //Проект
        $('option[value='+$('.projectName',head).attr('data-proj')+']',form).attr('selected','selected');
        $('#add_name',form).val($('.taskName',head.parents('.tasks')).text());
        $('#add_datetime',form).val($('span[date-datime]',head.parents('.tasks')).text());
        form.attr('data-id',head.parent('.tasks').attr('data-id'));


});
$('#left').on('click','.menu > span:first-child',function(e){  // Кнопка "изменить запись". Подтягивает форму для изменения. Отправлять форму будет кнопка на самой форме
        e.stopPropagation();
        var form=$('#add_project');
        $(this).parents('.project').append(form);
        form.show();
        $('>div:first-child',$(this).parents('.project')).css('visibility','hidden');
        $('.icon',form).attr('data-num',$('.icon',$(this).parents('.project')).attr('data-num'));
        form.attr('data-id',$(this).parents('.project').attr('data-id'));
        icone('.project');
        $('#add_name_pr').val( $('.name',$(this).parents('.project')).text());



});

$('#centr').on('click','.menu > span:nth-child(2)',function(e){
         e.stopPropagation();
         var self=$(this);
         obj.url='shuban-del-task/';
         obj.data={'id_task':self.parents('.tasks').attr('data-id')};
         obj.success=function(){
             massage('Задание успешно удаленно',1000);
             load_content();
        };
        $.ajax(obj);
});
$('#left').on('click','.menu > span:nth-child(2)',function(e){
         e.stopPropagation();
         var self=$(this);
         obj.url='shuban-del-pr/';
         obj.data={'id_pr':self.parents('.project').attr('data-id')};
         obj.success=function(e){
            if(e=='1'){
                massage('Проект успешно удален',1500);
                load_content();
                load_projects();
            }else{
                massage('Невозможно удалить проект у которого есть незавершенные задачи',3500);
            }

        };
        $.ajax(obj);
});

function fadeForm(self){
    $('input[name=priority]:checked').removeAttr("checked");$('#add_name').val('');$('#add_datetime').val('');
    self.parents('#add_task').fadeOut(100);
    $('div:last-child',self.parents('.add')).fadeIn(100);
    $('.taskName',self.parents('.tasks')).show();
    $('#add_task').appendTo('body');
};

function fadeForm_pr(self){
    $('#add_name_pr').val('');$('#add_project .icon').attr('data-num','1');
    self.parents('#add_project').fadeOut(100);
    $('div:last-child',self.parents('.add')).fadeIn(100);
    $('>div:first-child',self.parents('.project')).css('visibility','visible');
    $('#add_project').appendTo('body');
};

function add_form(){
    obj.data={}
    obj.data.priority=$('input[name=priority]:checked').val();
    obj.data.project=$('#add_task option[value]:selected').val();
    obj.data.name=$('#add_name').val();
    obj.data.pub_date=$('#add_datetime').val();


    for(var key in obj.data){
        if (!obj.data[key]){
            massage('Все поля обязательны для заполнения');
            return 0;
        }
    }
    if($('#add_task').attr('data-id')){
                obj.data.id_tasks=$('#add_task').attr('data-id');
                return 2;// выведет запись успешно "измененна"
    }
    return 1; // выведет запись успешно Добавленна

}
function add_form_pr(){
    obj.data={}
    obj.data.name=$('#add_name_pr').val();
    obj.data.img=$('#add_project .icon').attr('data-num');

    if (!obj.data.name){
            massage('Введите название',1000);
            return 0;
    }
    if($('#add_project').attr('data-id')){
                obj.data.id_project=$('#add_project').attr('data-id');
                return 2;   // выведет запись успешно "измененна"
    }
    return 1;  // выведет запись успешно Добавленна
};
function massage(str,time){
    time=time || 2000;
    $('#error_message').html(str);
    $("#error_box").fadeIn(500).delay(time).fadeOut(500);

};

function hideBottom(e){
    e.stopPropagation();
    var self=$(this).parent('.add');
    $('div:last-child',self).fadeOut(function(){
        $(e.data.sel).prependTo(self).fadeIn(300);
    });

};
function end (e){///   кнопка "Готово" на форме добавления-изменения
    e.stopPropagation();
    self=$(this);
    if (e.data.func()==0)    // заполняет data хламом из формы
        return 0
    else if (e.data.func()==1)
            e.data.text+=e.data.add
        else
            e.data.text+=e.data.edit
    obj.url=e.data.url;
    obj.success=function(){
        load_content();    //грyзит контент в цетр
        icone(e.data.cont);
        e.data.fF(self);   // прячет форму добавления\изменения и возвращает кнопку "добавить"
        massage(e.data.text,1000);
        load_projects();
    };
    $.ajax(obj);
};

function esc(e){//// прячет форму
     e.stopPropagation();
     e.data.fF($(this));
     $('.menu.menu_act').removeClass('menu_act');
}

function men(e){

    e.stopPropagation();
    $('.menu.menu_act').removeClass('menu_act');
    e.data.fF($(e.data.contId+' .esc'));
    $(this).addClass('menu_act');
};
function menu_esc(e){
    e.stopPropagation();
    $(this).parents('.menu').removeClass('menu_act');
    e.data.fF($(e.data.contId+' .esc'));
    $('.menu',$(e.data.contId).parents(e.data.cont)).removeClass('menu_act');
};