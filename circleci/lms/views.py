from rest_framework import generics
from lms.models import Author
from lms.serializers import AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_url_kwarg = 'author_id'
