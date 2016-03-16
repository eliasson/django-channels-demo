from django.conf.urls import url, include
from rest_framework import routers

from . import views
from . import rest


router = routers.DefaultRouter()
router.register(r'foo', rest.FooViewSet)
router.register(r'bar', rest.BarViewSet)
router.register(r'foobar', rest.CompoundFooViewSet)
router.register(r'chat', rest.ChatMessageViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^fake$', views.FakeChat.as_view(), name='home'),
    url(r'^$', views.HomeView.as_view(), name='home'),
]
