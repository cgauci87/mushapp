var apiBaseUrl = window.location.origin; //BaseURL
var userRegistrationUrl = apiBaseUrl + "/users/registration/"; // Sign Up API URL
var userLoginUrl = apiBaseUrl + "/users/sign-in/"; // Sign In API URL
var productUrl = apiBaseUrl + "/products/get-all-products"; // Get all Products API URL
var writeAreviewUrl = apiBaseUrl + "/products/user-review"; // Post the review by user API URL
var productDetailUrl = apiBaseUrl + "/products/product-detail?id="; // Get Products Details, Rating and Review API URL
var pendingProductReviewUrl = apiBaseUrl + "/admin-app/reviews" // Get list of Unapproved reivews and Apporval of reviews by admin API URL
var userProfileUrl = apiBaseUrl + "/users/profile"
var CRUDProductUrl = apiBaseUrl + "/products/";
var ToggleProductUrl = apiBaseUrl + "/products/toggle-product";
var ContactUsUrl = apiBaseUrl + "/users/contact-us";
var changeCurrentPassword = apiBaseUrl + "/users/change-password";
var forgotPasswordEmail = apiBaseUrl + "/users/forgot-password";

// COOKIES

function setCookie(cname, cvalue, exdays) { //Set cookie (cookie name, cookie value and expiry)
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) { // Get cookie value function
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

// Sign Up API Call Function
function registerUser() {
    var $inputs = $('#user-registration-form :input'); // Get Data from user form by its inputs
    var data = {};
    $inputs.each(function () { // Iterate each input and get the values by it name
        data[this.name] = $(this).val();
    });
    $.ajax({ // Ajax API call
        url: userRegistrationUrl, // API URL
        type: 'POST', // API Method
        contentType: 'application/json', // Request Data Type in header
        data: JSON.stringify(data), // Parse data into json before sending it to backend
        dataType: 'json', // The data type of body is json
        async: false,
        success: function (resp) {
            console.log(resp);
            alert("You account has been created successfully.")
            window.location.href = "login.html";
        },
        error: function (resp) {
            console.log(resp);
            alert(resp.message); // show error message on API failing
        }
    });
}

function contactUsFrom() {
    var $inputs = $('#user-contactus-form :input'); // Get Data from user form by its inputs
    var data = {};
    $inputs.each(function () { // Iterate each input and get the values by it name
        data[this.name] = $(this).val();
    });
    $.ajax({ // Ajax API call
        url: ContactUsUrl, // API URL
        type: 'POST', // API Method
        contentType: 'application/json', // Request Data Type in header
        data: JSON.stringify(data), // Parse data into json before sending it to backend
        dataType: 'json', // The data type of body is json
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            alert("Thank you for getting in touch!");
            window.location.href = 'index.html'; // on success show message of api
            // redirect to login page
        },
        error: function (resp) {
            console.log(resp);
            alert(resp.message); // show error message on API failing
        }
    });
}

function get_messages() {
    user_type = getCookie("user_type");
    user_token = getCookie("token");

    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }

    if (user_type == 1) {
        $.ajax({
            url: ContactUsUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            async: false,
            success: function (resp) {
                console.log(resp);
                // showing response message
                payload = resp.payload;

                console.log(payload);
                $('#messages_list_table').empty();
                if (payload.length > 0) {
                    $('#messages_list_table').empty();
                    for (var i = 0; i < payload.length; i++) {
                        var message = payload[i];
                        $("#messages_list_table").append(
                            '<tr>' +
                            '<td class="table-column-pr-0">' +
                            '<div class="custom-control">' +
                            '<label class="" for=""></label>' +
                            '</div>' +
                            '</td>' +
                            '<td>' + message.created_at + '</td>' +
                            '<td>' + message.email + '</td>' +
                            '<td>' + message.first_name + '</td>' +
                            '<td>' + message.last_name + '</td>' +
                            '<td>' + message.message + '</td>' +
                            '<td>' +
                            '<div class="btn-group" role="group">' +
                            '<a onclick="delete_message(' + message.id + ')" class="btn btn-sm btn-danger">' +
                            '<i class="tio-delete-outlined"></i> Delete' +
                            '</a>' +
                            '</div>' +
                            '</td>' +
                            '</tr>'
                        )

                    }
                }
            },
            error: function (resp) {
                console.log(resp);
                return []
            }
        });
    } else
        $.ajax({
            url: ContactUsUrl, // url
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Insufficient Privileges"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });
}


function loginUser() {
    var $inputs = $('#user-login-form :input');
    var data = {};
    $inputs.each(function () {
        data[this.name] = $(this).val();
    });
    $.ajax({
        url: userLoginUrl,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        dataType: 'json',
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            token = resp.payload.token; // save token in local storage
            setCookie("token", token, 365)
            setCookie("user_type", resp.payload.user_type); // The user type will be stored for authorization, 3 General User, 1 Superadmin
            alert(resp.message);
            // redirect to login page
            window.location.href = "index.html";
            return false;
        },
        error: function (xhr, status, error) {
            var err = eval("(" + xhr.responseText + ")");
            alert(err.message);
        }
    });
}
// To pull data related to products , all mushroom types and display it in carousel
function get_all_products_for_user() {
    var headers = {};
    $.ajax({ //using AJAX
        url: productUrl,
        type: 'GET',
        contentType: 'application/json',
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            payload = resp.payload;
            console.log(payload);
            for (var i = 0; i < payload.length; i++) {
                var product = payload[i]; // Show All products in sliders including images of cloudinary media uploaded by admin
                $('#news-slider').append('<div class="post-slide"> <div class="post-img"><img src="' + product.image + '"alt="Mushroom Image"> <a href="#" class="over-layer"><i class="fa fa-link"></i></a></div><div class="post-content"><h3 class="post-title"><a href="#">' + payload[i].title + '</a></h3><p class="post-description">' + payload[i].description + '</p> <a onclick="save_product_id(' + payload[i].id + ')" class="read-more reveal-click-reishi">Reviews</a></div></div>');
                $('#write_review_product_dropdown').append('<option value="' + payload[i].id + '">' + payload[i].title + '</option>'); // show all product in write review dropdown
            }
        },
        error: function (resp) {
            console.log(resp);
            return []
        }
    });
}
// copy
function write_a_review() {
    user_token = getCookie("token");
    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }
    if (user_token == "") {
        $.ajax({
            url: writeAreviewUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Please login first"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });

    } else
        var $inputs = $('#write-a-review-form :input');
    var data = {};
    $inputs.each(function () {
        data[this.name] = $(this).val();
    });
    data.rating = getCookie("rating"); // Get the rating from the cookie data
    $.ajax({
        url: writeAreviewUrl,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            alert("Success, Once the admin approves your review, it will be displayed on the website");
            // redirect to layout page
            window.location.href = "index.html";
        },
        error: function (resp) {
            console.log(resp);
            alert(resp.message);
        }
    });
}

function get_all_products_reviews_for_user() {
    user_type = getCookie("user_type");
    user_token = getCookie("token");

    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }

    if (user_type == 1) {
        $.ajax({ //using AJAX
            url: pendingProductReviewUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            success: function (resp) {
                console.log(resp); // showing response message
                payload = resp.payload;
                console.log(payload);

                // the loop show the unapproved reviews on Table, Only the admin is authorized to approve or reject it.
                for (var i = 0; i < payload.length; i++) {
                    $('#pending_review_list_id').append(
                        '<tr>' +
                        '<td>' + payload[i].created_at + '</td>' +
                        '<td>' + payload[i].username + '</td>' +
                        '<td>' + payload[i].product + '</td>' +
                        '<td>' + payload[i].comment + '</td>' +
                        '<td>' + payload[i].rating + '</td>' +
                        '<td>Pending</td>' +
                        '<td><button onclick="approve_or_disapprove_review(' + payload[i].id + ',' + 1 + ')">Approve</button></td>' +
                        '<td><button onclick="approve_or_disapprove_review(' + payload[i].id + ',' + 2 + ')">Disapprove</button></td>' +
                        '</tr>'

                    )
                }
            },
            error: function (resp) {
                console.log(resp);
                return []
            }
        });
    } else
        $.ajax({
            url: pendingProductReviewUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Insufficient Privileges"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });
}


// save the rating value in cookie from write review.html, and this value will be use in 'write_a_review()' function
function save_rating(value) {
    setCookie("rating", value, 365);
}


// function is show the whole information regarding product, user review on it, average rating, 1,2,3,4 and 5 rating in percentage sepratly etc
function get_product_detail() {
    var token = getCookie("token");
    var headers = {};
    $.ajax({
        url: productDetailUrl + getCookie("product_id"),
        type: 'GET',
        contentType: 'application/json',
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            payload = resp.payload;
            console.log(payload);

            $('#product_detail_title').text('');
            $('#product_detail_average_rating').text('');
            $('#product_detail_total_reviews_count').text(0);
            $('#reviews_percentage').text(0);
            $('.review_graph_circle').css({
                'transform': 'rotate(' + 0 + 'deg)'
            });
            $('#users-testimonial-box').text('');

            $('#review_one_stars').text(0 + '%');
            $('#review_two_stars').text(0 + '%');
            $('#review_three_stars').text(0 + '%');
            $('#review_four_stars').text(0 + '%');
            $('#review_five_stars').text(0 + '%');

            $('#div_review_one_stars').css({
                "width": 0 + '%'
            });
            $('#div_review_two_stars').css({
                "width": 0 + '%'
            });
            $('#div_review_three_stars').css({
                "width": 0 + '%'
            });
            $('#div_review_four_stars').css({
                "width": 0 + '%'
            });
            $('#div_review_five_stars').css({
                "width": 0 + '%'
            });



            // setting the main detail of product
            $('#product_detail_title').text(payload.title);
            $('#product_detail_average_rating').text(payload.average_rating);
            $('#product_detail_total_reviews_count').text(payload.total_reviews_count);
            $('#reviews_percentage').text(payload.reviews_percentage);
            $('.review_graph_circle').css({
                'transform': 'rotate(' + payload.graph_circle + 'deg)'
            });
            $('#users-testimonial-box').text('');


            // Show the average stars
            var reviews_i = "";
            for (var k = 0; k < payload.average_rating; k++) {
                reviews_i = reviews_i + '<i class="fas fa-star"></i>';
            }
            var reminder = 5 - payload.average_rating;
            reminder = Math.floor(reminder);
            for (var j = 0; j < reminder; j++) {
                reviews_i = reviews_i + '<i class="far fa-star"></i>';
            }
            $("#product_detail_average_rating_star_list").text("")
            $("#product_detail_average_rating_star_list").append(reviews_i)



            if (payload.average_rating < 1) {
                $('#users-testimonial-box').append('<p>No Reviews</p>')
                return false;
            }

            var one_star_count = payload.total_reviews.one_star_count;
            var two_star_count = payload.total_reviews.two_star_count;
            var three_star_count = payload.total_reviews.three_star_count;
            var four_star_count = payload.total_reviews.four_star_count;
            var five_star_count = payload.total_reviews.five_star_count;


            // Showing the 1,2,3,4 and 5 stars in percentage
            $('#review_one_stars').text(one_star_count + '%');
            $('#review_two_stars').text(two_star_count + '%');
            $('#review_three_stars').text(three_star_count + '%');
            $('#review_four_stars').text(four_star_count + '%');
            $('#review_five_stars').text(five_star_count + '%');

            $('#div_review_one_stars').css({
                "width": one_star_count + '%'
            });
            $('#div_review_two_stars').css({
                "width": two_star_count + '%'
            });
            $('#div_review_three_stars').css({
                "width": three_star_count + '%'
            });
            $('#div_review_four_stars').css({
                "width": four_star_count + '%'
            });
            $('#div_review_five_stars').css({
                "width": five_star_count + '%'
            });

            for (var i = 0; i < payload.user_reviews.length; i++) {
                //                console.log(payload.user_reviews[i].date);

                var reviews_i = "";
                for (var j = 0; j < payload.user_reviews[i].rating; j++) {
                    reviews_i = reviews_i + '<i class="fas fa-star"></i>';
                }
                var reminder = 5 - payload.user_reviews[i].rating;
                for (var j = 0; j < reminder; j++) {
                    reviews_i = reviews_i + '<i class="far fa-star"></i>';
                }


                // Showing users review, skills, country, comment and user detail
                if (payload.user_reviews[i].profile_image != "") {
                    user_image = payload.user_reviews[i].profile_image;
                } else {
                    user_image = ("/static/images/user-default-avatar.png");
                }
                $('#users-testimonial-box').append(
                    '<div class="testimonial-box">' +
                    '<div class="box-top">' +
                    ' <div class="profile">' +
                    '  <div class="profile-img">' +
                    '  <img src="' + user_image + '" alt="avatar" />' +
                    ' </div>' +
                    '<div class="name-user">' +
                    '<strong>' + payload.user_reviews[i].full_name + '</strong>' +
                    '<span>@' + payload.user_reviews[i].username + '</span>' +
                    '</div>' +
                    '<div class="location-user">' +
                    '<i class="fa-solid fa-location-dot"></i><span>' + payload.user_reviews[i].location + '</span>' +
                    '</div>' +
                    '<div class="date-submitted">' +
                    '<i class="fa-regular fa-clock"></i><span>' + payload.user_reviews[i].date + '</span>' +
                    '</div>' +
                    '</div>' +
                    '<div class="reviews">' +
                    reviews_i +
                    '</div>' +
                    '</div>' +
                    '<div class="client-comment">' +
                    '<p>' + payload.user_reviews[i].comment + '</p>' +
                    '</div>' +
                    '<div class="tags">' +
                    '<span>' + payload.user_reviews[i].category + '</span>' +
                    '<span>' + payload.user_reviews[i].session + '</span>' +
                    '<span>' + payload.user_reviews[i].skill_level + '</span>' +
                    '</div>' +
                    '</div>'
                )
            }


        },
        error: function (resp) {
            console.log(resp);
            return []
        }
    });
}

// Saving the product id in cookie once user click on product and visit to detail page. the product id will be used in 'get_product_detail()' function
function save_product_id(product_id) {
    setCookie("product_id", product_id, 365);
}


//logout, this function will expires all the values in cookie.
function logout() {
    // clear coookes
    setCookie("token", "", 365)
    setCookie("product_id", "", 365)
    setCookie("rating", "", 365)
    setCookie("user_type", "", 365)
    setCookie("edit_product_id", "", 365)
    alert("Logout Successfully.")
}

// this will hide and show the login/logout/write review according login and logout functionality. and show pending reveiew buttons according user type (3) admin
function change_buttons_behaviors(button) {
    user_type = getCookie("user_type");
    user_token = getCookie("token");
    if (user_token == "") {
        $('#footer-buttons').append(
            '<li class="list-inline-item"><a href="login.html" class="btn btn-light">Write a Review</a></li>'
        )
        $('#user_auth_dropdown').append(
            '<a class="dropdown-item" href="login.html"><i class="fas fa-sign-out-alt fa-fw"></i> Log In</a>'
        )
    } else {
        $('#footer-buttons').append(
            '<li class="list-inline-item"><a href="write-a-review.html" type="button" class="btn btn-outline-light">Write a Review</a></li>'
        )
        $('#user_auth_dropdown').append(
            '<a class="dropdown-item" href="login.html" onclick="logout()"><i class="fas fa-sign-out-alt fa-fw"></i> Log out</a>'
        )
        $('#user_auth_account').append(
            '<a class="dropdown-item" href="usr-account.html"><i class="fas fa-sliders-h fa-fw"></i> My Mush! Account</a>'
        )

    }

    if (user_type == 1) {
        $('#footer-buttons').append(
            '<li class="list-inline-item"><a href="approve-reviews.html" class="btn btn-outline-light">Pending Reviews</a></li>' +
            '<li class="list-inline-item"><a href="products.html" class="btn btn-outline-light">Products</a></li>' +
            '<li class="list-inline-item"><a href="contact-us-admin.html" class="btn btn-outline-light">Incoming Messages</a></li>'
        )
    }
}

// approve or reject the reviews by admin, just pass the review id and status(2 approved, 3 rejected)
function approve_or_disapprove_review(review_id, status) {
    var token = getCookie("token");
    var headers = {
        'Authorization': 'Token ' + token //Authentication - to verify the user login using token from cookies and provide security for the API
    };
    var data = {};
    $.ajax({
        url: pendingProductReviewUrl + "?id=" + review_id + "&status=" + status,
        type: 'PATCH',
        contentType: 'application/json',
        data: JSON.stringify(data),
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            alert(resp.message);
            $('#pending_review_list_id').empty();
            get_all_products_reviews_for_user();
            window.location.href = "index.html";
            // redirect to login page
        },
        error: function (resp) {
            console.log(resp);
            alert(resp.message);
        }
    });
}

// approve all the reviews or just disapprove
function approval_of_all_reviews(status) {
    var token = getCookie("token");
    var headers = {
        'Authorization': 'Token ' + token //Authentication - to verify the user login using token from cookies and provide security for the API
    };
    var data = {};
    $.ajax({
        url: pendingProductReviewUrl + "?all=" + true + "&status=" + status,
        type: 'PATCH',
        contentType: 'application/json',
        data: JSON.stringify(data),
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            alert(resp.message);
            $('#pending_review_list_id').empty();
            get_all_products_reviews_for_user();
            window.location.href = "index.html";
            // redirect to login page
        },
        error: function (resp) {
            console.log(resp);
            alert(resp.message);
        }
    });
}

// getting user profile api
function get_user_profile() {
    var token = getCookie("token");
    var headers = {
        'Authorization': 'Token ' + token //Authentication - to verify the user login using token from cookies and provide security for the API
    };
    $.ajax({ //using AJAX
        url: userProfileUrl,
        type: 'GET',
        // contentType, dataType & headers are used to call the API , js
        contentType: 'application/json',
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            payload = resp.payload;

            $('#profile_usename').append('@' + payload.username);
            $('#profile_email').append(payload.email);
            $('#profile_location').append('Location: ' + payload.location);
            $('#profile_name').append(payload.name);
            $('#profile_skill_level').append('Skill Level: ' + payload.skill_level);
            if (payload.profile_image != "") {
                $("#imagePreview").css(
                    "background-image",
                    "url(" + payload.profile_image + ")" // wip
                );
                $("#imagePreview").hide();
                $("#imagePreview").fadeIn(650);
            }
            $("#uf_first_name").val(payload.first_name);
            $("#uf_last_name").val(payload.last_name);
            $("#uf_email").val(payload.email);
            $("#uf_location").val(payload.location);
            $("#uf_location").text(payload.location);
            $('input:radio[name="level"]').filter('[value="' + payload.skill_level + '"]').attr('checked', true);

            if (payload.skill_level == "Expert") {
                $('#beginner_level_icon').show();
                $('#intermediate_level_icon').show();
                $('#expert_level_icon').show();
            } else if (payload.skill_level == "Intermediate") {
                $('#beginner_level_icon').show();
                $('#intermediate_level_icon').show();
                $('#expert_level_icon').hide();
            } else if (payload.skill_level == "Beginner") {
                $('#beginner_level_icon').show();
                $('#intermediate_level_icon').hide();
                $('#expert_level_icon').hide();
            }
            console.log(payload);
        },
        error: function (resp) {
            console.log(resp);
            return []
        }
    });
}


// update the user profile
function update_profile() {
    user_token = getCookie("token");
    if (user_token == "") {
        $.ajax({
            url: userProfileUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Please login first"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });
    } else
        var token = getCookie("token");
    var headers = {
        'Authorization': 'Token ' + token //Authentication - to verify the user login using token from cookies and provide security for the API
    };
    var first_name = $("#uf_first_name").val();
    var last_name = $("#uf_last_name").val();
    var skill_level = $('input[name="level"]:checked').val();
    var location = $("#uf_location_select").val();
    var data = {
        "first_name": first_name,
        "last_name": last_name,
        "location": location,
        "skill_level": skill_level
    }
    
    $.ajax({ //using AJAX
        url: userProfileUrl,
        type: 'PATCH',
        // contentType, dataType & headers are used to call the API , js
        contentType: 'application/json',
        data: JSON.stringify(data),
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            get_user_profile();
            alert(resp.message);
            window.location.href = "index.html";
        },
        error: function (resp) {
            console.log(resp);
            return []
        }
    });
}

//convert image into base64
function getBaseUrl() {
    var token = getCookie("token");
    var headers = {
        'Authorization': 'Token ' + token //Authentication - to verify the user login using token from cookies and provide security for the API
    };
    var file = document.querySelector('input[type=file]')['files'][0];
    var fd = new FormData();
    fd.append('profile_image', file);
    $.ajax({
        url: userProfileUrl,
        data: fd,
        headers: headers,
        processData: false,
        contentType: false,
        type: 'PATCH',
        success: function (data) {
            console.log(data);
        }
    });
}

function add_product() { //bug
    user_type = getCookie("user_type");
    if (user_type == 1) { // Access admin only
        var headers = {
            'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
        }
        var title = $("#add-product-title").val();
        var description = $("#add-product-description").val();
        var price = 9.99
        var category = $("#add-product-category").val();
        var formData = new FormData();
        formData.append('title', title);
        formData.append('description', description);
        formData.append('price', price);
        formData.append('category', category);
        formData.append('image', $('#add-product-image')[0].files[0]);
        $.ajax({
            url: CRUDProductUrl,
            data: formData,
            type: 'POST',
            headers: headers,
            contentType: false, // NEEDED, DON'T OMIT THIS (requires jQuery 1.6+)
            processData: false, // NEEDED, DON'T OMIT THIS
            success: function (resp) {
                console.log(resp);
                alert(resp.message);
                window.location.href = "index.html";
            }
        });
    } else
        $.ajax({
            url: CRUDProductUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Insufficient Privileges"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });
}

function edit_product() {
    user_type = getCookie("user_type");
    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }
    if (user_type == 1) { // Access admin only
        var title = $("#edit-product-title").val();
        var description = $("#edit-product-description").val();
        var price = 9.99
        var category = $("#edit-product-category").val();
        var formData = new FormData();
        formData.append('title', title);
        formData.append('description', description);
        formData.append('price', price);
        formData.append('category', category);
        formData.append('image', $('#edit-product-image')[0].files[0]);
        $.ajax({
            url: CRUDProductUrl + "?id=" + getCookie("edit_product_id"),
            data: formData,
            type: 'PATCH',
            headers: headers,
            contentType: false, // NEEDED, DON'T OMIT THIS (requires jQuery 1.6+)
            processData: false, // NEEDED, DON'T OMIT THIS
            success: function (resp) {
                console.log(resp);
                //redirect to the product page
                window.location.href = "products.html";
            }
        });
    } else
        $.ajax({
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Insufficient Privileges"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });
}

function get_products() {
    user_type = getCookie("user_type");
    user_token = getCookie("token");

    if (user_type == 1) { // Access admin only
        var headers = {
            'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
        }
        $.ajax({
            url: CRUDProductUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            success: function (resp) {
                console.log(resp);
                // showing response message
                payload = resp.payload;

                console.log(payload);
                $('#product_list_table').empty();
                if (payload.length > 0) {
                    $('#product_list_table').empty();
                    for (var i = 0; i < payload.length; i++) {
                        var product = payload[i];
                        var hide_status = "";
                        if (product.is_hide == false) {
                            hide_status = "checked";
                        } else {
                            hide_status = "";
                        }
                        $("#product_list_table").append(
                            '<tr>' +
                            '<td class="table-column-pr-0">' +
                            '<div class="custom-control">' +
                            '<label class="" for=""></label>' +
                            '</div>' +
                            '</td>' +
                            '<td class="table-column-pl-0">' +
                            '<a class="media align-items-center">' +
                            '<img class="avatar avatar-lg mr-3" src="' + product.image + '" alt="Image Description">' +
                            '<div class="media-body">' +
                            '<h5 class="text-hover-primary mb-0">' + product.title + '</h5>' +
                            '</div>' +
                            '</a>' +
                            '</td>' +
                            '<td>' +
                            '<label class="toggle-switch toggle-switch-sm" for="stocksCheckbox' + product.id + '">' +
                            '<input type="checkbox" onclick="toggle_product(' + product.id + ')" class="toggle-switch-input" id="stocksCheckbox' + product.id + '" ' + hide_status + ' >' +
                            '<span class="toggle-switch-label">' +
                            '<span class="toggle-switch-indicator"></span>' +
                            '</span>' +
                            '</label>' +
                            '</td>' +
                            '<td>' +
                            '<div class="btn-group" role="group">' +
                            '<a href="edit-product.html" onclick="save_product_id_for_editing(' + product.id + ')" class="btn btn-sm btn-white">' +
                            '<i class="tio-edit"></i> Edit' +
                            '</a>' +
                            '<a onclick="delete_product(' + product.id + ')" class="btn btn-sm btn-danger">' +
                            '<i class="tio-delete-outlined"></i> Delete' +
                            '</a>' +
                            '</div>' +
                            '</td>' +
                            '</tr>'
                        )

                    }
                }
            },
            error: function (resp) {
                console.log(resp);
                return []
            }
        });

    } else
        $.ajax({
            url: CRUDProductUrl,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Insufficient Privileges"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });
}

function toggle_product(product_id) {
    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }
    $.ajax({
        url: ToggleProductUrl + "?id=" + product_id,
        type: 'PATCH',
        contentType: 'application/json',
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            get_products();
        }
    });
}



function delete_product(product_id) {

    let text = "Are you sure you want to delete this product?\nAll reviews associated with this product would be deleted as well. This action cannot be undone.";
    if (confirm(text) == true) {
        text = "Deleted"
    } else {
        return false
    }


    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }
    $.ajax({
        url: CRUDProductUrl + "?id=" + product_id,
        type: 'DELETE',
        contentType: 'application/json',
        dataType: 'json',
        headers: headers,
        async: false,
        success: function (resp) {
            console.log(resp);
            get_products();
        }
    });
}

function delete_message(message_id) {

    let text = "Are you sure you want to delete this message?\nThis action cannot be undone.";
    if (confirm(text) == true) {
        text = "Deleted"
    } else {
        return false
    }

    $.ajax({
        url: ContactUsUrl + "?id=" + message_id,
        type: 'DELETE',
        contentType: 'application/json',
        dataType: 'json',
        async: false,
        success: function (resp) {
            console.log(resp);
            get_messages();
        }
    });
}

function save_product_id_for_editing(product_id) {
    setCookie("edit_product_id", product_id, 365);
}

function get_product_by_id() {
    $.ajax({
        url: productUrl + "?id=" + getCookie("edit_product_id"),
        type: 'GET',
        contentType: 'application/json',
        dataType: 'json',
        async: false,
        success: function (resp) {
            console.log(resp);
            // showing response message
            payload = resp.payload;
            console.log(payload);
            payload = payload[0];
            $("#edit-product-title").val(payload.title);
            $("#edit-product-description").val(payload.description);
            $("#edit-product-price").val(payload.price);
            $("#edit-product-category").val(payload.category);
            $("#edit-product-image").val(payload.image);
        }
    });
}

function change_current_password() {
    user_token = getCookie("token");
    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }
    if (user_token == "") {
        $.ajax({
            url: changeCurrentPassword,
            type: 'GET',
            contentType: 'application/json',
            dataType: 'json',
            headers: headers,
            async: false,
            error: function (resp) {
                console.log(resp); // show error message on API failing
                alert("Please login first"); // show alert to user
                window.location.href = 'login.html'; //redirect to login page
            }
        });
    } else
        var $inputs = $('#user-changecurrentpassword-form :input'); // Get Data from user form by its inputs
    var data = {};
    var headers = {
        'Authorization': 'Token ' + getCookie("token") //Authentication - to verify the user login using token from cookies and provide security for the API
    }
    $inputs.each(function () { // Iterate each input and get the values by it name
        data[this.name] = $(this).val();
    });
    $.ajax({ // Ajax API call
        url: changeCurrentPassword, // API URL
        type: 'POST', // API Method
        contentType: 'application/json', // Request Data Type in header
        data: JSON.stringify(data), // Parse data into json before sending it to backend
        headers: headers,
        dataType: 'json', // The data type of body is json
        async: false,
        success: function (resp) {
            console.log(resp);
            alert(resp.message);
            window.location.href = "index.html";
        },
        error: function (xhr, status, error) {
            var err = eval("(" + xhr.responseText + ")");
            alert(err.message);
        }
    });
}

function forgot_password_email() {
    var email = $("#forgot-password-email").val();

    var data = {
        "email": email
    }
    $.ajax({
        url: forgotPasswordEmail,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        dataType: 'json',
        async: false,
        success: function (resp) {
            window.location.href = "email-verification.html?email=" + email;
        }
    });
}

function change_forgot_password() {
    var password = $("#resetPasswordSrPassword").val();
    var confirmPassword = $("#resetPasswordSrConfirmPassword").val();
    var token = $("#reset_token").val();

    if (password != confirmPassword) {
        alert("Passwords do not match");
        return false;
    }

    var data = {
        "password": password,
        "reset_token": token
    }
    $.ajax({
        url: forgotPasswordEmail,
        type: 'PATCH',
        contentType: 'application/json',
        data: JSON.stringify(data),
        dataType: 'json',
        async: false,
        success: function (resp) {
            alert("Your password has been reset successfully");
            window.location.href = "login.html";
        }
    });
}