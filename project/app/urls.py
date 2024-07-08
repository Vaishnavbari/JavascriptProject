from django.urls import path
from . import views
urlpatterns = [
  path("home/", views.HomeView.as_view(), name="HomePage"),
  path("module/", views.LoadModuleView.as_view(), name="LoadModuleView")
]