from django.urls import path
from .views import PhotoFavorView, PhotoUnFavorView

app_name = 'api'


urlpatterns = [
    path('article/<int:pk>/like/', PhotoFavorView.as_view(), name='like'),
    path('article/<int:pk>/unlike/', PhotoUnFavorView.as_view(), name='unlike')
]
