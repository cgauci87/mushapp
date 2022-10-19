// Navbar script
document.querySelectorAll(".dropdown-toggle").forEach((item) => {
    item.addEventListener("click", (event) => {
        if (event.target.classList.contains("dropdown-toggle")) {
            event.target.classList.toggle("toggle-change");
        } else if (
            event.target.parentElement.classList.contains("dropdown-toggle")
        ) {
            event.target.parentElement.classList.toggle("toggle-change");
        }
    });
});


// Product Reviews - show div on click

change_buttons_behaviors();
//Show Div On Click
$(document).ready(function () {
    $(".reveal-click-reishi").click(function () {
        get_product_detail();
        $("#testimonials-reishi").show();
        $("#testimonials-reishi").css('display', 'flex');
        $("#testimonials-reishi").get(0).scrollIntoView();
    });
});

$(document).ready(function () {
    $("#reveal-click-lionsmane").click(function () {
        $("#testimonials-lionsmane").show();
        $("#testimonials-lionsmane").css('display', 'flex');
        $("#testimonials-lionsmane").get(0).scrollIntoView();
    });
});

$(document).ready(function () {
    $("#reveal-click-oyster").click(function () {
        $("#testimonials-oyster").show();
        $("#testimonials-oyster").css('display', 'flex');
        $("#testimonials-oyster").get(0).scrollIntoView();
    });
});

$(document).ready(function () {
    $("#reveal-click-enoki").click(function () {
        $("#testimonials-enoki").show();
        $("#testimonials-enoki").css('display', 'flex');
        $("#testimonials-enoki").get(0).scrollIntoView();
    });
});

$(document).ready(function () {
    $("#reveal-click-kingoyster").click(function () {
        $("#testimonials-kingoyster").show();
        $("#testimonials-kingoyster").css('display', 'flex');
        $("#testimonials-kingoyster").get(0).scrollIntoView();
    });
});

$(document).ready(function () {
    $("#reveal-click-goldenoyster").click(function () {
        $("#testimonials-goldenoyster").show();
        $("#testimonials-goldenoyster").css('display', 'flex');
        $("#testimonials-goldenoyster").get(0).scrollIntoView();
    });
});

