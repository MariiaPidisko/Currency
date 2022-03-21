from currency import views as currency_views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', currency_views.rate_list),
    path('', currency_views.index),
    path('cont/list/', currency_views.cont_list),
]
