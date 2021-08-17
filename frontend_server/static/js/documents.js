$(document).ready(function() {
    $("[data-link]").click(function() {
        window.location.href = $(this).attr("data-link");
        return false;
    });
});
