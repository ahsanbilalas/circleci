from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^authors/$',
        views.AuthorList.as_view(),
        name='author-list'
    ),
    url(
        r'^authors/(?P<author_id>[0-9]+)/$',
        views.AuthorDetail.as_view(),
        name='author-detail'
    ),
]
