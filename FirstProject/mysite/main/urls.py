from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
path("logout/", LogoutView.as_view(next_page='/home'), name='logout'),
]