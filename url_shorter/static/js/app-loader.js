$(function () {
    let path = window.location.pathname;
    console.log(path);

    path = path.replace(/^\/|\/$/g, "");
    console.log(path);


    if (path === "") {
        path = "url_shorter/app";   // Change this to your homepage JS
    }

    // Build the JS file path
    const script = "/static/js/" + path + ".js";

    console.log(script);

    $.getScript(script)
        .done(function () {
            console.log("Loaded:", script);
        })
        .fail(function () {
            console.log("No JS file found:", script);
        });

});