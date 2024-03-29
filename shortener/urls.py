from django.urls import path

from .views import HomePageView, CreateUrlView, MyUrlView, saveUrl, visit

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<str:pk>', visit, name='visit'),
    path('shorten-url/', CreateUrlView.as_view(), name='create_url'),
    path('save-url/', saveUrl, name='save_url'),
    path('my-urls/', MyUrlView.as_view(), name='my_urls'),
]
