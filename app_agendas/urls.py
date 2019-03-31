from django.urls import path
from . import views

urlpatterns = [
    path('1', views.HomePageView.as_view(), name='Agendas_Publicas'),
    path('2',views.SecondPageView.as_view(),name='Agendas_Institucionais'),
]
