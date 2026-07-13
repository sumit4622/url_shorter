$(document).ready(function () {
    $('form').on('submit', function (e) {
        e.preventDefault();

        var $form = $(this);
        // Find the submit button inside this form
        var $submitBtn = $form.find('button[type="submit"]');

        // 1. Change the color to show a "loading" or processed state
        // We remove the old background/hover classes and add the new ones
        $submitBtn
            .removeClass('bg-indigo-500 hover:bg-indigo-400')
            .addClass('bg-emerald-600 hover:bg-emerald-500') // Example: changes to green
            .prop('disabled', true) // Optional: disable to prevent double clicks
            .text('Sending...');   // Optional: change the text status

        // 2. Fire your AJAX request
        $.ajax({
            type: 'POST',
            url: $form.attr('action'),
            data: $form.serialize(),
            success: function (response) {
                console.log("this is workigi");
                // Keep the success color or reset it if needed
                $submitBtn.text('OTP Sent!');
            },
            error: function (xhr) {
                // If it fails, revert back to the original color so they can try again
                $submitBtn
                    .removeClass('bg-emerald-600 hover:bg-emerald-500')
                    .addClass('bg-indigo-500 hover:bg-indigo-400')
                    .prop('disabled', false)
                    .text('Send OTP');

                alert('Something went wrong. Please try again.');
            }
        });
    });
});