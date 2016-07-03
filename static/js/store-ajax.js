$(document).ready(function() {
    $('#likes').click(function(){
        var catid;
        catid = $(this).attr("data-catid");
        console.log(catid)
        $.get('/storehouse/like_category/', {category_id: catid}, function(data){
                   $('#like_count').html(data);
                   $('#likes').hide();
                   alert('zalajkowales brawo');
        });
    });

    $('#item_name').blur(function(){
        var newname;

        newname = $(this).attr('value');
        newname = $(this).val()
        console.log('new name ', newname);
        $.get('/storehouse/check_name/', {newviewname: newname}, function(data){
            $('#namealert').html(data);
        });
    });
});

