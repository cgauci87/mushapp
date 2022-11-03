from django.shortcuts import render
from django.views import View

# to render;

def index(request):
    """ Return homepage """
    return render(request, 'index.html')


def whoarewePage(request):
    """ Who Are We page """
    return render(request, 'who-are-we.html')


def knowyourmushroomsPage(request):
    """ Know Your Mushrooms page """
    return render(request, 'know-your-mushrooms.html')


def forumPage(request):
    """ Forum page """
    return render(request, 'forum.html')


def ContactusPage(request):
    """ Contact Us page """
    return render(request, 'contact-us.html')


def ContactusAdminPage(request):
    """ Contact Us Admin page """
    return render(request, 'contact-us-admin.html')


def loginPage(request):
    """ Return Login page """
    return render(request, 'login.html')


def RegistrationPage(request):
    """ Return Registration page """
    return render(request, 'usr-registration.html')


def AccountPage(request):
    """ Return Account page """
    return render(request, 'usr-account.html')


def ForgotPasswordPage(request):
    """ Forgot Password page """
    return render(request, 'forgot-password.html')


def PasswordResetPage(request):
    """ Password Reset page """
    return render(request, 'password-reset.html')


def EmailVerificationPage(request):
    """ Email Verification page """
    return render(request, 'email-verification.html')


def ChangePasswordPage(request):
    """ Change Password page """
    return render(request, 'change-password.html')


def WriteReviewPage(request):
    """ Write Review page """
    return render(request, 'write-a-review.html')


def ProductsPage(request):
    """ Products page """
    return render(request, 'products.html')


def AddProductPage(request):
    """ Add product page """
    return render(request, 'add-product.html')


def EditProductPage(request):
    """ Edit product page """
    return render(request, 'edit-product.html')


def ApproveReviewsPage(request):
    """ Approve reviews page """
    return render(request, 'approve-reviews.html')
