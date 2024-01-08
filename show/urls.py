from django.urls import path

from show import views

urlpatterns = [path("", views.show_elem, name="show_elem")]
