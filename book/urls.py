from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='detail'),
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('bupdate/<int:pk>', views.BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete'),
    # path('task', views.TaskView.as_view(), name='task'),
    # path('wupdate/<int:pk>', views.WriterUpdateView.as_view(), name='writer_update'),
]
