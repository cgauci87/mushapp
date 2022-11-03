from . import views
from django.urls import path

# url patterns -  all templates binded
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('who-are-we.html', views.whoarewePage, name='whoarewe'),
    path('know-your-mushrooms.html', views.knowyourmushroomsPage, name='knowyourmushrooms'),
    path('forum.html', views.forumPage, name='forum'),
    path('contact-us.html', views.ContactusPage, name='contactus'),
    path('contact-us-admin.html', views.ContactusAdminPage, name='contactusadmin'),
    path('login.html', views.loginPage, name='login'),
    path('usr-registration.html', views.RegistrationPage, name='registration'),
    path('usr-account.html', views.AccountPage, name='account'),
    path('forgot-password.html', views.ForgotPasswordPage, name='forgotpassword'),
    path('password-reset.html', views.PasswordResetPage, name='passwordreset'),
    path('email-verification.html', views.EmailVerificationPage, name='emailverification'),
    path('change-password.html', views.ChangePasswordPage, name='changepassword'),
    path('write-a-review.html', views.WriteReviewPage, name='writereview'),
    path('products.html', views.ProductsPage, name='products'),
    path('add-product.html', views.AddProductPage, name='addproduct'),
    path('edit-product.html', views.EditProductPage, name='editproduct'),
    path('approve-reviews.html', views.ApproveReviewsPage, name='approvereviews'),
]
