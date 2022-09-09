from django.urls import path

from . import views

urlpatterns = [
    path('',views.DemoPageView.as_view(),name='demo')
]