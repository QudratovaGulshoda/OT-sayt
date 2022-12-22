from django.urls import path
from .views import *
urlpatterns = [
    
    path('windows/',page11),
    path('macos/',page22),
    path('linux/',page33),
    path('andiroid/',page44),
    path('ios/',page55),
    path('',home),
]