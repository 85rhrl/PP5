from django.urls import path
from ownlists import views

urlpatterns = [
    path("ownlists/", views.OwnlistList.as_view()),
    path("ownlists/<int:pk>/", views.OwnlistDetail.as_view()),
]
