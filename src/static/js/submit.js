// This Javascript function serves to submit a POST request to the server and display the resulting page
$(function() {
    $('#submit').click(function() {
        alert("Clicked button");
        $.ajax({
            url: '/generate',
            data: $('form').serialize(),
            type: 'GET',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});