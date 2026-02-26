from django.urls import path

from .views import HomePageView,AboutPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="page_list"),
    path("about/", AboutPageView.as_view(), name="about"),
]
