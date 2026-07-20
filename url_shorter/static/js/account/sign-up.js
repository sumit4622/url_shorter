$(document).ready(function () {
    $("#sign-up").hide();
    $("#sign-in").show();
    console.log("Page loaded");
});

// Corrected event listener
$('#handlesubmit').click(function (e) {
    e.preventDefault();
    console.log("Button clicked!");

    var $form = $(this).closest('form');

    $.ajax({
        type: "POST",
        url: $form.attr("action"),
        data: $form.serialize(),
        headers: {
            "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val() // Pass CSRF token explicitly
        },
        success: function (response) {
            console.log("Success:", response);
        },
        error: function (xhr) {
            console.error("Error status:", xhr.status);
            console.error("Server Response:", xhr.responseText); // Prints full Python error trace in browser console
        }
    });
});