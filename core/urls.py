from .views import HomeView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('home/', csrf_exempt(HomeView.as_view())),
]