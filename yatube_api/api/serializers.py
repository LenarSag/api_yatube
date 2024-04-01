from rest_framework import serializers

from posts.models import Post, Group, Comment


# class UserSerializaer(serializers.ModelSerializer):
#     username = serializers.CharField(source="author.username",
# read_only=True)

#     class Meta:
#         model = User
#         fields = ("username",)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False
    )
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Post
        fields = (
            "id",
            "text",
            "author",
            "image",
            "group",
            "pub_date",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
