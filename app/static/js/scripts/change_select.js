// change_select.js

// Меняет содержимое вобора города в зависимости от выброного региона

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

var j = jQuery.noConflict();

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

j(function() {
    var state_select = j('#region');
    var city_select = j('#city'); 
  

    state_select.change(function() {
        var state = state_select.val();
        var action = '/comment/region/' + state;
        var method = 'GET';
        
        j.ajax({
            url: action,
            type: method,
            data: {}
        }).done(function(data) {
            var optionHTML = '';
            for (var city in data.cities) {
                var id = data.cities[city].id;
                var title = data.cities[city].title;
                optionHTML += '<option value="'+id+'">'+title+'</option>';
            }

            city_select.html(optionHTML)

        }).fail(function(data) {
            console.log(data);
        });
    });

})
