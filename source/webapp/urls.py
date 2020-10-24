from django.urls import path
from .views import PhotoView, IndexView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'


urlpatterns = [
    path('photos/<int:pk>/', PhotoView.as_view(), name='photo_detail'),
    path('', IndexView.as_view(), name='index'),
    path('photos/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photos/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete')
]
