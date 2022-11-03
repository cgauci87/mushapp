# Reviewer  

<p float="left">
<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667462060/docs/desktop.png" alt="desktop-view" width="100%"> 

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/phone.png" alt="mobile-view-portrait" width="25%"> 

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667463305/docs/landscape_phone.png" alt="mobile-view-landscape" width="50%"> 
</p>


---

[Live application can be found here](https://mushcommunity-app.herokuapp.com/)

This is a full-stack framework project built using Python, Django Rest Framework and JQuery-ajax, JavaScript, HTML and CSS. This is a mushroom community website designed
to display reviews to mushroom fanatics and allow them to make reviews. This project has been built for educational purposes.

---
## UX

## Strategy
Using the core UX principles I first started with Strategy, thinking about the target audience for this community app and the features they 
would benefit from.

The target audience for 'Mush!App' are:
- Average age group 38 years old
- People that would like to know more about fungi
- People that enjoy growing mushroom kits

These users will be looking for:
- An informative website, with information that is easy-to-find & concise
- Reviews, with essential information such as knowledge level, location and growing method
- A form to write a review
- A way to contact the admin
- The ability to make a user account to edit their account

This website will offer all of these things whilst also allowing for intuitive navigation and comfortability of use. 

Due to the age group of the users, it is assumed that most users will be viewing the site on their mobile phones and therefore creating something
responsive is integral to the design, I have used Bootstrap grids and elements & custom CSS to allow for this.

## User Stories
Please find all my defined user stories & their acceptance criteria [here](https://github.com/cgauci87/mushapp/issues)

1. As a user I can simply navigate through the site so that I can view desired content.
2. As a user, I can get key information about mushrooms from the landing page.
3. As an admin user, I can log in so that I can access the site's admin pages.
4. As an admin user, I can approve or reject any incoming reviews so that I can manage the reviews section efficiently.
5. As an admin user, I can sign in to add & remove products from the carousel so that I can make sure the website is up to date and accurately 
reflects what is being displayed.
6. As an admin user, I can create, remove, update or delete carousel items from the database so that I can ensure items are accurate and able 
to be added to the carousel on the site.
7. As a user, I can log in or register so that I can write reviews.
8. As a user, I can easily see if I'm logged in or not so that I can choose to log in or log out depending on what I'm doing.
9. As a user, I can edit my existing account so that I change my account user details.
10. As a user, if logged in I can see an auto-populated form with my account details.
11. As a user, I can see reviews separately so that I will be able to easily find the information.
12. All reviews contain key details and content.
13. As a user, I can see a reviews dashboard to get an overview of the overall ratings of a mushroom variety type.
14. As an admin user, I can view and manage messages which have been sent from the contact-us form.
15. As a user, I can find a navigation bar and footer so that I can see what content there is on the website.
16. As a user, I can send a contact form to the admin so that I can send any general queries.
17. As a logged-in Admin, I can delete an existing review or incoming message.

## Scope
In order to achieve the desired user & community goals, the following features will be included in this release:

- Responsive navbar that will navigate to the various pages throughout the site
- Landing page with information about the community and links to the reviews
- Who Are We page, provide description about the community
- Know Your Mushrooms page, with knowledge about popular mushrooms.
- Register/login feature using JWT Authentication with Django REST Framework.
- Contact form that sends an email using Gmail SMTP

## Structure
This website has been designed with simplicity in mind, each page only has key information on it so that the user can find what they want 
quickly without having to read through unnecessary things. I have separated each key feature to highlight its functionality to the user.

The website is made of three apps:

1. Website - core functionality
2. Products - product management and display
3. Users - user management

### Databases

All apps require databases to store information so I have built 7 custom models.

#### Products
There are total of 4 models in Products:

Product & ProductReview are the model names for the Products app which have custom fields along with generic fields inherited from 
baselayer.basemodels using LogsMixin.

ProductApprovalStatusChoices & ProductReviewApprovalStatusChoices are the model names for the Products app which are focused on choices 
based on admin decision -
Each product/review has either PENDING or APPROVED or REJECTED. According to the decision made by the Admin, the product/review will be either 
(hidden from being displayed to users) or approved which will be displayed to users or otherwise rejected which means the product/review 
will be deleted. 
These models use "models.TextChoices" which is built-in.

#### Users
There are total of 3 models in Users:

User & ContactUs are the model names for the Users app which have custom fields along with generic fields inherited from baselayer.basemodels
using LogsMixin.
AbstractUser class has been used, inherits the User class and was able to add additional fields required for the User in the database itself 
such as user_type, 
location, profile_image and reset_password_token. To generate access token, it inherits from baselayer.baseauthentication which has custom 
JWT authentication 
for both user types - User and Admin.

The UserTypeChoices model is being used to define user types; Admin and User.

Entity Relationship Diagram below to see how the models relate to each other: 


<p text-align="center">
    <img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/schema.jpg" alt="desktop-view" width="75%"> 
</p>

### Color Palette

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/palette.png" alt="color-palette" width="100%">


---
## Features

### Home page
**Navigation bar**: The navigation bar has links to all the active pages for the user and are clearly labelled.

If the user is logged in then the right side of the menu shows links for pages that only authorised users can visit & use, they are: 
'My Mush! Account' & 'Logout'. Otherwise, the user will be given the option to 'Login'. This change in the menu ensures users are directed
to pages they can use and preventing any frustration. Furthermore, it makes it abundantly clear what the logged-in status is to the user.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/login.png" alt="login-toogle" width="100%">

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667462059/docs/mymushaccount_logout.png" alt="mymushaccount-logout-toogle" width="100%">

The navigation bar is fully responsive and collapses on mobile screens to a hamburger icon, this easily allows the user to continue to use the navigation links without the need to press back on the browser.


<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667467130/docs/navbar_portrait.png" alt="navbar-portrait" width="25%">

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667467129/docs/navbar_landscape.png" alt="navbar-landscape" width="50%">


**Carousel with links**: Each image in the Carousel represents a mushroom variety. Once user click "Reviews" button, a smooth scrolling effect will be invoked which will display the reviews dashboard and reviews of that specific variety.


<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667467627/docs/carousel_desktop.png" alt="navbar-landscape" width="100%">


**Reviews Dashboard**: This dashboard is the first view that the user will see once the scrolling effect is invoked as mentioned above. The reviews dashboard consists of graph and average ratings of that specific variety which the user selected.


<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667468791/docs/review_dashboard.png" alt="reviews-dashboard" width="100%">


**Reviews box**: User can see the reviews just below the dashboard. Each review box consists of details such as the name who has submitted the review, username, profile image, location, date submitted along with tags such as season (Spring/Summer/Autumn/Winter) where it gives an indication to the audience when the reviewer harvested, along with the cultivation method used (Ready-To-Fruit Block/Hardwood Log).

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667468676/docs/reviews.png" alt="reviews" width="100%">


**Footer**: The footer is split into two; action buttons - depends on the user type, if user type is user, an action buttion named "Write a Review" will display. If user type is Admin, then addional buttons will be displayed, namely; "Pending Reviews" , "Products" & "Incoming Messages".    

At the bottom of the footer, icons of social media links and copyright are displayed (to all user types).


<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667471646/docs/footer_user.png" alt="footer-user" width="100%">

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667471646/docs/footer_admin.png" alt="footer-admin" width="100%">

### Login Form
**Login form**: Registered users are able to login through  the 'Login' page.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667473516/docs/login_page.png" alt="login-page" width="100%">

### Registration Form
**Registration form**: Users who wish to create an account can do so by click "Sign Up" which is found in the 'Login' Page. Once users reach the registration form, they need to fill out all five required fields. With reference to the E-mail address field - value must be unique -  not found in an existing account.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667473516/docs/registration_page.png" alt="registration-page" width="100%">

### Forgot Password Page
**Forgot Password**: If a user forgot the password and has issue logging in, user can click "Forgot Password?" link which is located in the Login Page. Once user reach the Forgot Password page, user is required to input the email address which is linked into their existing account. 

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667474249/docs/forgot_password_page.png" alt="forgotpassword-page" width="100%">

### Email Verification Page
**Email Verification**: Once the user submit their email address in the Forgot Password page; The email verification page will be displayed. This page contains instructions on how user can proceed further in order to complete the verification process.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667474249/docs/email_verification_page.png" alt="emailverification-page" width="100%">  

### Reset Token Email
**Reset Token**: An email with a link for the user to reset token will be send to the user's inbox.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667475612/docs/reset_token_email.png" alt="resettoken-email" width="100%">

### Change Password Page
**Change Password**: Once the user clicks the link provided in the email; User will be redirected to the Change Password page. User is required to input their new password and repeat it in the second field. Once user click "Change Password" button - The new password will come into effect.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667475612/docs/change_password_page.png" alt="emailverification-page" width="100%">  

### Who Are We Page

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667476814/docs/who_are_we.png" alt="whoarewe-page" width="100%">

### Know Your Mushrooms Page

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667476814/docs/know_your_mushrooms.png" alt="knowyourmushrooms-page" width="100%">

### Mush!Forum Page

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667476813/docs/forum.png" alt="mushforum-page" width="100%">

### Contact Mush! Page

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667476814/docs/contact_mush.png" alt="contactmush-page" width="100%">

### My Mush! Account Page
**User account**: A form is pre-populated with user account details. This form can be updated excluding email address as it as read-only field.
Users can also upload their own profile photo or opt to remain with the default image. Users can reset their password by clicking on the padlock icon.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667479344/docs/my_mush_account.png" alt="mymushaccount-page" width="100%">


### Write A Review Page
**Write A Review**: Once the user clicks the action button "Write A Review" in the footer, if the user is authenticated - will be redirected to the Write A Review page which contains a form with fields and rating input - all required. Otherwise, if user is not logged in - user will be redirected to the login page.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667477545/docs/write_a_review.png" alt="writeareview-page" width="100%">

---

## Admin Pages

All admin pages are accessible only by Admin, through the action buttons in the footer mentioned above. Each page contains datatable which will fetch data from database. Most of these pages have full CRUD functionality.

### Pending Reviews Page

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667481392/docs/pending_reviews.png" alt="pendingreviews-page" width="100%">

### Products Page

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667481409/docs/products.png" alt="products-page" width="100%">

### Incoming Messages Page

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667481409/docs/incoming_messages.png" alt="incomingmessages-page" width="100%">

---

## Technologies Used

I have used several technologies that have enabled this design to work:

- [Django Rest Framework](https://www.djangoproject.com/)
    - Django is the framework that has been used to build the over project and its apps.
- [Python](https://www.python.org/)
    - Python is the core programming language used to write all of the code in this application to make it fully functional.
- [jQuery.ajax()](https://api.jquery.com/jquery.ajax/)
    - Used to perform asynchronous HTTP (Ajax) requests.
- [JavaScript](https://www.w3schools.com/js/)
    - JavaScript language used to write code to make some animations functional.
- [Bootstrap](https://getbootstrap.com/)
    - Used for creating responsive design.
- [Google Fonts](https://fonts.google.com/)
    - Used to obtain the fonts linked in the header, fonts used were Raleway and Lobster
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used on the high scores and rules pages.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project.
- [GitHub](https://github.com/)
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
    - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)
    - Used as the development environment.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used to deploy my application.
- [Lucid](https://lucid.app/documents#/dashboard)
    - Used to create the ERD for the project.
- [ImageResizer](https://imageresizer.com/)
    - Used to resize images to reduce loading time.
- [Pep8](http://pep8online.com/)
    - Used to test my code for any issues or errors.
- [Grammarly](https://www.grammarly.com/)
    - Used to fix the grammar errors across the project.
- [Coloors](https://coolors.co/)
    - Used to create a colour palette for the design.
- [Cloudinary](https://cloudinary.com/)
    - Used to store all most of my static and dynamic images.
- [Favicon.io](https://favicon.io/)
    - Used to create favicon's for my website
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate all HTML code written and used in this webpage.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate all CSS code written and used in this webpage.
- [JSHint](https://jshint.com/)
    - Used to validate JS code
- [Freeformatter CSS Beautify](https://www.freeformatter.com/css-beautifier.html)
    - Used to accurately format my CSS code.
- [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html)
    - Used to accurately format my HTML code.
- [SQLite](https://www.sqlite.org/index.html)
    - I have SQLite to run my database tests locally.
- [PostgreSQL](https://www.postgresql.org/)
    - I have used Heroku's PostgreSQL relational database in deployment to store the data for my models.
---

## Testing
I have used a combination of manual and automated testing to ensure the website's functionality meets the desired intent.

### Code Validation
All of my code has been validated using an online validator specific to the language, all code now passes with zero errors. 

- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate all HTML code written and used in this webpage.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667482254/docs/html_validator_results.png" alt="w3c-html-validation" width="100%">

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate all CSS code written and used in this webpage.

<img src="https://res.cloudinary.com/diudkwkuw/image/upload/v1667482254/docs/css_validator_results.png" alt="w3c-css-validation" width="100%">

![](assets/images/css_validation.jpg)

- [JSHint](https://jshint.com/)
    - Used to validate JS code

- [Pep8](http://pep8online.com/)
    - Used to test my code for any issues or errors.


### Manual Testing

I have tested this project manually myself and have also had it peer-reviewed & tested by friends and family on desktop and mobile devices.

[TESTING.md](TESTING.md)

### Automated Testing

I have used the Coverage library throughout testing to keep track of how much of my Python code was covered by the tests I had written. From running the coverage report my website has 54% of my code tested. The remaining code is covered by manual testing.

To generate your own coverage report from the command line:

1. Install the package using `pip3 install coverage`
2. Run `coverage run manage.py test`
3. Then `coverage html` to generate the report
4. You can view the report in a browser by using the command `python3 -m http.server` and opening the `index.html` file from inside the `htmlcov` folder.

### Bugs and Fixes

 - I noticed that upon submitting a review, the new rating on the next submission won't be saved if same user try to write another review. To fix this, I've
  added `[setCookie("rating", "", 365)]` in the ajax request so to clear rating cookie upon success.

 - After deploying my project to Heroku I had an issue with my header, the  images weren't loading. After discussing the issue with mentor, I have linked 
  directly the Cloudinary image URL. 

- At various stages of my testing, upon submitting the registration form, it won't redirect to the login page. To fix this, I've added `preventDefault()` method
  to the ajax request.

---
## Deployment

The master branch of this repository has been used for the deployed version of this application.

### Using Github & Gitpod

To deploy my Django application, I had to use the [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template).

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- To create a Gitpod workspace you then need to click `Gitpod`, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
    - `git add .`: adds all modified files to a staging area
    - `git commit -m "A message explaining your commit"`: commits all changes to a local repository.
    - `git push`: pushes all your committed changes to your Github repository.

*Forking the GitHub Repository*

If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

1. Find the relevant GitHub repository
2. In the top right corner of the page, click the Fork button (under your account)
3. Your repository has now been 'Forked' and you have a copy to work on

*Cloning the GitHub Repository*

Cloning your repository will allow you to download a local version of the repository to be worked on. Cloning can also be a great way to backup your work.

1. Find the relevant GitHub repository
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down
4. Now open Gitpod & select the directory location where you would like the clone created
5. In the terminal type 'git clone' & then paste the link you copied in GitHub
6. Press enter and your local clone will be created.

### Creating an Application with Heroku

I followed the below steps using the Code Institute tutorial and [Django Blog cheatsheat](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies `pip3 freeze --local > requirements.txt`. Please note this file should be added to a .gitignore file to prevent the file from being committed. A `Procfile` is also required that specifies the commands that are executed by the app on startup. 

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in; if you do not already have an account then you will need to create one.
2. Click the `New` dropdown and select `Create New App`.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

*Heroku Settings*
You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.
- In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - SECRET_KEY - to be set to your chosen key
    - CLOUDINARY_URL - to be set to your Cloudinary API environment variable
- In the resources tab you must install 'Heroku Postgres'

*Heroku Deployment*
In the Deploy tab:
1. Connect your Heroku account to your Github Repository following these steps:
    1. Click on the `Deploy` tab and choose `Github-Connect to Github`.
    2. Enter the GitHub repository name and click on `Search`.
    3. Choose the correct repository for your application and click on `Connect`.
2. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the `Deploy Branch` button whenever you want a change made.
3. Once you have chosen your deployment method and have clicked `Deploy Branch` your application will be built and you should see the below `View` button, click this to open your application:


---
## Credits

Throughout the process of building this website, I have used various sources online to help me fix bugs & tackle issues, in addition to various modules to build the functionality of this website:

[Django REST Framework](https://www.django-rest-framework.org/)

[AJAX in Django](https://testdriven.io/blog/django-ajax-xhr/)

[Coverage](https://coverage.readthedocs.io/en/6.2/)

[Gmail SMTP](https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e)

[AJAX Request](https://davidwalsh.name/xmlhttprequest)

[AJAX, CSRF & CORS](https://www.django-rest-framework.org/topics/ajax-csrf-cors/)

[Star Rating](https://www.w3schools.com/howto/howto_css_user_rating.asp)

[JWT Authentication](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)

[Testing](https://www.youtube.com/watch?v=0MrgsYswT1c)

---
## Acknowledgements

I would like to thank my course mentor Harry Dhillon for his support and guidance throughout the course of the project and my peers on Slack for their support & feedback.

---