from django.urls import path

from bboard.views import *


urlpatterns = [

    path('', login_html),
    path('html/', index_html)


]