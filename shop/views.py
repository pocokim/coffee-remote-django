from shop.models import Menu
from rest_framework import viewsets
from shop.serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
