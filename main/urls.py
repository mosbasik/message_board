from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'main.views.index', name='index'),
    url(r'^login/$', 'main.views.login', name='login'),
    url(r'^logout/$', 'main.views.logout', name='logout'),
    url(r'^create-post/$', 'main.views.create_post', name='create_post'),
    url(r'^get-posts/$', 'main.views.get_posts', name='get_posts'),
]
