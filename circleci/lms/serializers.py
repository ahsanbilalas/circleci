from rest_framework import serializers
from lms.models import Author


# Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', )

