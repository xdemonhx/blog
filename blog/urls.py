"""
blog url configuration
tag_list        '/tag/tag_name/'        list all the entries in tag_name
category_list   '/category/cat_name/'   list all the entries in cat_name
tag             '/tag/'                 list all the tags
homepage        '/'                     homepage view
blog_detail     '/blog_id'              blog detail view
"""
from django.conf.urls import url
from .views import BlogListView, TagListView, CategoryListView, BlogDetailView, BlogListPageView

urlpatterns = [
    url(r'^tag/(?P<tag_slug>\w+)$', BlogListView.as_view(), name= 'tag'),
    url(r'^tag/(?P<tag_slug>\w+)/(?P<page>\d+)',BlogListPageView.as_view(), name='tag_page'),
    url(r'^category/(?P<category_slug>\w+)$', BlogListView.as_view(), name='category'),
    url(r'^category/(?P<category_slug>\w+)/(?P<page>\d+)', BlogListPageView.as_view(), name='category_page'),
    url(r'^home$', BlogListView.as_view(), name='home'),
    url(r'^home/(?P<page>\d+)' , BlogListPageView.as_view(), name='home_page'),
    url(r'^tags$', TagListView.as_view(), name='tag_list'),
    url(r'^category$', CategoryListView.as_view(), name='category_list'),
    url(r'^(?P<pk>\d+)', BlogDetailView.as_view(), name='blog_detail'),
]