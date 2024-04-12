from django.urls import path
from wishlists import views

urlpatterns = [
    path("wishlists/", views.WishlistList.as_view()),
    path("wishlists/<int:pk>/", views.WishlistDetail.as_view()),
]
