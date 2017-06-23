$('#centr').on('click','.check',function(){
    var self=$(this);
    var obj={
        type:'POST',
		timeout:5000,
		data:{'id':self.parents('.tasks').attr('data-id'),
		        'status':self.attr('data-status')},
		error:function(){loader.fadeOut();},
		url:'shuban-id/',
		success:function(data){
		    self.attr('data-status',data);
		    a=data=="True" && 'line-through' || 'None';
		    $('.taskName',self.parents('.tasks')).css('text-decoration',a);
		    loader.fadeOut(200);
		    load_projects();
		    load_content();
		},
    };
    $.ajax(obj);
});

