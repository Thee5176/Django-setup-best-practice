from django.urls import Path
from .views import homePageView

urlpatterns = [
    path("", homePageView, name="home"),

]
