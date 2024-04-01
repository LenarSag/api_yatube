from django.urls import include, path
from rest_framework.authtoken import views as auth_view
from rest_framework import routers

from api.views import (
    PostViewSet, GroupViewSet, CommentListView, CommentDetailView
)


app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("api-token-auth/", auth_view.obtain_auth_token),
    path("", include(router.urls)),
    path(
        "posts/<int:post_id>/comments/",
        CommentListView.as_view(),
        name="comment_list"
    ),
    path(
        "posts/<int:post_id>/comments/<int:comment_id>/",
        CommentDetailView.as_view(),
        name="comment_detail",
    ),
]
