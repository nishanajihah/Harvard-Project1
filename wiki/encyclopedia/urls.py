from django.urls import path

from . import views

# To get the particular route page
app_name = "enc"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("create/new-page/", views.create, name="create")
]
