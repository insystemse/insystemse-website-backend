from django.urls import path
from presentation.views import *

urlpatterns = [
    path('new_message/', NewMessage.as_view(), name='new_message'),
]