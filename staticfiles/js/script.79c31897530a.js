// Navbar script - to activate dropdown toogle
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


// This will show or hide the [Login/Logout/Write a Review/Pending Reviews/Products/Incoming Messages] buttons according to the user_token and user_type of the user.
change_buttons_behaviors();


