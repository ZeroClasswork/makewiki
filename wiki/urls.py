from django.urls import path

from . import views

urlpatterns = [
    path('', views.PageList.as_view(), name='wiki-list-page'),
    path('<str:slug>', views.PageDetailView.as_view(), name='wiki-details-page'),
]
