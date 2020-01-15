from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class SnippetSerializer(serializers.ModelSerializer):
    """
    ModelSerializer compare with Serializer:
        * An automatically determined set of fields.
        * Simple default implementations for the create() and update() methods.
    """
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

        # owner = serializers.CharField(read_only=True, source='owner.username')
        owner = serializers.ReadOnlyField(source='owner.username')
