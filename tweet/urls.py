from rest_framework import routers

from .views import TweetViewSet


router = routers.SimpleRouter()
router.register(r'tweets', TweetViewSet)
urlpatterns = router.urls
