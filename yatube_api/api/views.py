from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied("Удаление чужого контента запрещено!")
        return super().destroy(request, *args, **kwargs)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_post_or_404(self):
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post_or_404()
        return self.queryset.filter(post=post.id)

    def perform_create(self, serializer):
        post = self.get_post_or_404()
        serializer.save(post=post, author=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied("Удаление чужого контента запрещено!")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
