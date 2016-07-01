$(document).ready(function() {
    $('#likes').click(function(){
        var catid;
        catid = $(this).attr("data-catid");
        console.log(catid)
        $.get('/storehouse/like_views/', {category_id: catid}, function(data){
                   $('#like_count').html(data);
                   $('#likes').hide();
        });
    });
});

