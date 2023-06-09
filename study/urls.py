from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('memos/new/', views.ReviewCreateView.as_view(), name="memo-create"),
    path('memos/<int:memo_id>/edit/', views.ReviewUpdateView.as_view(), name="memo-update"),
]