from django.urls import path, include
from . views import ShowAccountsPage

urlpatterns = [
    path('signup/', ShowAccountsPage.show_signup, name='signup'),
    path('login/', ShowAccountsPage.show_login, name='login'),
    path('logout/', ShowAccountsPage.show_logout, name='logout'),
]