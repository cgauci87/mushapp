# Manual Testing

[Back to main README](README.md)

## Epic 1 - Core website functionality
### User Stories

1. [Site Navigation](https://github.com/cgauci87/mushapp/issues/1): As a user I can simply navigate through the site so that I can view desired content.

2. [Informative Landing Page](https://github.com/cgauci87/mushapp/issues/2): As a user, I can get key information about mushrooms from the landing page.

15. [Basic website layout - Navbar/Footer](https://github.com/cgauci87/mushapp/issues/15): As a user, I can find a navigation bar and footer so that I can see what content there is on the website.


The homepage instantly provides the user with all information needed to be able to navigate through the website and to gain an understanding the purpose of this site.

The navbar is self-explanatory and it is also clear to the user and responsive to mobile devices.

![login-toogle](https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/login.png)

![mymushaccount-logout-toogle](https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/mymushaccount_logout.png)

![navbar-portrait](https://res.cloudinary.com/diudkwkuw/image/upload/v1667467130/docs/navbar_portrait.png)

![navbar-landscape](https://res.cloudinary.com/diudkwkuw/image/upload/v1667467129/docs/navbar_landscape.png)


The footer provides all the action buttons depending on the user type, along with social media icon links.


![footer-user](https://res.cloudinary.com/diudkwkuw/image/upload/v1667471646/docs/footer_user.png)


16. [Contact form can be sent](https://github.com/cgauci87/mushapp/issues/16): As a user, I can send a contact form to the admin so that I can send any general queries.

![contactmush-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667476814/docs/contact_mush.png)

Upon submitting the contact form, the admin will receive the message sent and can view or delete it by accessing the "Incoming Messages" button. 

![incomingmessages-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667481409/docs/incoming_messages.png)


## Epic 2 - Admin functionality
### User Stories    
3. [Admin Login](https://github.com/cgauci87/mushapp/issues/3):As an admin user, I can log in so that I can access the site's admin pages.

Admin can login using same login page as per other users. Once logged in, addional buttons will be displayed, namely; "Pending Reviews" , "Products" & "Incoming Messages" in the Footer.

![footer-admin](https://res.cloudinary.com/diudkwkuw/image/upload/v1667471646/docs/footer_admin.png)

4. [Approve/reject reviews](https://github.com/cgauci87/mushapp/issues/4): As an admin user, I can approve or reject any incoming reviews so that I can manage the reviews section efficiently.

Admin can easily access the "Approve" and "Reject" buttons which are located on each row per product. An alert box with a message "Success" will be displayed once any of these buttons are clicked.

![pendingreviews-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667481392/docs/pending_reviews.png)
![success-message](https://res.cloudinary.com/diudkwkuw/image/upload/v1667498681/docs/success_message.png)

5. [Carousel items can be updated](https://github.com/cgauci87/mushapp/issues/5): As an admin user, I can sign in to add & remove products from the carousel so that I can make sure the website is up to date and accurately reflects what is being displayed.

Once the admin is logged in, the admin user is able to access the "Products" page, add or remove products from the carousel by using the toggle switch which is located in each row on column named "Dislay on Carousel". This will hide or unhide products by sending a PATCH AJAX request to the backend. Important to note that; if a product will be hidden - it will be dynamically hidden across all pages, so users will no longer be able to view the said product or write a review on same product or view reviews of the hidden product. On the other hand - if the product will be marked as unhidden on the toggle switch - visibility of such product in all pages will come into effect again.

![products-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667481409/docs/products.png)

6. [Carousel items have full CRUD functionality](https://github.com/cgauci87/mushapp/issues/6): As an admin user, I can create, remove, update or delete carousel items from the database so that I can ensure items are accurate and able to be added to the carousel on the site.

Once the admin is logged in, the admin user is able to access the "Products" page, can add a product by clicking "Add Product" button which will redirect Admin to the `add-product.html` page. This page has 3 required fields; Title, Description and  input image field.

![add-product](https://res.cloudinary.com/diudkwkuw/image/upload/v1667502152/docs/add_product.png)

Admin can also update an existing product by clicking the  "Edit" icon which will redirect Admin to the `edit-product.html` page. This page contains the same fields as per the `add-product.html` page. The distinction is that the fields will be pre-populated  with the current values (if the product is not hidden) and if the admin change anything from the fields - then, the changes will be overwitten by sending a PATCH AJAX request to the backend.

![edit-product](https://res.cloudinary.com/diudkwkuw/image/upload/v1667502152/docs/edit_product.png)


14. [Admin user can view contact us form messages](https://github.com/cgauci87/mushapp/issues/17): As an admin user, I can view messages which have been sent from the contact-us form.

The Admin user can view messages from the datatable which can be accessed from `contact-us-admin.html`, "Incoming Messages" button.

![incomingmessages-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667481409/docs/incoming_messages.png)


17. [Products and incoming messages can be deleted by Admin on the front-end.](https://github.com/cgauci87/mushapp/issues/17): As a logged-in Admin, I can delete an existing product or incoming message.

The Admin can delete an existing product or message by clicking the "Delete" icon. A message will pop up to confirm whether to proceed with delete action or not.

![confirm-delete-product-alert](https://res.cloudinary.com/diudkwkuw/image/upload/v1667502152/docs/delete_confirm_message.png)

    ![confirm-delete-message-alert](https://res.cloudinary.com/diudkwkuw/image/upload/v1667503959/docs/delete_confirm_message_2.png)


## Epic 3 - User Authentication
### User Stories

7. [Users can login](https://github.com/cgauci87/mushapp/issues/7): As a user, I can log in or register so that I can write reviews.
8. [Logged in status is clear to the user](https://github.com/cgauci87/mushapp/issues/8): As a user, I can easily see if I'm logged in or not so that I can choose to log in or log out depending on what I'm doing.
9. [Edit account](https://github.com/cgauci87/mushapp/issues/9): As a user, I can edit my existing account so that I change my account user details.
10. [Form will be auto-populated if the user is logged in](https://github.com/cgauci87/mushapp/issues/10): As a user, if logged in I can see an auto-populated form with my account details.

The navbar displays different nav links depending on the status of the user. If they aren't logged in already the only option visible will be `Login`.

![login-toogle](https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/login.png)

On the login page the user has the option to sign up if they do not have an account:

![login-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667473516/docs/login_page.png)
![registration-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667473516/docs/registration_page.png)

If a user is trying to register a new account with an existing email in the database - an alert will display:

![email-already-exists-alert](https://res.cloudinary.com/diudkwkuw/image/upload/v1667506482/docs/email_already_exists.png)

Once a user has registered, they are presented with a success message and redirected to login page:

![registered-successfully-alert](https://res.cloudinary.com/diudkwkuw/image/upload/v1667506750/docs/account_created_successfully.png)

Once a user logs in, they are presented with a success message and redirected to home page:

![logged-in-successfully](https://res.cloudinary.com/diudkwkuw/image/upload/v1667506482/docs/logged_in_successfully.png)


If they are logged in, then this changes - pages that require authentication show instead  `My Mush! Account` & `Logout`.

![mymushaccount-logout-toogle](https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/mymushaccount_logout.png)

Logged in users have the benefit of `My Mush! Account` form pre-populated with their account details:

![mymushaccount-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667479344/docs/my_mush_account.png)

Logged in users can submit a review by clicking on `Write A Review` button. The form contains fields and rating input - all required.

![writeareview-page](https://res.cloudinary.com/diudkwkuw/image/upload/v1667477545/docs/write_a_review.png)

If user writes a very short review (less than 10 characters long) - An alert will trigger:

![comment-must-be-longer-alert](https://res.cloudinary.com/diudkwkuw/image/upload/v1667510743/docs/comment_must_be_longer.png)

If user forgot to input star rating - An alert will trigger:

![forgotten-input-star-rating-alert](https://res.cloudinary.com/diudkwkuw/image/upload/v1667510743/docs/no_rating_input.png)


## Epic 4 - Reviews can be viewed on click
### User Stories
11. [Mushroom reviews can be viewed seperately](https://github.com/cgauci87/mushapp/issues/11): As a user, I can see reviews separately so that I will be able to easily find the information.
12. [All reviews contain key details and content](https://github.com/cgauci87/mushapp/issues/12): As a user, I can see each review and the details - who submitted the review, when it was submitted, user profile photo, user location along with the cultivation method tag and harvest season tag.

Details of the user who submitted the review are populated at the top of the review content.
The user details are: First Name, Last Name, Username, Profile Image and Country. These details can change dynamically i.e. if the user updates their account details - the previous details will get overwritten.

It also includes star rating according to the user input and the date when the review was submitted along with the review content itself.

At the bottom; tags will appear according to the user input - `season` (Spring/Summer/Autumn/Winter) and  `category` as a cultivation method (Ready-To-Fruit Block/Hardwood Log)


![reviews](https://res.cloudinary.com/diudkwkuw/image/upload/v1667468676/docs/reviews.png)

The reviews that will be displayed are only for one selected mushroom variety - so the users can navigate easily and can see reviews seperately for a specific variety.


## Epic 5 - Review dashboard
### User Stories
13. [Users are able to see review dashboard](https://github.com/cgauci87/mushapp/issues/133): As a user, I can see a review dashboard to get an overview of the overall ratings of a mushroom variety type.

The functionality of reviews dashboard of a selected mushroom variety is displayed upon user clicks the `Reviews` button of a product in Carousel.

The indicators in the dashboard provides a full picture, good visual on the average ratings of a specific variety.


![reviews_db](https://res.cloudinary.com/diudkwkuw/image/upload/v1667513366/docs/reviews_db.png
)
