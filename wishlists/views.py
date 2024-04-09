from rest_framework import generics, permissions
from PP5.permissions import IsOwnerOrReadOnly
from wishlists.models import Wishlist
from wishlists.serializers import WishlistSerializer


class WishlistList(generics.ListCreateAPIView):
    """
    List wishlists or create a wishlist if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WishlistDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a wishlist or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()