from django.urls import path
from erc_platform.apps import ErcPlatformConfig
from rest_framework.routers import SimpleRouter

from erc_platform.views import ProductViewSet, ContactsViewSet, ChainMemberListAPIView, ChainMemberCreateAPIView, \
        ChainMemberRetrieveAPIView, ChainMemberUpdateAPIView, ChainMemberDestroyAPIView

app_name = ErcPlatformConfig.name

router = SimpleRouter()
router.register(r'product', ProductViewSet, basename="product")
router.register(r'contacts', ContactsViewSet, basename="contacts")


urlpatterns = [
    path('', ChainMemberListAPIView.as_view(), name='chain_member_list'),
    path('create/', ChainMemberCreateAPIView.as_view(), name='chain_member_create'),
    path('<int:pk>/', ChainMemberRetrieveAPIView.as_view(), name='chain_member_retrieve'),
    path('<int:pk>/update/', ChainMemberUpdateAPIView.as_view(), name='chain_member_update'),
    path('<int:pk>/delete/', ChainMemberDestroyAPIView.as_view(), name='chain_member_delete'),
]

urlpatterns += router.urls
