from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage ,name="homepage"),
path("countskss/",views.count ,name="count")
]
