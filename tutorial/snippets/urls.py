from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^snippets/$',views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view()),
    url(r'^model/$',views.ModelList.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.ModelDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)