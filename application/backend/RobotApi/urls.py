from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('forward/<speed>/', views.forward),
    path('backward/<speed>/', views.backward),
    path('right/<speed>/', views.right),
    path('left/<speed>/', views.left),
]
