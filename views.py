from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.views.generic import ListView
from cookie_stands.models import CookieStand
from cookie_stands.permissions import IsOwnerOrReadOnly
from cookie_stands.serializers import CookieStandSerializer


class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandListView(ListView):
    template_name = 'index.html'
    model = CookieStand
