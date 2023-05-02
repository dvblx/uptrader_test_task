from django.urls import path
from .views import *

urlpatterns = [
    path('', MenusView.as_view(), name='menus'),

]