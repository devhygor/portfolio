from django.urls import path
from portfolio.views import index

urlpatterns = [
    path('', index),
    # path('imagem/', imagem, name='imagem'),
]