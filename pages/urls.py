# from . import views
# from django.urls import path
#
# urlpatterns = [
#     # Quando acessar a raiz do site ("/"), chama a view home
#     path('', views.home, name='home'),
#
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('ajuda/', views.ajuda, name='ajuda'),
]