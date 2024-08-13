# player_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('info/<int:no>/<str:name>',views.playersea,name="playersea"),
    # path('playersear',views.playersear, name="playersear"),
    # path('users',views.usersView,name="users"),
    path('views',views.loginViews,name="views"),
    path('login',views.loginPage,name="loginPage"),
    path('contact',views.contactPage,name="contactPage"),
    path('about',views.aboutPage,name="aboutPage"),
    path('posts',views.postsPage,name="postsPage"),
    path('logout',views.logoutPage,name="logoutPage"),
]