from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('niaz', views.niaz, name="niaz"),
    path('<str:name>', views.greet, name="greet")
]