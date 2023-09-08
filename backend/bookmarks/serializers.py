from rest_framework import serializers
from accounts.serializers import UserSerializer
from accounts.models import User
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = [
            "id", "user", "title", "url", "description",
             "thumbnail","created_at", "updated_at","site_name", "collaborators"
        ]

    def to_representation(self, instance):
        data = super(BookmarkSerializer, self).to_representation(instance)
        data['user'] =  UserSerializer(instance.user).data
        try:
            data["user"] = UserSerializer(User.objects.get(name=instance.user.id)).data
        except AttributeError:
            pass
        return data
