from django.urls import path
from . import views


urlpatterns = [
    path('', views.surv_list, name='surv_list'),
    path('survey/<int:pk>/', views.surv_detail, name='surv_detail'),
    path('surv/new/', views.surv_new, name='surv_new'),
]

#comment
