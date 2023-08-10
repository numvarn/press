from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author', views.author, name='author'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('author/<int:id>', views.author_detail, name='author_detail')
]
