from django.urls import path

from .views import *


urlpatterns = [
    path('get_data/', AjaxHandlerView.as_view(), name="get_data"),
]