$.get( "shuban-projects/", function( data ) {
        $('#left > div').html(data);
        icone('.project');

});

$.get( "shuban-tasks/", function( data ) {
        $('#centr').html(data);
       /// icone('.project');

});


function icone(context){
    var h,numIcon,sizeIcon=parseInt($('.icon:first-child',context).css('height'));
    $('.icon',context).each(function(){
            numIcon=$(this).attr('data-num');
            $(this).css({
                'min-width': sizeIcon+'px',
                'background-size':  sizeIcon*6+'px '+sizeIcon*3+'px',
                'background-position': -(Math.floor((numIcon)%6)*sizeIcon)+'px '+(-Math.floor(numIcon/6)*sizeIcon)+'px',
            });
    });

}
