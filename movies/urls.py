from django.urls import path
from . import views

app_name = 'movies'
# sncy: urlpatterns is 'url configuration' and should be a list, this is what django expects us to do
urlpatterns = [
    # sncy: the path('') means root path -> movies/
    # sncy: it will go to views.py and look for index()
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
