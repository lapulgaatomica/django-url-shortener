from django.urls import path

from .views import HomePageView, CreateUrlView, saveUrl, visit

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('visit/<str:pk>', visit, name='visit'),
    path('shorten-url/', CreateUrlView.as_view(), name='create_url'),
    path('save-url/', saveUrl, name='save_url'),
]
