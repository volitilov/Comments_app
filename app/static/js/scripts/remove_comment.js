// remove_comment.js

// тихое удаление комментария с помощью ajax

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

var j = jQuery.noConflict();

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

j(function() {
    j('.delComment_btn').click(function(event) {
        var target = event.target || window.event.target;
        var parent = target.parentNode.parentNode;
        var comment_id = parent.id;

        j.ajax({
            url: '/comment/'+comment_id+'...del',
            type: 'POST'
        }).done(function(response) {
            if (response['success']) {
                parent.style.display = 'none';
            }
        })

    })
})
