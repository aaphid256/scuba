# Django URL patterns

from django.urls import path

from . import views

urlpatterns = [
    # Paths for views
    path("dives", views.index, name="index"),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('dives/<int:pk>/', views.dive_detail, name='dive_detail'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/<int:pk>/', views.destination_detail,
         name='destination_detail'),
    path('dive_planner/', views.dive_planner, name='dive_planner'),
    path('diver_profile/', views.diver_profile, name='diver_profile'),

]
