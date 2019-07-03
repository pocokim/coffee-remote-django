from order.models import Order
from rest_framework import viewsets
from order.serializers import OrderSerializer
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter