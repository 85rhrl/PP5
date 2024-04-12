from rest_framework import generics, permissions
from PP5.permissions import IsOwnerOrReadOnly
from ownlists.models import Ownlist
from ownlists.serializers import OwnlistSerializer


class OwnlistList(generics.ListCreateAPIView):
    """
    List ownlists or create a ownlist if logged in.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OwnlistSerializer
    queryset = Ownlist.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OwnlistDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a ownlist or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = OwnlistSerializer
    queryset = Ownlist.objects.all()
