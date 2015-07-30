var page = 0    // default starting page (most recent posts)
loadPosts()     // page 0 of posts is is loaded automatically



// $('#create-post-button').click(function(e) {

//     e.preventDefault()  // prevent the form from being submitted normally

//     $.ajax({
//         url: '/create-post/',
//         method: 'POST',
//         beforeSend: function(xhr) {
//             xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
//         },
//         success: function() {
//             $('li[data-post-id="' + id + '"]').remove()
//             var current_id = $('#post-form input[name="id"]').val()
//             if (id === current_id) {
//                 clear_form()
//             }
//         }
//     })
// })


// ====================
// clear submission form
// ====================

// function clear_form() {
//     $('#post-form input')
// }


/**
 * Listens for clicks on the 'load older posts' button.  Default behavior is
 * suppressed, the global page counter is incremented, and the loadPosts
 * function is called.
 */
$('#load-older-posts').click(function(e) {
    e.preventDefault()
    page++
    loadPosts()
})


/**
 * Calls 'get-posts/' with global variable 'page' as a GET parameter. If a
 * non-zero length result is returned by django, appends the older posts to
 * the bottom of the page.  If the result IS length zero, this is announced
 * with a message and the 'load older posts' button is hidden.
 */
function loadPosts() {
    $.ajax({
        url: '/main/get-posts/',
        data: {
            page: page
        },
        success: function(result) {
            console.log(result.length)
            if (result.length === 0) {
                $('#posts').append('<p class="text-center">No more posts to load.</p>')
                $('#load-older-posts').hide()
            } else {
                $('#posts').append(result)
            }
        }
    })
}


$('#posts').on('click', '.favorite-button', function() {
    favorite(this)
})


$('#posts').on('click', '.unfavorite-button', function() {
    unfavorite(this)
})


/**
 *
 */
function favorite(button) {

    var post = button.closest('.post')
    var id = $(post).attr('data-post-id')

    $.ajax({
        url: '/main/create-favorite/',
        method: 'POST',
        data: {
            id: id
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
        },
        success: function() {
            $(button).removeClass('flaticon-favourite24')
            $(button).removeClass('favorite-button')
            $(button).addClass('flaticon-bookmark50')
            $(button).addClass('unfavorite-button')
        },
    })
}


/**
 *
 */
function unfavorite(button) {

    var post = button.closest('.post')
    var id = $(post).attr('data-post-id')

    $.ajax({
        url: '/main/delete-favorite/',
        method: 'POST',
        data: {
            id: id
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
        },
        success: function() {
            $(button).removeClass('flaticon-bookmark50')
            $(button).removeClass('unfavorite-button')
            $(button).addClass('flaticon-favourite24')
            $(button).addClass('favorite-button')
        },
    })
}



// get the cookie containing the CSRF token (needed for POSTing with ajax)
function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}