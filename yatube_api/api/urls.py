from django.urls import include, path
from rest_framework.authtoken import views as auth_view
from rest_framework import routers

from api.views import (
    PostViewSet, GroupViewSet, CommentViewSet
)


API_VERSION = "v1"

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"groups", GroupViewSet, basename="group")
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet, basename="comment"
)


urlpatterns = [
    path(f"{API_VERSION}/api-token-auth/", auth_view.obtain_auth_token),
    path(f"{API_VERSION}/", include(router.urls)),
]
