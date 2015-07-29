from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^create-post/$', 'main.views.create_post', name='create_post'),
    url(r'^get-posts/$', 'main.views.get_posts', name='get_posts'),
]
